from extractors.moderators import fetch_moderators
from extractors.maps.data import extract_maps_data
from argparse import ArgumentParser
from pathlib import Path
import logging


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    arg_parser = ArgumentParser(
        description='Extract data from the RUNNING WITH RIFLES game files'
    )

    target_arg_parser = arg_parser.add_subparsers(dest='target', required=True)

    # Maps -------------------------------

    maps_arg_parser = target_arg_parser.add_parser('maps', help='Extract maps-related data')

    maps_arg_parser.add_argument(
        'steam_dir',
        help='Steam root directory',
        type=Path
    )

    maps_subtarget_arg_parser = maps_arg_parser.add_subparsers(dest='subtarget', required=True)

    maps_subtarget_arg_parser.add_parser('data', help='Extract maps metadata')
    maps_subtarget_arg_parser.add_parser('images', help='Extract maps images')

    # Ranks ------------------------------

    ranks_arg_parser = target_arg_parser.add_parser('ranks', help='Extract ranks-related data')

    ranks_arg_parser.add_argument(
        'steam_dir',
        help='Steam root directory',
        type=Path
    )

    ranks_subtarget_arg_parser = ranks_arg_parser.add_subparsers(dest='subtarget', required=True)

    ranks_subtarget_arg_parser.add_parser('data', help='Extract ranks metadata')
    ranks_subtarget_arg_parser.add_parser('images', help='Extract ranks insignia')

    # Moderators -------------------------

    target_arg_parser.add_parser('moderators', help='Extract in-game moderators on official servers')

    # ------------------------------------

    args = arg_parser.parse_args()

    if args.target == 'maps':
        if args.subtarget == 'data':
            extract_maps_data(args.steam_dir)
        elif args.subtarget == 'images':
            pass
    elif args.target == 'ranks':
        pass
    elif args.target == 'moderators':
        fetch_moderators()


if __name__ == '__main__':
    main()
