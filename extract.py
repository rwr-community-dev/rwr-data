from argparse import ArgumentParser


def main() -> None:
    arg_parser = ArgumentParser(
        description='Extract data from the RUNNING WITH RIFLES game files'
    )

    arg_parser.add_argument(
        'steamdir',
        help='Steam root directory'
    )

    command_arg_parser = arg_parser.add_subparsers(dest='command', required=True)

    maps_arg_parser = command_arg_parser.add_parser('maps', help='Extract maps-related data')

    what_map_arg_parser = maps_arg_parser.add_subparsers(dest='maps_what', required=True)

    what_map_arg_parser.add_parser('data')
    what_map_arg_parser.add_parser('maps')

    ranks_arg_parser = command_arg_parser.add_parser('ranks', help='Extract ranks-related data')
    moderators_arg_parser = command_arg_parser.add_parser('moderators', help='Extract in-game moderators on official servers')

    args = arg_parser.parse_args()

    if args.command == 'build':
        pass
    elif args.command == 'watch':
        pass


if __name__ == '__main__':
    main()
