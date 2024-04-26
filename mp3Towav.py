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
    input_file = ""
    filename = ""
    index = 0
    if len(args) >= 1:
        input_file = args[0]
    else:
        print("请传入 视频地址 参数")
        sys.exit(1)
    if len(args) >= 2:
        output_file = args[1]
    else:
        output_file = str(int(time.time()))  # 使用当前时间戳作为文件名
    file_path = f'{os.getcwd()}/{output_file}.wav'
    command = ['ffmpeg', '-i', input_file, '-acodec', 'pcm_s16le', '-ar', '44100', file_path]

    # 执行转换命令
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, error = process.communicate()
    # 检查是否成功转换
    if process.returncode != 0:
        print(f"Error converting MP3 to WAV: {error.decode()}")
    else:
        print("Conversion successful!")
