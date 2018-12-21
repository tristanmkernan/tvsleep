# TV Sleep

Restores that glorious missing feature of televisions to the computer: a sleep timer!

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
$ tvsleep --help
usage: main.py [-h] minutes

positional arguments:
  minutes     length of time to wait before putting computer to sleep

optional arguments:
  -h, --help  show this help message and exit

$ tvsleep 42  # put the computer to sleep in 42 minutes
```

# License

GPLv3+
