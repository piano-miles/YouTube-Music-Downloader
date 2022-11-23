import shutil
from tkinter import filedialog
import tkinter as tk
from pytube import Search, YouTube, Playlist
from moviepy.editor import *
import os
print('Importing libraries...')


root = tk.Tk()
root.withdraw()

query = input('Enter a URL or Search for a Song. ')
videos = []
pt = ''
pl = False

if 'youtube.com' in query:
    if 'list' in query:
        print("The program has detected a playlist.")
        pl = True

        try:
            p = Playlist(query)
            pt = p.title
            for i in range(len(p.videos)):
                videos.append(
                    p.videos[i].streams.first())
        except Exception as e:
            print("Failure to download playlist:\n"+e)
            quit()

    else:
        video = YouTube(query)
        ans = input('Download "'+video.title+'"? (y/n) ')

        if 'y' in ans:
            video = video.streams.get_highest_resolution()
            videos.append(video)
        else:
            quit()

else:
    s = Search(query)
    l = True
    while l:
        results = s.results
        le = len(results)
        if le < 1:
            print("No results were found. Please try again with a different search.")
            quit()
        else:
            print('\nFound ' + str(le) + ' results for "' + query + '".')
            for i in range(le):
                print('Result ' + str(i+1) + ': '+results[i].title)
            ans = input('Load more results for "' + query + '"? (y/n) ')
            if 'y' in ans:
                s.get_next_results()
            else:
                l = False

    try:
        ans = int(
            input('Please type the number result you would like to download. ')) - 1

    except Exception as e:
        print('Invalid input:')
        print(e)
        quit()

    else:
        video = s.results[ans]
        ans = input('Download "'+video.title+'"? (y/n) ')

        if 'y' in ans:
            video = video.streams.get_highest_resolution()
            videos.append(video)
        else:
            quit()
i = 1
j = str(i)
file_path = ''

try:
    print('Please select download location.')
    file_path = filedialog.askdirectory()
    print('Selected ' + file_path)
except Exception as e:
    file_path = "./"

if pl:
    file_path += "/" + pt
    os.mkdir(file_path)

for v in videos:
    try:
        video = v
        t = video.title
        print('Downloading "' + t + '"')
        video.download(filename='d-'+j+'.mp4')

    except Exception as e:
        print('Failed to download video.')
        print(e)
        quit()

    else:
        try:
            videoclip = VideoFileClip('d-'+j+'.mp4')
            audioclip = videoclip.audio
            audioclip.write_audiofile(t+'.mp3')
            audioclip.close()
            videoclip.close()

        except Exception as r:
            print('Failed to convert to mp3.')
            print(r)

        else:
            print('Deleting interim files')
            os.remove('d-'+j+'.mp4')
            print('Moving to '+file_path)
            shutil.move('./'+t+'.mp3', file_path+'/'+t+'.mp3')
            print("Done.")
