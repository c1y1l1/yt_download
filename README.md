# yt_download
  
* 目的:製作下載youtube音樂的工具，且可用於隨身音響
* 說明:主要使用 `pytube`下載音樂，並結合`tkinter`製作GUI，由於`pytube`下載的編碼為.mp4，但音響只能讀取.mp3的檔案，因此透過`moviepy`重新編碼。
  * `image`：存放`download.py`中使用的圖片
  * `download.py`：主程式，執行此
* 使用方法:
  1. 程式有使用圖片，請先將`image`資料夾與`download.py`放在同一個位置
  2. 運行後會出現兩個視窗(小視窗：yt_download；大視窗：瀏覽器)
  <div align="center">
  <img src=https://github.com/c1y1l1/yt_download/blob/main/image_rm/1.png height="70%" width="70%"/>
  </div>
  
  3. 小視窗有A,B鍵，開始選歌前請先點A鍵設定存檔位置
  4. 使用大視窗挑選欲下載歌曲，挑好就按B鍵下載
* 其他細節:
  1. 由於目的是下載進TF卡，並用於音響，因為音響只能讀編碼為.mp3的檔案，因此有使用`moviepy`；但如果只是用於手機或電腦撥放，則可將第37行解除註解，並將第38～41行刪除
  
  ```py
  37 # yt.streams.filter().get_audio_only().download(filename=name+'.mp3', output_path=target_path)
  38 yt.streams.filter().get_audio_only().download(filename=name+'.mp4', output_path=target_path)
  39 video = AudioFileClip(os.path.join(target_path, name+'.mp4'))
  40 video.write_audiofile(os.path.join(target_path, name+'.mp3'))
  41 os.remove(os.path.join(target_path, name+'.mp4'))
  ```
  
  2. 如果已有喜歡的音樂清單，也可將第24～32行解除註解，並將第33～41行凸排
  ```py
  24   # if "&list=" in url:
  25   #     print(url)
  26   #     playlist = Playlist(url)
  27   #     for i in playlist.video_urls:
  28   #         yt = YouTube(i)
  29   #         filters = re.compile(u'[^0-9a-zA-Z\u0083\u008a\u008c\u008e\u009a\u009c\u009e\u009f\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u00ff\u0100-\u017f\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\u3130-\u318f\uff00-\uffef]+', re.UNICODE)
  30   #         filename = filters.sub('-', yt.title)
  31   #         yt.streams.filter().get_audio_only().download(filename=filename+'.mp3', output_path=target_path)
  32   # else:
  33   yt = YouTube(url)
  34   filters = re.compile(u'[^0-9a-zA-Z\u0083\u008a\u008c\u008e\u009a\u009c\u009e\u009f\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u00ff\u0100-\u017f\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\u3130-\u318f\uff00-\uffef]+', re.UNICODE)
  35   name = filters.sub('-', yt.title)
  36   # print(yt.streams.filter(progressive=True))
  37   # yt.streams.filter().get_audio_only().download(filename=name+'.mp3', output_path=target_path)
  38   yt.streams.filter().get_audio_only().download(filename=name+'.mp4', output_path=target_path)
  39   video = AudioFileClip(os.path.join(target_path, name+'.mp4'))
  40   video.write_audiofile(os.path.join(target_path, name+'.mp3'))
  41   os.remove(os.path.join(target_path, name+'.mp4'))
  ```
  <div align="center">
  <img src=https://github.com/c1y1l1/yt_download/blob/main/image_rm/2.png height="70%" width="70%"/>
  </div>
