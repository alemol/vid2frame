# -*- coding: utf-8 -*-

'''
Usage: frames.py -i video.mp4 -o outdir/

Extract from video.mp4 all the frames to outdir/ 

@author: Alejandro Molina
last update august 2019

'''

import os
import getopt
import sys
import shlex
import contextlib
import subprocess
from pathlib import Path
from os import (remove, makedirs)
from pipes import quote
from os.path import (split, splitext, abspath, join, exists)


def extract_frames(video_path, dir_output):
    #https://trac.ffmpeg.org/wiki/Seeking#Cuttingsmallsections
    dirout, video_name = split(abspath(video_path))
    bname = splitext(video_name)[0]

    img_out = join(dir_output,'frame_%06d_{}.jpg'.format(bname))
    # un parche para evitar dialogo interactivo de overwrite file
    with contextlib.suppress(FileNotFoundError):
        remove(Path(img_out))

    ffmpeg_cmd = 'ffmpeg -i {} {} -hide_banner'.format(quote(video_path), img_out)
    # like ffmpeg -i video.webm thumb%04d.jpg -hide_banner

    try:
        out_cmd = subprocess.run(shlex.split(ffmpeg_cmd),
            stdout=None)

    except subprocess.CalledProcessError as e:
        print('exception:{}\ncaptured output:{}'.format(e, e.output))
        raise RuntimeError('ffmpeg returned non-zero status: {}'.format(e.stderr))
        exit(1)

    print(img_out, out_cmd.returncode)



def mkdir(create_dir):
    if not exists(create_dir):
        makedirs(create_dir)
    return create_dir


if __name__ == '__main__':

    video = sys.argv[1]
    frame_rate = sys.argv[2]
    outdir = sys.argv[3]

    usage = 'Usage: frames.py -i video.mp4 -o outdir/'

    try:
        opts, args = getopt.getopt(sys.argv[1:],'i:o:h',
            ['input', 'output', 'help'])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(usage)
            sys.exit(2)
        elif opt in ('-i', '--input'):
            video = arg
        elif opt in ('-o', '--output'):
            outdir = arg

    mkdir(outdir)
    extract_frames(video, outdir)
