from extractors.utils import get_directories, parse_map_path, parse_map_data, save_json
from extractors import OUTPUT_DIR, STATIC_DIR, WIKI_BASE_URL, VALID_PACKAGES
from extractors.maps import INVALID_MAPS, WIKI_PAGES
from collections import OrderedDict
from pathlib import Path
from lxml import etree
import logging

logger = logging.getLogger('maps:data')


def extract_maps_data(steam_dir: Path) -> None:
    logger.info('Extracting maps data...')

    game_dir, workshop_dir, packages_dir = get_directories(steam_dir)

    maps_paths = []

    maps_paths.extend(
        packages_dir.glob('*/maps/*/objects.svg')
    )

    maps_paths.extend(
        workshop_dir.glob('*/media/packages/*/maps/*/objects.svg')
    )

    data = OrderedDict()

    for map_path in maps_paths:
        package_id, map_id = parse_map_path(map_path.parent)

        if not map_id or map_id in INVALID_MAPS or package_id not in VALID_PACKAGES:
            logger.warning(f'Invalid map ID ({map_id}) or server type ({package_id})')

            continue

        map_xml = etree.parse(map_path)

        map_infos = map_xml.findtext('//svg:rect[@inkscape:label=\'#general\']/svg:desc', namespaces={'svg': 'http://www.w3.org/2000/svg', 'inkscape': 'http://www.inkscape.org/namespaces/inkscape'})

        if not map_infos:
            logger.error('No general map info found')

            continue

        map_infos = parse_map_data(map_infos)

        if 'name' not in map_infos:
            logger.error('Map name not found')

            continue

        logger.info(f'{package_id}:{map_id}')

        if package_id not in data:
            data[package_id] = OrderedDict()

        wiki_page = WIKI_PAGES.get(package_id, {}).get(map_id)

        data[package_id][map_id] = OrderedDict([
            ('name', map_infos['name'].replace('Pacific: ', '').replace('Edelweiss: ', '').replace('WW2: ', '').title().replace('\'S', '\'s')),
            ('wikiUrl', (WIKI_BASE_URL + wiki_page) if wiki_page else None),
            # ('hasImage', (STATIC_DIR / 'maps' / 'images' / package_id / f'{map_id}.png').exists()),
            ('hasPreview', (STATIC_DIR / 'maps' / 'images' / 'previews' / package_id / f'{map_id}.png').exists())
        ])

    # ------------------------------------

    filename = OUTPUT_DIR / 'maps' / 'data.json'

    logger.info(f'Saving to {filename}...')

    save_json(filename, data)
