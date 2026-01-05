from builders import OUTPUT_DIR, create_archive, copy_static_files
from builders.ranks.data import build_ranks_data
from builders.moderators import fetch_moderators
from builders.maps.data import build_maps_data
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
        description='Build data related to the RUNNING WITH RIFLES gathered from several sources'
    )

    target_arg_parser = arg_parser.add_subparsers(dest='target', required=True)

    # All --------------------------------

    all_arg_parser = target_arg_parser.add_parser('all', help='Build everything')

    all_arg_parser.add_argument(
        'steam_dir',
        help='Steam root directory',
        type=Path
    )

    all_arg_parser.add_argument(
        '-r', '--rev',
        help='Create release archive for the given revision',
        type=int
    )

    # Maps -------------------------------

    maps_arg_parser = target_arg_parser.add_parser('maps', help='Build maps-related data')

    maps_arg_parser.add_argument(
        'steam_dir',
        help='Steam root directory',
        type=Path
    )

    maps_subtarget_arg_parser = maps_arg_parser.add_subparsers(dest='subtarget', required=True)

    maps_subtarget_arg_parser.add_parser('data', help='Build map metadata')
    maps_subtarget_arg_parser.add_parser('images', help='Build map images')

    # Ranks ------------------------------

    ranks_arg_parser = target_arg_parser.add_parser('ranks', help='Build rank-related data')

    ranks_arg_parser.add_argument(
        'steam_dir',
        help='Steam root directory',
        type=Path
    )

    ranks_subtarget_arg_parser = ranks_arg_parser.add_subparsers(dest='subtarget', required=True)

    ranks_subtarget_arg_parser.add_parser('data', help='Build rank metadata')
    ranks_subtarget_arg_parser.add_parser('insignias', help='Build rank insignias')

    # Moderators -------------------------

    target_arg_parser.add_parser('moderators', help='Build in-game moderators on official servers')

    # ------------------------------------

    args = arg_parser.parse_args()

    logging.info('Removing previous builds...')

    try:
        rmtree(OUTPUT_DIR)
    except OSError:
        pass

    if args.target == 'all':
        build_maps_data(args.steam_dir)
        copy_static_files('')
        build_ranks_data(args.steam_dir)
        fetch_moderators()

        if args.rev:
            create_archive(args.rev)
    elif args.target == 'maps':
        if args.subtarget == 'data':
            build_maps_data(args.steam_dir)
        elif args.subtarget == 'images':
            copy_static_files('maps/images/previews')
    elif args.target == 'ranks':
        if args.subtarget == 'data':
            build_ranks_data(args.steam_dir)
        elif args.subtarget == 'images':
            pass
    elif args.target == 'moderators':
        fetch_moderators()


if __name__ == '__main__':
    main()
