import os
from pytube import YouTube
import clipboard
import re
#pip install pytube
#pip install clipboard 
#HE RUN KARAICHA BAS HYA SATHI

def yt_download():
    yt_link_patt = re.compile(r'^https://youtu\.be/[\w-]+(\?.*)?$|^https://youtube\.com/shorts/[\w-]+(\?.*)?$')
    link = clipboard.paste()
    match = yt_link_patt.match(link)
    if match:
        try:
            yt = YouTube(link)
            stream = yt.streams.get_highest_resolution()
            # Title attribute
            # print("Downloading:", yt.title)

            # Directory making or checking
            cwd = os.path.dirname(os.path.realpath(__file__))
            foldname = "yt_downloads"
            newPath = os.path.join(cwd, foldname)
            if not os.path.exists(newPath):
                os.makedirs(newPath)
            else:
                pass

            # Download video
            stream.download(output_path=newPath) 
            # print("Download complete!")
            return "Download complete"
        except Exception as e:
            # print("Error:", e)
            return "Error occured while downloading!"
    else:
        # print("No link found on clipboard")
        return "No link found on clipboard"

yt_download()

# video_url = "https://youtu.be/UV7DA6-hLIo?feature=shared"
# 35mb cha song ahe he, mala je first bhetla yt war tech takla ;)

#https://youtu.be/cTnUoYHqGhE?feature=shared
# ha video ahe

# https://youtube.com/shorts/kEDIZn8vOgY?feature=shared
# hi short ahe