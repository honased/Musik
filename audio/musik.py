import math
import numpy
import pyaudio
import random

SAMPLE_RATE = 44100
BUFFER_SIZE = 200
CHANNELS = 1

def sine_wave(time, freq):
    return math.sin(time * 2 * math.pi * freq)

def square_wave(time, freq):
    if sine_wave(time, freq) >= 0.0: return 1.0
    return -1.0

def noise_wave(time, freq):
    return (random.random() * 2) - 1

class Sound():
    def __init__(self, samplers, frequencies) -> None:
        self.samplers = samplers
        self.frequencies = frequencies
        self.time = 0
        self.life = 0
        self.on = False

    def get_samples(self, frame_count) -> float:
            samples = []
            n_samplers = len(self.samplers)
            for i in range(frame_count):
                val = 0
                if self.on:
                    for j in range(n_samplers):
                        val += self.samplers[j](self.time, self.frequencies[j])
                samples.append((val / n_samplers))
                self.time += 1.0 / SAMPLE_RATE
                self.life -= (1.0 / SAMPLE_RATE) * 1000
                if self.life <= 0:
                    self.on = False
            return samples
    
    def get_samplers(self): return self.samplers
    def get_frequencies(self): return self.frequencies
    def get_alive(self): return self.on
    def set_life(self, life: int):
        self.life = life
        self.on = True

def sine_wave_sound(val):
    return Sound([sine_wave], [val])

def square_wave_sound(val):
    return Sound([square_wave], [val])

def noise_wave_sound(val):
    return Sound([noise_wave], [val])

def mix_sounds(s1: Sound, s2: Sound) -> Sound:
    return Sound(s1.get_samplers() + s2.get_samplers(), s1.get_frequencies() + s2.get_frequencies())

def pitch_shift(s: Sound, val: int) -> Sound:
    return Sound(s.get_samplers(), [x + val for x in s.get_frequencies()] )

def pitch_shift_semi(s: Sound, semitones: int) -> Sound:
    return Sound(s.get_samplers(), [x * (math.pow(2, semitones/12)) for x in s.get_frequencies()] )

class MusicManager:
    sounds = []
    p = pyaudio.PyAudio()
    stream = None

    @staticmethod
    def musik_callback(in_data, frame_count, time_info, status):
        samples = [0] * frame_count
        for sound in MusicManager.sounds:
            sound_sample = sound.get_samples(frame_count)
            for i in range(frame_count):
                samples[i] += sound_sample[i]

        if len(MusicManager.sounds) > 0:
            for i in range(frame_count):
                samples[i] /= len(MusicManager.sounds)
                samples[i] *= 0x7fff

        for sound in MusicManager.sounds.copy():
            if not sound.get_alive():
                MusicManager.sounds.remove(sound)

        samples = numpy.int16(samples).tobytes()

        return (samples, pyaudio.paContinue)

    @staticmethod
    def play_sound(sound: Sound, ms: int):
        s = Sound(sound.get_samplers(), sound.get_frequencies())
        s.set_life(ms)
        MusicManager.sounds.append(s)

    @staticmethod
    def is_active(): return MusicManager.stream.is_active()

    @staticmethod
    def start_up():
        MusicManager.stream = MusicManager.p.open(
                format=pyaudio.paInt16,
                channels=CHANNELS,
                rate=SAMPLE_RATE,
                output=True,
                frames_per_buffer=BUFFER_SIZE,
                stream_callback=MusicManager.musik_callback)
        MusicManager.stream.start_stream()

    @staticmethod
    def shut_down():
        MusicManager.stream.stop_stream()
        MusicManager.stream.close()
        MusicManager.p.terminate()
