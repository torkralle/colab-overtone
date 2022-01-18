import numpy as np

def hanning_window(N=4096):
    w = np.zeros(N)
    if N % 2 == 0:
        for n in range(N):
            w[n] = 0.5 - 0.5 * np.cos(2.0 * np.pi * n / N)
    else:
        for n in range(N):
            w[n] = 0.5 - 0.5 * np.cos(2.0 * np.pi * (n + 0.5) / N)
    return w

def simply_multiply_hanning_window(offset, x, s, N=4096):
  w = hanning_window(N)
  for n in range(N):
    x[n] = s[offset + n] * w[n]
  return x

def multiply_hanning_window(freq_arr, frame, limit_len, N=4096):
    # 必要な配列と変数を用意
    out_arr = np.zeros(N)
    w = hanning_window(N)
    is_limit = False
    offset = int(np.round(N / 2 * (frame - 1)))

    for n in range(N):
        # 何番目にハニング窓を掛けるか
        index = offset + n
        if(index == limit_len):
          print("this is limit index, ", index)
          is_limit = True
          break
        out_arr[n] = freq_arr[index] * w[n]
    return out_arr, is_limit
