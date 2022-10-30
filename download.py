from pytube import YouTube,Playlist
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory
import threading
import re
from moviepy.editor import AudioFileClip
import os
# =========================
def yt():
    options = Options()
    options.add_argument("--incognito")
    global chrome
    chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    chrome.maximize_window()
    chrome.get('https://www.youtube.com/')

def dow():
    url = chrome.current_url
    target_path = loc.get()
    # if "&list=" in url:
    #     print(url)
    #     playlist = Playlist(url)
    #     for i in playlist.video_urls:
    #         yt = YouTube(i)
    #         filters = re.compile(u'[^0-9a-zA-Z\u0083\u008a\u008c\u008e\u009a\u009c\u009e\u009f\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u00ff\u0100-\u017f\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\u3130-\u318f\uff00-\uffef]+', re.UNICODE)
    #         filename = filters.sub('-', yt.title)
    #         yt.streams.filter().get_audio_only().download(filename=filename+'.mp3', output_path=target_path)
    # else:
    yt = YouTube(url)
    filters = re.compile(u'[^0-9a-zA-Z\u0083\u008a\u008c\u008e\u009a\u009c\u009e\u009f\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u00ff\u0100-\u017f\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\u3130-\u318f\uff00-\uffef]+', re.UNICODE)
    name = filters.sub('-', yt.title)
    # print(yt.streams.filter(progressive=True))
    # yt.streams.filter().get_audio_only().download(filename=name+'.mp3', output_path=target_path)
    yt.streams.filter().get_audio_only().download(filename=name+'.mp4', output_path=target_path)
    video = AudioFileClip(os.path.join(target_path, name+'.mp4'))
    video.write_audiofile(os.path.join(target_path, name+'.mp3'))
    os.remove(os.path.join(target_path, name+'.mp4'))
    

def thread_it(func):
    t = threading.Thread(target=func) 
    t.setDaemon(True) 
    t.start()

def selectpath():
    path_= askdirectory()
    path.set(path_)

window = tk.Tk()
window.geometry('255x25+1+750')
window.resizable(0,0)
window.attributes('-topmost', 1)
window.title('yt_download')

path = StringVar()

L_img = PhotoImage(file = 'image/L.ico')
L_img = L_img.subsample(12,12)
dl_img = PhotoImage(file = 'image/dl.ico')
dl_img = dl_img.subsample(29,29)

thread_it(yt)

# label = tk.Label(window).grid(row=0,column=0)
tk.Label(window, text="下載位址:").grid(row=0, column=0)
loc = tk.Entry(window, textvariable=path)
loc.grid(row=0, column=1)
tk.Button(window, image=L_img, command=selectpath).grid(row=0,column=2)
download_butten = tk.Button(window,image=dl_img, bg='white', command=lambda:thread_it(dow)).grid(row=0, column=4)

window.mainloop()
chrome.quit()
