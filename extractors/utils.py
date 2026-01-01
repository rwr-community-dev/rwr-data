from typing import Dict, Union, List, Tuple, Optional
from extractors import RWR_STEAM_APP_ID
from pathlib import Path
import json
import re

_map_path_regex = re.compile(r'[/\\](?P<server_type>.[^/]+)[/\\]maps[/\\](?P<map_id>.+)$')


def save_json(file: Path, data: Union[Dict, List]) -> None:
    file.parent.mkdir(exist_ok=True)

    with file.open('w', encoding='utf-8') as f:
        json.dump(data, f)


def get_directories(steam_dir: Path) -> Tuple[Path, Path, Path]:
    game_dir = steam_dir / 'steamapps' / 'common' / 'RunningWithRifles'

    return (
        game_dir,
        steam_dir / 'steamapps' / 'workshop' / 'content' / str(RWR_STEAM_APP_ID),
        game_dir / 'media' / 'packages'
    )


def parse_map_path(map_path: Path) -> Tuple[Optional[str], Optional[str]]:
    server_type = None
    map_id = None

    parsed = _map_path_regex.search(str(map_path))

    if parsed:
        parsed = parsed.groupdict()

        server_type = parsed['server_type']
        map_id = parsed['map_id']

    return server_type, map_id


def parse_map_data( map_infos: str):
    map_infos = map_infos.replace('\r', '').replace('\n', '')
    entries = [entry.strip().rstrip(';') for entry in filter(None, map_infos.strip().split(';')) if not entry.lstrip().startswith('#')]
    key_value_pairs = [[key_value_pair.strip() for key_value_pair in entry.split('=', maxsplit=1)] for entry in entries]

    return {key_value_pair[0]: key_value_pair[1] for key_value_pair in key_value_pairs}
