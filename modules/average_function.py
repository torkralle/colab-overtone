def get_average(band_width, offset, H):
    ave = 0
    # Bのバンド幅内の平均を取る作業	
    for k in range(band_width):
      ave = ave + H[offset + k]
    return ave / band_width
