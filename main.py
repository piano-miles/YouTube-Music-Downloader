from pytube import YouTube
from moviepy.editor import *
import os

url = "https://www.youtube.com/watch?v=v-8h00D6l8E"

i = 1
j = str(i)
try:
    video = YouTube(url)

    title = video.title
    video = video.streams.get_highest_resolution()

    print("Downloading "+title)
    video.download(filename='d-'+j+".mp4")
except Exception as e:
    print("Failed to download video.")
    print(e)
else:
    try:
        videoclip = VideoFileClip('d-'+j+".mp4")
        audioclip = videoclip.audio
        audioclip.write_audiofile(title+".mp3")
        audioclip.close()
        videoclip.close()
    except Exception as r:
        print("Failed to convert to mp3.")
        print(r)
    else:
        print("Deleting interim files")
        os.remove("d-"+j+".mp4")