# Beat tracking example
from __future__ import print_function
import librosa
from dtaidistance import dtw
# 1. Get the file path to the included audio example
# filename = librosa.util.example_audio_file()

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`

# y, sr = librosa.load('will_go_next_step.mp3')
# tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
# print(tempo)
# print(beat_frames)


y, sr = librosa.load('will_go_next_step.mp3')
y1, sr1 = librosa.load('will_go_next_step1.mp3')

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
tempo1, beat_frames1 = librosa.beat.beat_track(y=y1, sr=sr1)

o_env = librosa.onset.onset_strength(y, sr=sr)
o_env1 = librosa.onset.onset_strength(y1, sr=sr1)

# distance = dtw.distance(o_env, o_env1)
distance = dtw.distance(beat_frames, beat_frames1)
print(distance)


# times = librosa.times_like(o_env, sr=sr)
# onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)

# print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# 4. Convert the frame indices of beat events into timestamps
# beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# print(beat_frames)
# print(beat_frames, len(beat_frames))
# print(beat_times, len(beat_times))
# print(o_env)