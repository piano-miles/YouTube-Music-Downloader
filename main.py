import os
from moviepy.editor import *
from pytube import Search, YouTube, Playlist

print('Importing libraries...')

url = ''
query = input('Enter a URL or Search for a Song. ')
video = ''

if 'youtube.com' in url:
    video = YouTube(query)
    ans = input('Download "'+video.title+'"? (y/n) ')

    if 'y' in ans:
        video = video.streams.get_highest_resolution()
    else:
        quit()
else:

    s = Search(query)
    l = True
    while l:
        results = s.results
        print('\nFound ' + len(results) + ' results for "' + query + '".')
        for i in range(len(results)):
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
        else:
            quit()
i = 1
j = str(i)

try:
    t = video.title
    print('Downloading "' + t + '"')
    video.download(filename = 'd-'+j+'.mp4')

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
        print('Done')
