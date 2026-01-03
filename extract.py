from extractors import OUTPUT_DIR, create_archive, copy_static_files
from extractors.ranks.data import extract_ranks_data
from extractors.moderators import fetch_moderators
from extractors.maps.data import extract_maps_data
from argparse import ArgumentParser
from shutil import rmtree
from pathlib import Path
import logging
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(name)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    arg_parser = ArgumentParser(
        description='Extract data from the RUNNING WITH RIFLES game files'
    )

    target_arg_parser = arg_parser.add_subparsers(dest='target', required=True)

    # All --------------------------------

    all_arg_parser = target_arg_parser.add_parser('all', help='Extract everything')

    all_arg_parser.add_argument(
        'steam_dir',
        help='Steam root directory',
        type=Path
    )

    all_arg_parser.add_argument(
        '-a', '--archive',
        help='Create archive for release',
        action='store_true'
    )

    # Maps -------------------------------

    maps_arg_parser = target_arg_parser.add_parser('maps', help='Extract maps-related data')

    maps_arg_parser.add_argument(
        'steam_dir',
        help='Steam root directory',
        type=Path
    )

    maps_subtarget_arg_parser = maps_arg_parser.add_subparsers(dest='subtarget', required=True)

    maps_subtarget_arg_parser.add_parser('data', help='Extract map metadata')
    maps_subtarget_arg_parser.add_parser('images', help='Extract map images')

    # Ranks ------------------------------

    ranks_arg_parser = target_arg_parser.add_parser('ranks', help='Extract rank-related data')

    ranks_arg_parser.add_argument(
        'steam_dir',
        help='Steam root directory',
        type=Path
    )

    ranks_subtarget_arg_parser = ranks_arg_parser.add_subparsers(dest='subtarget', required=True)

    ranks_subtarget_arg_parser.add_parser('data', help='Extract rank metadata')
    ranks_subtarget_arg_parser.add_parser('insignias', help='Extract rank insignias')

    # Moderators -------------------------

    target_arg_parser.add_parser('moderators', help='Extract in-game moderators on official servers')

    # ------------------------------------

    args = arg_parser.parse_args()

    logging.info('Removing previous builds...')

    try:
        rmtree(OUTPUT_DIR)
    except OSError:
        pass

    if args.target == 'all':
        extract_maps_data(args.steam_dir)
        copy_static_files('')
        extract_ranks_data(args.steam_dir)
        fetch_moderators()

        if args.archive:
            create_archive()
    elif args.target == 'maps':
        if args.subtarget == 'data':
            extract_maps_data(args.steam_dir)
        elif args.subtarget == 'images':
            copy_static_files('maps/images/previews')
    elif args.target == 'ranks':
        if args.subtarget == 'data':
            extract_ranks_data(args.steam_dir)
        elif args.subtarget == 'images':
            pass
    elif args.target == 'moderators':
        fetch_moderators()


if __name__ == '__main__':
    main()
