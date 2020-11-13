# massDownloader
Download your own Youtube videos for archiving in bulk


Prerequisites:
You need to run this on a computer running any version of linux (tested with Raspbian, Debian and Ubuntu).

Install python3
for example in a Terminal on Ubuntu run:

sudo apt-get install python3

Install Youtube downloader(refer to their license, and instructions in case something goes wrong):

sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl

sudo chmod a+rx /usr/local/bin/youtube-dl

download the Files in this Repo and extract them into any folder.
This folder will be the target for the download.
you only need DL.py and list.txt

open list.txt
Replace its contents with the links for the source you want to download (your own Videos exclusively)
If you put your videos (on Youtube) into one playlist, you can just place the link to the playlist in the file and all of the related videos wil lbe downlaoded sequentially.

make sure you use direct links not bit.ly ore other URL shorteners. also in case download failes use the link you get on a video when you click on the "share" button.
open a terminal and go to the folder containing DL.py and list.txt (or rightclick in the folder and click on "open terminal here")
run this command:
python3 DL.py

(you may need sudo before it)
the Videos specified in list.txt will no download into the working folder.
this may take a while if you have a lot of videos.
