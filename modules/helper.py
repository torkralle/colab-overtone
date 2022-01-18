import numpy as np
from fastdtw import fastdtw

def l2_norm(x, y): return (x - y) ** 2
def euclidean(x, y): return abs(x - y)

def get_square_dtw(x, y):
  return fastdtw(x, y, dist=l2_norm)

def get_euclidean_dtw(x, y):
  return fastdtw(x, y, dist=euclidean) 
  
def normalize_sound(sound, master_volume):
  sound /= np.max(np.abs(sound))
  sound *= master_volume
  return sound

def get_average(band_width, offset, H):
    ave = 0
    # Bのバンド幅内の平均を取る作業	
    for k in range(band_width):
      ave = ave + H[offset + k]
    return ave / band_width

def pool_average(band_width, number_of_band, H):
    for band in range(number_of_band):
        offset = band_width * (band - 1) 
        for k in range(band_width):
            H[offset + k] = get_average(band_width, offset, H)
    return H
