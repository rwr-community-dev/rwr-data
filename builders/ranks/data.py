from builders.utils import get_directories
from collections import OrderedDict
from pathlib import Path
import logging

logger = logging.getLogger('ranks:data')


def build_ranks_data(steam_dir: Path) -> None:
    logger.info('Building ranks data...')

    game_dir, workshop_dir, packages_dir = get_directories(steam_dir)

    ranks_paths = [
        # Vanilla
        packages_dir / 'vanilla' / 'factions' / 'green.xml',

        # WWII
        packages_dir / 'pacific' / 'factions' / 'allies.xml',
        packages_dir / 'ww2_base' / 'factions' / 'ukf.xml',
        packages_dir / 'pacific' / 'factions' / 'ija.xml',
        packages_dir / 'ww2_base' / 'factions' / 'pzg.xml',
        packages_dir / 'ww2_base' / 'factions' / 'wh.xml',
    ]

    data = OrderedDict()

    for rank_path in ranks_paths:
        pass
