# RWR Data

Useful, machine-readable data related to the [RUNNING WITH RIFLES](https://store.steampowered.com/app/270150/RUNNING_WITH_RIFLES/)
game.

## Download

Data aren't made available into this repo itself. They are provided in the `rwr-data.tar.gz` file of each release.

| Latest version                                                                                                                                                                  | Older version                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [![GitHub Release](https://img.shields.io/github/v/release/rwr-community-dev/rwr-data)](https://github.com/rwr-community-dev/rwr-data/releases/latest/download/rwr-data.tar.gz) | Download the desired `rwr-data.tar.gz` file on the [releases](https://github.com/rwr-community-dev/rwr-data/releases) page |

## Updates

Get notified about updates by either subscribing to the release events of this repo ("Watch" button), or by using the
[releases Atom feed](https://github.com/rwr-community-dev/mindustry-campaign-stats/releases.atom).

## Available data

  - Maps
    - Metadata (JSON)
      - Map name
      - Link to the official wiki page (if available)
      - **Annotated extract**:

        ```json5
        {
          "vanilla": { // Package (mod) name
            "map2": { // Map ID
              "name": "Keepsake Bay", // Map name (mandatory)
              "wikiUrl": "https://runningwithrifles.fandom.com/wiki/Keepsake_Bay" // Official wiki page (optional)
            }
          }
        }
        ```
    - Images (PNG). The map displayed when pressing <kbd>TAB</kbd> in-game
    - Previews (PNG, if available). In-game representative screenshot. Mostly sourced from the [official wiki](https://runningwithrifles.fandom.com/wiki/Maps)
  - Ranks
    - Metadata (JSON)
      - Rank name
      - Required XP
      - **Annotated extract**:

        ```json5
        {
          // TODO
        }
        ```
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

The code was partially extracted from the defunct [RWRS](https://github.com/EpocDotFr/rwrs) project.

### Adding a map preview

> [!NOTE]
> TODO: document.

### Creating a release

  1. Run the `python extract.py all {steamdir} -a` command (read above)
  2. Create a GitHub release following the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format
  3. The name of the release must follows this format: `{year}.{n}`, where `{year}` is the current year and `{n}` the
     last value of that year plus one
  4. Upload the resulting `data/rwr-data.tar.gz` file into the release
  5. Publish the release

> [!NOTE]
> The Python code itself is not versioned. What is versioned is the resulting data.

## Credits

  - All RUNNING WITH RIFLES assets (images, game data) © Osumia Games
  - Map previews comes from the [official RWR wiki](https://runningwithrifles.fandom.com/wiki/Maps)