import pyaudio
import wave
import time
import sys
import math
import numpy
import musik

sound = musik.sine_wave_sound(196)
sound = musik.mix_sounds(sound, musik.square_wave_sound(161.8))
sound = musik.pitch_shift_semi(sound, 1)

sounds = []
sounds.append(sound)
sounds.append(musik.sine_wave_sound(500.8))

musik.MusicManager.start_up()

while musik.MusicManager.is_active():
    musik.MusicManager.play_sound(sound, 50)
    sound = musik.pitch_shift_semi(sound, 1)
    time.sleep(0.1)

musik.MusicManager.shut_down()