from extractors.utils import get_directories, parse_map_path, parse_map_data, save_json
from extractors import INVALID_MAPS, INVALID_GAME_TYPES, OUTPUT_DIR
from collections import OrderedDict
from pathlib import Path
from lxml import etree
import logging


logger = logging.getLogger('maps:data')


def extract_maps_data(steam_dir: Path) -> None:
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
        server_type, map_id = parse_map_path(map_path.parent)

        if not map_id or map_id in INVALID_MAPS or server_type in INVALID_GAME_TYPES:
            logger.warning('Invalid map ID ({}) or server type ({})'.format(map_id, server_type))

            continue

        map_xml = etree.parse(map_path)

        map_infos = map_xml.findtext('//svg:rect[@inkscape:label=\'#general\']/svg:desc', namespaces={'svg': 'http://www.w3.org/2000/svg', 'inkscape': 'http://www.inkscape.org/namespaces/inkscape'})

        if not map_infos:
            logger.warning('No general map info found')

            continue

        map_infos = parse_map_data(map_infos)

        if 'name' not in map_infos:
            logger.warning('Map name not found')

            continue

        logger.info(server_type + ':' + map_id)

        if server_type not in data:
            data[server_type] = OrderedDict()

        data[server_type][map_id] = OrderedDict([
            ('name', map_infos['name'].replace('Pacific: ', '').replace('Edelweiss: ', '').replace('WW2: ', '').title().replace('\'S', '\'s')),
            # ('has_minimap', os.path.isfile(os.path.join(app.config['MINIMAPS_IMAGES_DIR'], server_type, map_id + '.png'))),
            # ('has_preview', os.path.isfile(os.path.join(app.config['MAPS_PREVIEW_IMAGES_DIR'], server_type, map_id + '.png')))
        ])

    # ------------------------------------

    filename = OUTPUT_DIR / 'maps' / 'data.json'

    logger.info(f'Saving to {filename}')

    save_json(filename, data)

    logger.info('Done')
