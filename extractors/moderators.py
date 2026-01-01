from extractors.helpers import save_json
from extractors import OUTPUT_DIR
from pathlib import Path
from lxml import etree
import requests


def fetch_moderators() -> None:
    # Admins -----------------------------

    print('Retrieving admin list')

    response = requests.get('https://rwr.runningwithrifles.com/shared/admins.xml', verify=False)

    response.raise_for_status()

    admins_xml = etree.fromstring(response.text)

    mods = [
        item.get('value') for item in admins_xml.iterchildren('item')
    ]

    # Moderators -------------------------

    print('Retrieving moderator list')

    response = requests.get('https://rwr.runningwithrifles.com/shared/moderators.xml', verify=False)

    response.raise_for_status()

    moderators_xml = etree.fromstring(response.text)

    mods.extend(
        [item.get('value') for item in moderators_xml.iterchildren('item')]
    )

    # ------------------------------------

    filename = OUTPUT_DIR / Path('moderators.json')

    print(f'Saving to {filename}')

    save_json(filename, mods)

    print('Done')
