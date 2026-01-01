from extractors.moderators import fetch_moderators
from argparse import ArgumentParser
from pathlib import Path


def main() -> None:
    arg_parser = ArgumentParser(
        description='Extract data from the RUNNING WITH RIFLES game files'
    )

    what_arg_parser = arg_parser.add_subparsers(dest='what', required=True)

    # Maps -------------------------------

    maps_arg_parser = what_arg_parser.add_parser('maps', help='Extract maps-related data')

    maps_arg_parser.add_argument(
        'steamdir',
        help='Steam root directory',
        type=Path
    )

    what_maps_arg_parser = maps_arg_parser.add_subparsers(dest='maps_what', required=True)

    what_maps_arg_parser.add_parser('data', help='Extract maps metadata')
    what_maps_arg_parser.add_parser('images', help='Extract maps images')

    # Ranks ------------------------------

    ranks_arg_parser = what_arg_parser.add_parser('ranks', help='Extract ranks-related data')

    ranks_arg_parser.add_argument(
        'steamdir',
        help='Steam root directory',
        type=Path
    )

    what_ranks_arg_parser = ranks_arg_parser.add_subparsers(dest='ranks_what', required=True)

    what_ranks_arg_parser.add_parser('data', help='Extract ranks metadata')
    what_ranks_arg_parser.add_parser('images', help='Extract ranks insignia')

    # Moderators -------------------------

    what_arg_parser.add_parser('moderators', help='Extract in-game moderators on official servers')

    # ------------------------------------

    args = arg_parser.parse_args()

    if args.what == 'maps':
        pass
    elif args.what == 'ranks':
        pass
    elif args.what == 'moderators':
        fetch_moderators()


if __name__ == '__main__':
    main()
