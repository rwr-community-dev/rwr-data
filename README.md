# RWR Data

Useful, machine-readable data related to the [RUNNING WITH RIFLES](https://store.steampowered.com/app/270150/RUNNING_WITH_RIFLES/)
game.

## Download

Data aren't made available into this repo itself. They are provided in the `rwr-data.tar.gz` file of each release.

### Latest version

[Direct link](https://github.com/rwr-community-dev/rwr-data/releases/latest/download/rwr-data.tar.gz)

### Older version

Head to the [releases](https://github.com/rwr-community-dev/rwr-data/releases) page and download the desired `rwr-data.tar.gz` file.

## Available data

  - Maps
    - Metadata (JSON)
      - Map name
      - Link to the official wiki page (if available)
    - Images (PNG). What is displayed when pressing <kbd>TAB</kbd> in-game
    - Previews (PNG, if available). In-game representative screenshot. Mostly sourced from the [official wiki](https://runningwithrifles.fandom.com/wiki/Maps)
  - Ranks
    - Metadata (JSON)
      - Name
      - Required XP
    - Insignias (PNG)

## Development

> [!NOTE]
> You only need to read the followings if you want to update the data. **You don't need to install anything to get access
> to the data** (read above).

### Prerequisites

  - Python >= 3.10
  - RUNNING WITH RIFLES game with all its DLCs

### Installation

Clone this repo, and then the usual `pip install -r requirements.txt`.

### Usage

Everything happens through a CLI. You can read about all the available commands using:

```shell
python extract.py -h
```

You can use the `-h` (or `--help`) option for each of the subcommands as well.

The command that will probably be most used is the one that updates all the data at once:

```shell
python extract.py all {steamdir} -a 
```

Where `{steamdir}` is the absolute path to the Steam root directory. `-a` (or `--archive`) creates the release archive
from the created files.

## Credits

  - All RUNNING WITH RIFLES assets (images, game data) © Osumia Games
  - Map previews comes from the [official RWR wiki](https://runningwithrifles.fandom.com/wiki/Maps)