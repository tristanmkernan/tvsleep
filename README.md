# TV Sleep

Restores that glorious missing feature of televisions to the computer: a sleep timer!

![main](screenshots/gui.png?raw=true)

## Motivation

To use when falling asleep with Netflix or Twitch streaming.

## Caveats

Supports OS X only. PRs welcome!

## Installation

Use `pip3` to install the Python module globally.

```sh
$ pip3 install tvsleep
```

## Usage

```sh
$ tvsleep -h
usage: tvsleep [-h] [-v] [--gui] minutes

positional arguments:
  minutes        length of time to wait before putting computer to sleep

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  display extra info during run
  --gui          open the gui

$ tvsleep --gui 42 # opens the GUI with preset 42 minutes

$ tvsleep -v 42  # put the computer to sleep in 42 minutes, with countdown
```

# License

GPLv3+
