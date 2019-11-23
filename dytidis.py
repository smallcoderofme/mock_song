from dtaidistance import dtw
import parselmouth
import numpy as np

def remove_point_zero(arr):
	will_remove = []
	for x in arr:
		if x == 0.0 or x == 0:
			will_remove.append(x)
	for x in will_remove:
		arr.remove(x)
	return arr

snd = parselmouth.Sound("will_go_next_step.mp3")
pitch = snd.to_pitch()

snd1 = parselmouth.Sound("jjxyb.mp3")
pitch1 = snd1.to_pitch()


pitch_values = pitch.selected_array['frequency']
pitch_values1 = pitch1.selected_array['frequency']

# re_value = remove_point_zero(pitch_values.tolist())
# print("pitch", re_value, len(re_value))
# re_value1 = remove_point_zero(pitch_values1.tolist())
# print("pitch1", re_value1, len(re_value1))
distance = dtw.distance(pitch_values, pitch_values1)
print(distance)
