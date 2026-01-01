from typing import Dict, Union, List
from pathlib import Path
import json


def save_json(file: Path, data: Union[Dict, List]) -> None:
    file.parent.mkdir(exist_ok=True)

    with file.open('w', encoding='utf-8') as f:
        json.dump(data, f)
