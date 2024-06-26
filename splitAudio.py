# -*- coding: utf-8 -*-
import sys
import time
import subprocess
import os

 # pyinstaller -F splitAudio.py   打包

def get_terminal_width():
    return 100


if __name__ == '__main__':
    args = sys.argv[1:]
    url = ""
    filename = ""
    index = 0
    if len(args) >= 1:
        url = args[0]
    else:
        print("请传入 视频地址 参数")
        sys.exit(1)
    if len(args) >= 2:
        filename = args[1]
    else:
        filename = str(int(time.time()))  # 使用当前时间戳作为文件名
    file_path = f'{os.getcwd()}/{filename}.mp3'
    command = ['ffmpeg', '-i', url, '-vn', '-acodec', 'libmp3lame', file_path]
    # command = ['ffmpeg', '-i', url, '-vn', '-acodec', 'pcm_s16le', '-ar', '44100', '-ac', '2', file_path]
    subprocess.run(command)
