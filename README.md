# vid2frame

vid2frame is a tool of generation of images for deep learning from VR movies.


Extract images from a mp4 video using `frames.py`. All frames from a video file will be send to individual `.jpg` image files. Use the following command:

```

$python frames.py -i coral_smaller.mp4 -o outframes

```


### Prerequisites

Verify you have a Python 3 installation or use a virtualenv.


```

$ python --version

Python 3.7.1

```

### Dependencies

Verify you have FFmpeg. The code was tested with ffmpeg version 4.1.


```
$ ffmpeg -version

ffmpeg version 4.1 Copyright (c) 2000-2018 the FFmpeg developers
built with Apple LLVM version 10.0.0 (clang-1000.11.45.5)
configuration: --prefix=/usr/local/Cellar/ffmpeg/4.1 --enable-shared --enable-pthreads --enable-version3 --enable-hardcoded-tables --enable-avresample --cc=clang --host-cflags= --host-ldflags= --enable-ffplay --enable-gpl --enable-libmp3lame --enable-libopus --enable-libsnappy --enable-libtheora --enable-libvorbis --enable-libvpx --enable-libx264 --enable-libx265 --enable-libxvid --enable-lzma --enable-opencl --enable-videotoolbox
libavutil      56. 22.100 / 56. 22.100
libavcodec     58. 35.100 / 58. 35.100
libavformat    58. 20.100 / 58. 20.100
libavdevice    58.  5.100 / 58.  5.100
libavfilter     7. 40.101 /  7. 40.101
libavresample   4.  0.  0 /  4.  0.  0
libswscale      5.  3.100 /  5.  3.100
libswresample   3.  3.100 /  3.  3.100
libpostproc    55.  3.100 / 55.  3.100

```


### Data

Input data must be a mp4 movie. We provide a VR movie 'coral_smaller.mp4' for test proposes.

```
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'coral_smaller.mp4':
  Metadata:
    major_brand     : mp42
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    creation_time   : 2036-02-06T06:28:16.000000Z
    encoder         : HandBrake 0.10.2 2015060900
  Duration: 00:01:00.00, start: 0.000000, bitrate: 2861 kb/s
    Stream #0:0(und): Video: h264 (Main) (avc1 / 0x31637661), yuv420p(tv, bt709), 800x450 [SAR 1:1 DAR 16:9], 2859 kb/s, 15 fps, 15 tbr, 90k tbn, 180k tbc (default)
    Metadata:
      creation_time   : 2036-02-06T06:28:16.000000Z
      handler_name    : VideoHandler
Stream mapping:
  Stream #0:0 -> #0:0 (h264 (native) -> wrapped_avframe (native))
```



## Built With

* [FFmpeg](https://ffmpeg.org/about.html) - FFmpeg multimedia framework


## Authors

* **Alejandro Molina-Villegas** - [Conacyt-CentroGeo](http://mid.geoint.mx/site/integrante/id/15.html)

* **Adán Salazar Garibay** - [Conacyt-CentroGeo](http://mid.geoint.mx/site/integrante/id/14.html)


## License

   Copyright 2019 Alejandro Molina-Villegas

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.