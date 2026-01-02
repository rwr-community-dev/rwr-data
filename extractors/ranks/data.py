from extractors.utils import get_directories
from collections import OrderedDict
from pathlib import Path
import logging

logger = logging.getLogger('ranks:data')


def extract_ranks_data(steam_dir: Path) -> None:
    logger.info('Extracting ranks data...')

    game_dir, workshop_dir, packages_dir = get_directories(steam_dir)

    ranks_paths = packages_dir.glob('*/factions/*.xml')

    print(list(ranks_paths))

    data = OrderedDict()

    for rank_path in ranks_paths:
        pass
