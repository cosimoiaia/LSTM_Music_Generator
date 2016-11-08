#!/usr/bin/env python
#!/usr/bin/env python

##########################################
#
# RTTTS-player.py: Simple python RTTTS (https://en.wikipedia.org/wiki/Ring_Tone_Transfer_Language) Player
#
# Usage:
#      $ ./RTTTS-player.py HighwayT:d=8,o=5,b=180:32p,d#,d#,4d#,2p,c,c,4c#,2p,c,c,c#,c,c,c#,c,d#,4d#
#
# Author: Cosimo Iaia <cosimo.iaia@gmail.com>
# Date: 05/11/2016
#
# This file is distribuited under the terms of GNU General Public
#
#########################################


import math, pyaudio, numpy
from rtttl import parse_rtttl as rt_parser



def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return numpy.sin(numpy.arange(length) * factor)

def play_tone(stream, frequency=440, length=1, rate=44100):
    chunks = []
    chunks.append(sine(frequency, length, rate))

    chunk = numpy.concatenate(chunks) * 0.25

    stream.write(chunk.astype(numpy.float32).tostring())


def main(song):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1, rate=44100, output=1)

    try:
        tunes=rt_parser(song)
    except:
        return
    
    for note in tunes['notes']:
        play_tone(stream, frequency=note['frequency'], length=(note['duration']/1000))

    stream.close()
    p.terminate()


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
       print("Usage: player.py <RTTTS String>")
    else:
       main(sys.argv[1])
