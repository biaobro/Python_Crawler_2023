# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : get_duration.py
@Project            : S051_Audio_Parse
@CreateTime         : 2023/4/24 18:02
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/24 18:02 
@Version            : 1.0
@Description        : None
"""

import librosa
import wave
import contextlib
import eyed3
from pydub import AudioSegment
import os


def get_files(foldername):
    """
    遍历制定目录下的全部文件名，注意不是完整路径名
    :param foldername:
    :return:
    """
    for filepath, dirnames, filenames in os.walk(foldername):
        for filename in filenames:
            print(filename)


def get_duration_mp3(file_path):
    """
    获取mp3音频文件时长
    :param file_path:
    :return: 单位是s
    """
    mp3Info = eyed3.load(file_path)
    return mp3Info.info.time_secs


def get_duration_wav(file_path):
    """
    获取wav音频文件时长
    :param file_path:
    :return:
    """
    with contextlib.closing(wave.open(file_path, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    return duration


def get_duration_mp3_and_wav(file_path):
    """
    获取mp3/wav音频文件时长
    :param file_path:
    :return:
    """
    duration = librosa.get_duration(filename=file_path)
    return duration


# 获取wav音频时长的又一种方式
def get_wav_make(file_path):
    sound = AudioSegment.from_wav(file_path)
    duration = sound.duration_seconds  # 音频时长（ms）
    return duration


if __name__ == "__main__":
    foldername = r"F:\Python\BB-Crawler-2023\S052_Tosound\Wav\wav\wav_tosound"

    for filepath, dirnames, filenames in os.walk(foldername):
        for filename in filenames:

            # # file_path = './task_8b1DA380f9E7.wav'
            #
            # 仅mp3
            # duration = get_duration_mp3(foldername+"\\"+filename)
            #
            # # 仅wav
            # duration = get_duration_wav(foldername+"\\"+filename)
            #
            # mp3 和 wav 均可
            duration = get_duration_mp3_and_wav(foldername+"\\"+filename)
            #
            print(filename, f'duration = {duration}')
        # break
