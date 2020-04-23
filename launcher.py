
import os
import tkinter as tk
from PIL import Image, ImageTk
from pytube import YouTube
from tkinter.ttk import Progressbar
import ffmpeg
import time

def video():
    global mediaFormat
    mediaFormat='videoaudiomerge'
def audio():
    global mediaFormat
    mediaFormat = 'audio'
def videotitle():
    Videolink = entry.get()
    yt = YouTube(Videolink)
    global videon
    videon=yt.title
def Highres():
    global mediaFormat
    mediaFormat = 'Highres'
def Confirm():
    Videolink = entry.get()
    yt = YouTube(Videolink)
    VideoName["text"] = "Title: "+yt.title
    print(yt.streams)
def itag():
    global mediaFormat
    mediaFormat = 'itagvideo'

def youtubeDownload():
    global entry
    global itagentry
    ytscript = tk.Tk()
    ytscript.geometry('980x720')
    ytscript.title("Youtube downloader")
    ytscript.configure(background='#3b3b3b')
    entry = tk.Entry(ytscript, width=100)
    entry.place(rely=0.05,relx=0.50, anchor='s')
    Gobt = tk.Button(ytscript, text="Confirm", command=Confirm)
    Gobt.place(rely=0.055, relx=0.85, anchor='s')
    global VideoName
    VideoName = tk.Label(ytscript, text="Title: ", wraplength=180)
    VideoName.place(rely=0.25, relx=0.90, anchor='s')
    Selecttype = tk.Label(ytscript, text="Select the video/audio type")
    Selecttype.place(rely=0.30, relx=0.9, anchor='s')
    CheckVar1 = tk.IntVar()
    CheckVar2 = tk.IntVar()
    CheckVar3 = tk.IntVar()
    CheckVar4 = tk.IntVar()
    C1 = tk.Checkbutton(ytscript, text="Only Audio", variable=CheckVar1, onvalue=1, offvalue=0, command=audio)
    C2 = tk.Checkbutton(ytscript, text="Video and audio for merge", variable=CheckVar2, onvalue=1, offvalue=0, command=video)
    C3 = tk.Checkbutton(ytscript, text="Highest resolution for streams", variable=CheckVar3, onvalue=1, offvalue=0,command=Highres)
    C4 = tk.Checkbutton(ytscript, text="By itag: ", variable=CheckVar4, onvalue=1, offvalue=0,command=itag)
    C1.place(rely=0.34, relx=0.9, anchor='s')
    C2.place(rely=0.38, relx=0.9, anchor='s')
    C3.place(rely=0.42, relx=0.9, anchor='s')
    C4.place(rely=0.46, relx=0.841, anchor='s')
    itagentry = tk.Entry(ytscript, width=100)
    itagentry.place(rely=0.459, relx=0.93, anchor='s', width=100)
    textlink = tk.Label(ytscript, text="Link to the video: ")
    textlink.place(rely=0.05, relx=0.1, anchor='s')
    downloadbt = tk.Button(ytscript, text="Download", command=download)
    downloadbt.place(rely=0.50, relx=0.9, anchor='s')
    #global progress
    #progress = Progressbar(ytscript,length=180, mode='determinate')
    #progress.place(rely=0.54, relx=0.90, anchor='s')
    global status
    status = tk.Label(ytscript, text="Click Download to start")
    status.place(rely=0.55, relx=0.90, anchor='s')
    ytscript.mainloop()

def download():
    Videolink = entry.get()
    print(Videolink)
    yt = YouTube(Videolink)
    print("Video title: " + yt.title)
    status["text"] = "Downloading..."
    if mediaFormat == "audio":
        stream = yt.streams.filter(only_audio=True).first()
        stream.download()
    if mediaFormat == "videoaudiomerge":
        streamvideo = yt.streams.filter(adaptive=True, file_extension='mp4').first()
        streamvideo.download(filename="video")
        streamaudio = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        streamaudio.download(filename="audio")
    if mediaFormat == "Highres":
        yt.streams[0].download()
    if mediaFormat == "itagvideo":
        tag = itagentry.get()
        itagstream = yt.streams.get_by_itag(tag)
        itagstream.download()
    status["text"] = "Download finished"


def mergefiles():
    video_stream = ffmpeg.input('video.mp4')
    audio_stream = ffmpeg.input('audio.mp4')
    ffmpeg.output(audio_stream, video_stream, 'out.mp4').run()

window = tk.Tk()
window.geometry('980x720')
window.title("Scriptz by Ferferite")
Youtube = tk.Button(window, text="Youtube video/audio downloader", command=youtubeDownload)
MergeVideo = tk.Button(window, text="Merge video with audio with ffmpeg", command=mergefiles)
Youtube.grid(column=0, row=0)
MergeVideo.grid(column=0, row=1)
window.mainloop()