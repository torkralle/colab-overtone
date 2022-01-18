import numpy as np
def highpass_filter(s):
  # 操作用の配列を用意
  length_of_s = len(s)
  d = np.zeros(length_of_s)
  d[0] = 0

  # ハイパスフィルターを掛ける
  for n in range(1, length_of_s):
    d[n] = s[n] - 0.98 * s[n-1]

  copy_arr = np.zeros(length_of_s)
  for n in range(length_of_s):
    copy_arr[n] = d[n]
  
  return copy_arr
