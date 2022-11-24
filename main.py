import os
from sys import platform
from moviepy.editor import *
from pytube import Search, YouTube, Playlist
import tkinter as tk
from tkinter import filedialog
import shutil
from tqdm import tqdm
import time

ta = True

if platform == 'linux' or platform == 'linux2':
    print('Running on Linux')
elif platform == 'darwin':
    print('Running on MacOS.')
    print('Tkinter will be disabled, meaning you will have to manually enter a file path.')
    ta = False
elif platform == 'win32':
    print('Running on Windows')

if ta:
    try:
        root = tk.Tk()
        root.withdraw()
    except Exception as e:
        print("\nThere seems to be an issue with Tkinter on your machine.\n")
        print(e)
        ta = False
    else:
        ta = True

rep = True

while rep:
    query = input(
        'Enter a URL of a video, song, or playlist, or search for a song. ')
    videos = []
    pt = ''
    pl = False

    if 'youtube.com' in query:
        if 'list' in query:
            pl = True

            try:
                p = Playlist(query)
                pt = p.title

            except Exception as e:
                print("Failure to download playlist:\n"+str(e))
                time.sleep(5)
                quit()

        else:
            video = YouTube(query)
            ans = input('Download "'+video.title+'"? (y/n) ')

            if 'y' in ans:
                video = video.streams.get_highest_resolution()
                videos.append(video)
            else:
                time.sleep(5)
                quit()

    else:
        s = Search(query)
        l = True
        while l:
            results = s.results
            le = len(results)
            if le < 1:
                print("No results were found. Please try again with a different search.")
                time.sleep(5)
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
            time.sleep(5)
            quit()

        else:
            video = s.results[ans]
            ans = input('Download "'+video.title+'"? (y/n) ')

            if 'y' in ans:
                video = video.streams.get_highest_resolution()
                videos.append(video)
            else:
                time.sleep(5)
                quit()
    i = 1
    j = str(i)

    file_path = ''

    try:
        print('Please select download location.')
        if ta:
            file_path = str(filedialog.askdirectory())
        else:
            file_path = input('Please manually enter a file path, or leave blank to use the code folder. ')
        if file_path == '':
            ans = input('A download location has not been selected.\n' +
                        '\nWould you like to proceed with the relative path? Answering no will quit the program. (y/n) ')
            if 'y' in ans:
                file_path = os.getcwd()+'/'
            else:
                time.sleep(5)
                quit()
        print('Selected ' + file_path)

    except Exception as e:
        ans = input('A download location has not been selected.\n' + str(e) +
                    '\nWould you like to proceed with the relative path? Answering no will quit the program. (y/n) ')
        if 'y' in ans:
            file_path = os.getcwd()+'/'
        else:
            time.sleep(5)
            quit()

    if pl:
        ans = input('The program has detected a playlist named "' +
                    pt + '". Do you wish to continue? (y/n) ')
        if 'y' in ans:
            print("Adding videos to queue")
            for i in tqdm(range(len(p.videos))):
                videos.append(p.videos[i].streams.first())

            file_path += '/' + pt
            try:
                os.mkdir(file_path)
            except Exception as e:
                if 'FileExistsError' in str(e):
                    for f in os.listdir(file_path):
                        os.remove(os.path.join(file_path, f))

        else:
            time.sleep(5)
            quit()

    for k in tqdm(range(len(videos))):
        video = videos[k]

        try:
            t = video.title
            print(' Downloading "' + t + '"')
            video.download(filename='d-'+str(j)+'.mp4')

        except Exception as e:
            print('Failed to download video.')
            print(e)
            time.sleep(5)
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
                print(' Deleting interim files')
                os.remove('d-'+str(j)+'.mp4')
                print('Moving to '+file_path)
                shutil.move(os.getcwd()+'/'+t+'.mp3', file_path+'/'+t+'.mp3')

        j += 1

    if pl:
        try:
            ans = input("Would you like to zip this playlist? (y/n) ")
            if "y" in ans:
                shutil.make_archive(file_path, 'zip', file_path+'/..')
        except Exception as e:
            print("Failed to zip file.")
            print(e)

    print("Done.")

    ans = input("\n\nWould you like to download another file? (y/n) ")
    if not ('y' in ans):
        rep = False
        quit()
