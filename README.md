# RWR Data

Useful data related to the [RUNNING WITH RIFLES](https://store.steampowered.com/app/270150/RUNNING_WITH_RIFLES/)
game, gathered from several sources.

## Download

Data aren't made available into this repo itself. They are provided in the `rwr-data.tar.gz` file of each release.

| Latest version                                                                                                                                                                  | Older version                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [![GitHub Release](https://img.shields.io/github/v/release/rwr-community-dev/rwr-data)](https://github.com/rwr-community-dev/rwr-data/releases/latest/download/rwr-data.tar.gz) | Download the desired `rwr-data.tar.gz` file on the [releases](https://github.com/rwr-community-dev/rwr-data/releases) page |

## Updates

Get notified about updates by subscribing either to:

  - The release events of this repo ("Watch" button); or
  - The [releases Atom feed](https://github.com/rwr-community-dev/rwr-data/releases.atom)

## Available data

> [!IMPORTANT]
> Only data from **official packages** (vanilla game and official DLCs) are available. Third-party packages (mods) aren't
> planned (yet?).

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
            },
            // ...
          },
          // ...
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
          "vanilla": [ // Package (mod) name
            { // Position in the array defines the rank's level. Here it's rank 0
              "name": "Private", // Rank name
              "xp": 0 // Required amount of XP
            },
            { // Rank 1
              "name": "Private 1st Class",
              "xp": 500
            },
            // ...
          ],
          // ...
        }
        ```
    - Insignias (PNG). What is displayed in-game when hovering soldiers with your cursor
  - Moderators on official servers (JSON)
    - **Annotated extract**:

      ```json5
      [
        "ahnold", // In-game username
        "jackmayol",
        // ...
      ]
      ```

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
python build.py -h
```

You can use the `-h` (or `--help`) option for each of the subcommands as well.

The command that will probably be most used is the one that updates all the data at once:

```shell
python build.py all {steamdir} -a 
```

Where `{steamdir}` is the absolute path to the Steam root directory. `-a` (or `--archive`) creates the release archive
from the created files.

The code was partially extracted from the defunct [RWRS](https://github.com/EpocDotFr/rwrs) project.

### Adding a map preview

> [!NOTE]
> TODO: document.

### Creating a release

  1. Run the `python build.py all {steamdir} -a` command (read above)
  2. Create a GitHub release following the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format
  3. The name of the release must follows this format: `{year}.{n}`, where `{year}` is the current year and `{n}` the
     last value of that year plus one, or `1` if it's the first release of the said year
  4. Upload the resulting `data/rwr-data.tar.gz` file into the release
  5. Publish the release

> [!NOTE]
> The Python code itself is not versioned. What is versioned is the resulting data.

## Credits

  - All RUNNING WITH RIFLES assets (images, game data) © Osumia Games
  - Map previews comes from the [official RWR wiki](https://runningwithrifles.fandom.com/wiki/Maps)
