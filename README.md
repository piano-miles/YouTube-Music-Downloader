# YouTube Music Downloader

A simple tool to download YouTube videos or songs as mp3s.

## Install

This program has two dependencies: *pytube* and *moviepy*. To install these, run:

```shell
pip install -r requirements.txt
```

in the commandline.

The program also uses the os, tkinter, shutil, time, and tqdm libraries, all of which should be included in your installation of Python 3 by default.

## Usage

To search for and download a song, simply:

1) Run `main.py`,
2) Type a search for the song you want to download (include things like title and artist), and
3) Follow the directions to select your song and download it.

To download a song from a URL, simply:

1) Run `main.py`,
2) Paste the URL into the terminal, and
3) Follow the directions to confirm the song and download it.

To download a collection of songs from a YouTube playlist, simply:

1) Run `main.py`,
2) Paste the URL into the terminal, and
3) Follow the directions to confirm the playlist and download it as a folder or zip archive.

Once the program finishes running, you will find an mp3 file with your song's name in the folder where `main.py` is located.

## Note for MacOS

This program uses tkinter to prompt the user for a directory. As of this time, tkinter seems to [not work](https://www.python.org/download/mac/tcltk/) on some machines running MacOS:
> If you are using macOS 10.6 or later, the Apple-supplied Tcl/Tk 8.5 has serious bugs that can cause application crashes. If you wish to use IDLE or Tkinter, do not use the Apple-supplied Pythons. Instead, install and use a newer version of Python from python.org or a third-party distributor that supplies or links with a newer version of Tcl/Tk.
