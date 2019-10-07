from google.colab import files
from IPython.display import Image, Audio
from midi2audio import FluidSynth
from music21 import *

def audio_out(ob, soundfont='/usr/share/sounds/sf2/FluidR3_GM.sf2'):
    fs = FluidSynth(soundfont)
    fs.midi_to_audio(str(ob.write('midi')), 'output.wav')
    return Audio('output.wav')

def img_out(ob):
    return Image(filename=str(ob.write('img.png')))

def upload():
    return files.upload()

def download(path):
    return files.download(path)
