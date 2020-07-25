from __future__ import unicode_literals
import youtube_dl
import subprocess 

ydl_opts = {'format': 'bestvideo+audio/best'} 


'''
Read this:

1. 
ydl_opts = {} It will Download as Default Quality with less File Size, Good for Internet Bandwidth
2.
ydl_opts = {'format': 'bestvideo/best'} It will Download as Best Quality Available 
3.
ydl_opts = {'format': 'bestvideo+audio/best'} It will Download 2


Syntax Example:
options = {
    'format': 'bestaudio/best',  # choice of quality
    'extractaudio': True,        # only keep the audio
    'audioformat': "mp3",        # convert to mp3
    'outtmpl': '%(id)s',         # name the file the ID of the video
    'noplaylist': True,          # only download single song, not playlist
    'listformats': True,         # print a list of the formats to stdout and exit
}

Official Documentation: https://github.com/ytdl-org/youtube-dl/blob/master/README.md#embedding-youtube-dl

'''

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://youtu.be/eEVL9irXj0g']) #Youtube URL 


cmd = "ffmpeg -i Video.webm -i Audio.webm -c copy output.webm" #i renamed the files as Video and Audio
returned_output = subprocess.call(cmd, shell=True) #This will combine the Video and Audio File
