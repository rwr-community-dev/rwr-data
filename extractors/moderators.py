from extractors.utils import save_json
from extractors import OUTPUT_DIR
from lxml import etree
import requests
import logging

logger = logging.getLogger('moderators')


def fetch_moderators() -> None:
    # Admins -----------------------------

    logger.info('Retrieving admin list...')

    response = requests.get('https://rwr.runningwithrifles.com/shared/admins.xml', verify=False)

    response.raise_for_status()

    admins_xml = etree.fromstring(response.text)

    mods = [
        item.get('value') for item in admins_xml.iterchildren('item')
    ]

    # Moderators -------------------------

    logger.info('Retrieving moderator list..')

    response = requests.get('https://rwr.runningwithrifles.com/shared/moderators.xml', verify=False)

    response.raise_for_status()

    moderators_xml = etree.fromstring(response.text)

    mods.extend(
        [item.get('value') for item in moderators_xml.iterchildren('item')]
    )

    # ------------------------------------

    filename = OUTPUT_DIR / 'moderators.json'

    logger.info(f'Saving to {filename}...')

    save_json(filename, mods)
