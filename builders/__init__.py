from shutil import copytree
from datetime import date
from pathlib import Path
import logging
import tarfile

OUTPUT_DIR = Path('dist')
STATIC_DIR = Path('static')

RWR_STEAM_APP_ID = 270150

VALID_PACKAGES = [
    # Vanilla
    'pvp',
    'vanilla', 'vanilla.winter', 'vanilla.desert',

    # WWII
    'ww2_combined', 'pacific', 'edelweiss', 'ww2_undead',
]

WIKI_BASE_URL = 'https://runningwithrifles.fandom.com/wiki/'


def create_archive(rev: int) -> None:
    if rev < 1:
        raise ValueError('revision must be greater than zero')

    filename = OUTPUT_DIR / f'rwr-data-{date.today().year}.{rev}.tar.gz'

    logging.info(f'Compressing {OUTPUT_DIR} to {filename}...')

    with tarfile.open(filename, mode='w:gz') as f:
        f.add(OUTPUT_DIR / 'maps', 'maps')
        f.add(OUTPUT_DIR / 'ranks', 'ranks')
        f.add(OUTPUT_DIR / 'moderators.json', 'moderators.json')


def copy_static_files(path: str) -> None:
    logging.info(f'Copying static files ({path})...')

    copytree(STATIC_DIR / path, OUTPUT_DIR / path, dirs_exist_ok=True)
