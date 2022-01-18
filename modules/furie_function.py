import numpy as np

def convolution(V, B, N=4096):
	# ボーカルV * ホーミーBがY
  Out = np.zeros(N, dtype = np.complex)
  for k in range(N):
    Out[k] = V[k] * B[k]
  return Out

def symmetric_copy(B, N=4096):
  B[0] = 0
  B[int(N / 2)] = 0
  for k in range(1, int(N / 2)):
    B[N - k] = B[k]
  return B

def convert_into_absolute_value(H, N=4096):
  for k in range(N):
    H[k] = abs(H[k])
  return H
