from builders.utils import get_directories
from collections import OrderedDict
from pathlib import Path
from pprint import pprint
import logging

logger = logging.getLogger('ranks:data')


def build_ranks_data(steam_dir: Path) -> None:
    logger.info('Building ranks data...')

    game_dir, workshop_dir, packages_dir = get_directories(steam_dir)

    ranks_paths = [
        # In Vanilla, ranks from all factions are the same, so only parse Green's ones. These ranks are valid for the
        # pvp, vanilla.desert and vanilla.winter subpackages as well
        packages_dir / 'vanilla' / 'factions' / 'green.xml',

        # For WWII packages, ranks differs between factions:
        # IJA is present and identical in both pacific and ww2_combined packages, so only parse ww2_combined ones
        packages_dir / 'ww2_combined' / 'factions' / 'ija.xml',
        # UKF is present in various flavours, however they are still identical, so only parse the main one
        packages_dir / 'ww2_base' / 'factions' / 'ukf.xml',

        # TODO the rest
    ]

    pprint(list(ranks_paths))

    data = OrderedDict()

    for rank_path in ranks_paths:
        pass
