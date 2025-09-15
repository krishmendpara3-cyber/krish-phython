# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 19:17:43 2025

@author: Meet
"""

import numpy as np
import matplotlib.pyplot as plt


fs = 1000          
duration = 1       # Duration in seconds
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

freq = 5
original = np.sin(2 * np.pi * freq * t)
shift = 0.1
shifted = np.sin(2 * np.pi * freq * (t - shift))

#result
plt.figure(figsize=(10, 4))
plt.plot(t, original, label="Original 5 Hz Sine")
plt.plot(t, shifted, label="Shifted by 0.1s", linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Original and Shifted 5 Hz Sine Wave')
plt.legend()
plt.grid(True)
plt.show()
