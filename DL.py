#yt-downloader
import os

file = open("list.txt", "r")
for line in file:
	print("downloading video from url: " + line)
	os.system("youtube-dl " + line )
print("finished downloading")

