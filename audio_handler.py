import librosa as ls
from librosa import onset, beat
import matplotlib.pyplot as plt
import numpy as np

class Audio_Handler:
    def __init__(self, file_path: str):
        # self.audio_file = open(file_path)
        audio_series, sample_rate = ls.load(path=file_path, mono=True)  # (ndarray, float)
        # print(self.audio_series)
        self.duration = ls.get_duration(y=audio_series)
        bpm, beat_frames = self.get_bpm(audio_series=audio_series, sampling_array=sample_rate)
        print(f'bpm = {bpm}')
        # audio_frames = self.time_to_frames(audio_series=audio_series, sampling_rate=sample_rate)
        self.compute_freqs(audio_series=audio_series, sampling_rate=sample_rate, beat_frames=beat_frames)


    def get_bpm(self, audio_series: np.ndarray, sampling_array: float):  # can use to gauge accuracy of tempo
        tempo, beat_frames = beat.beat_track(y=audio_series, sr=sampling_array)
        # print('beat frames: ')
        # for b in beat_frames:
        #     print(b)
        return tempo, beat_frames


    def time_to_frames(self, audio_series: np.ndarray, sampling_rate: float):  # can pass in hop length if not default
        return ls.time_to_frames(times=audio_series, sr=sampling_rate)


    def compute_freqs(self, audio_series: np.ndarray, sampling_rate: float, beat_frames: list[int]):
        beat_sample_indices = ls.frames_to_samples(frames=beat_frames)
        # [print(b) for b in beat_sample_indices]
        audio_beats = np.asfarray([audio_series[x] for x in beat_sample_indices])
        # [print(a) for a in audio_beats]
        # need to use stft to convert the time series to frequencies
        # returns (freq_magnitude, freq, time)
        stft = ls.stft(y=audio_beats)  # get the short-time fourier transform
        for s in stft:
            print(s)


        # freqs = [ls.hz_to_note(b) for b in audio_beats]
        # print(freqs)



        # onset_strength = onset.onset_strength(y=audio_series, sr=sampling_rate)
        # correlation = ls.autocorrelate(onset_strength)
        # fig, axis = plt.subplots()
        # axis.plot(correlation)
        # axis.set(title='Auto-correlation', xlabel='Lag (frames)')
        # plt.show()
        # for x in audio_series:
        #     try:
        #         # note = ls.hz_to_note(x)
        #         print(x)
        #     except: pass
