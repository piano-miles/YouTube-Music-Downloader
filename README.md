# YouTube Music Downloader
A simple tool to download YouTube videos or songs as mp3s.
## Dependencies
This program has two non-standard dependencies: *pytube* and *moviepy*. 

To install these, run `python3 -m pip install pytube moviepy` in the commandline.

The program also uses the os, tkinter, shutil, and tqdm libraries, all of which should be included in your installation of Python 3 by default.
## Usage
To search for and download a song, simply:
1) Run `main.py`,
2) Type a search for the song you want to download (include things like title and artist), and
3) Follow the directions to select your song and download it.

To download a song from a URL, simply:
1) Run `main.py`,
2) Paste the URL into the console,
3) Type '`y`' to confirm the chosen video or song is correct.

Once the program finishes running, you will find an mp3 file with your song's name in the folder where `main.py` is located.
