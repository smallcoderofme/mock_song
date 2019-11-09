import parselmouth
import numpy as np
snd = parselmouth.Sound("qdkslg.mp3")

pitch = snd.to_pitch()

# print(pitch.selected_array['frequency'])
pitch_values = pitch.selected_array['frequency']
# pitch_values[pitch_values==0] = np.nan
print('times (s): {}'.format(pitch.xs()))
print('frequency (Hz): {}'.format(pitch_values))