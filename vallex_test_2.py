PATH = '/beegfs/home/ivan.zorin/dev/code/VALL-E-X/'

import sys
sys.path.append(PATH)

from utils.generation import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
# from IPython.display import Audio, display

import os

# download and load all models
preload_models()

presets_path = os.path.join(PATH, 'presets')
presets = os.listdir(presets_path)
# print(presets)

# generate audio from text
text_prompt = """
Hello, my name is Slimshady. Will the real Slimshady please stand up, please stand up. 
"""


preset = presets[0]
prompt = presets_path + '/' + preset
audio_array = generate_audio(text_prompt, prompt=prompt)
print(audio_array.shape)
# print(preset)
# display(Audio(audio_array, rate=SAMPLE_RATE))