# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 19:14:19 2025

@author: Meet
"""

import numpy as np
import matplotlib.pyplot as plt

fs = 500            
duration = 2         # Duration in seconds
t = np.linspace(0, duration, int(fs * duration), endpoint=False)  # Time vector
sine_wave = np.sin(2 * np.pi * 5 * t)      # 5 Hz sine wave
cosine_wave = np.cos(2 * np.pi * 10 * t)   # 10 Hz cosine wave

product_signal = sine_wave * cosine_wave

#result
plt.figure(figsize=(10, 4))
plt.plot(t, product_signal)
plt.title('Product of 5 Hz Sine and 10 Hz Cosine Waves')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
