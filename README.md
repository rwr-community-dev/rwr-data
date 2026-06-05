# RWR Data

Useful data related to the [RUNNING WITH RIFLES](https://store.steampowered.com/app/270150/RUNNING_WITH_RIFLES/) game,
gathered from several sources.

The code was partially extracted from the defunct [RWRS](https://github.com/EpocDotFr/rwrs) project.

## Download

Data aren't made available into this repo itself. They are provided in the `rwr-data-*.tar.gz` file of each
[release](https://github.com/rwr-community-dev/rwr-data/releases).

Link to latest release: [![Latest release](https://img.shields.io/github/v/release/rwr-community-dev/rwr-data)](https://github.com/rwr-community-dev/rwr-data/releases/latest)

### Automation

You'd want to automate download of the latest release file. You could do so by using [this tool](https://github.com/devmatteini/dra)
or by rolling [your own bash script](https://gist.github.com/steinwaywhw/a4cd19cda655b8249d908261a62687f8).

## Updates

There's no update schedule, data are updated as needed. Get notified about updates by subscribing either to:

  - The release events of this repo ("Watch" button); or
  - The [releases Atom feed](https://github.com/rwr-community-dev/rwr-data/releases.atom)

## Available data

> [!IMPORTANT]
> Only data from **official packages** (vanilla game and official DLCs) are available. Third-party packages (typically
> mods) aren't planned (yet?).

Emojis meaning: ✅ data is available; 🚧 data is not yet available but work is in progress; 📅 data is not yet available
but is planned to.

### Maps

#### Metadata ✅

**Format**: JSON

**Content**:

  - Map name. Extracted from the game's files
  - Link to the official wiki page (if available)

**Location**: `maps/data.json`

**Annotated extract**:

```json5
{
  "vanilla": { // Package ID
    "map2": { // Map ID
      "name": "Keepsake Bay", // Map name (mandatory)
      "wikiUrl": "https://runningwithrifles.fandom.com/wiki/Keepsake_Bay" // Official wiki page (optional)
    },
    // ...
  },
  // ...
}
```

#### Images 📅

**Format**: PNG

**Content**: The map displayed when pressing <kbd>TAB</kbd> in-game. Extracted from the game's files

**Location**: `maps/images/{package}/{name}.png`

#### Previews ✅

**Format**: PNG (if available)

**Content**: In-game representative screenshot. Mostly sourced from the [official wiki](https://runningwithrifles.fandom.com/wiki/Maps)

**Location**: `maps/images/previews/{package}/{name}.png`

### Ranks

#### Metadata 🚧

**Format**: JSON

**Content**:

Extracted from the game's files:

  - Rank name
  - Required XP

**Location**: `ranks/data.json`

**Annotated extract**:

```json5
{
  "vanilla": [ // Faction ID (NOT the package's ID). Caution: this faction ID is NOT necessarily the one used in the game's file
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

#### Insignias 📅

**Format**: PNG

**Content**: What is displayed in-game when hovering soldiers with your cursor. Extracted from the game's files

**Location**: `ranks/images/{faction}/{level}.png`

### Moderators ✅

**Format**: JSON

**Content**:

Moderators on official servers. Sourced from config actually used by official servers.

**Location**: `moderators.json`

**Annotated extract**:

```json5
[
  "ahnold", // In-game username (lowercase)
  "jackmayol",
  // ...
]
```

## Development

> [!NOTE]
> You only need to read the followings if you want to update the data. **You don't need to install anything to get access
> to the data** (read above).

### Prerequisites

  - Python >= 3.10 (developed using 3.14)
  - [Pipenv](https://pipenv.pypa.io/en/latest/)
  - RUNNING WITH RIFLES game with all its DLCs

### Installation

Clone this repo, and then `pipenv install --dev`.

### Usage

Everything happens through a CLI. You can read about all the available commands using:

```shell
pipenv run build --help
```

You can use the `--help` option for each of the subcommands as well.

### Adding a map preview

Map previews are the only images versioned into this repo since those are user-generated content. They are simply copied
into the archive upon release.

They are located in the `static/maps/images/previews` directory. The naming follows the same convention as the map's
images, e.g `{package}/{name}.png`.

### Creating a release

  1. Make sure your game installation is up to date (including DLCs)
  2. Run the `pipenv run build all {steamdir} --rev {n}` command where `{steamdir}` is the absolute path to the Steam root
     directory and `{n}`) is the desired revision. The revision must be the last value of the current year plus one, or
     `1` if it's the first release of the year
  3. Create a GitHub release following the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format
  4. The name of the release must match this format: `{year}.{n}`. It must be identical to the one found in the archive's
     name
  5. Upload the resulting `dist/rwr-data-*.tar.gz` file into the release
  6. Publish the release

## Credits

  - All RUNNING WITH RIFLES assets (images, game data) © Osumia Games
  - Map previews comes from the [official RWR wiki](https://runningwithrifles.fandom.com/wiki/Maps)
  - Original code by [@EpocDotFr](https://github.com/EpocDotFr)