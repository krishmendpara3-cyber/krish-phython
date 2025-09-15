# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 19:19:21 2025

@author: Meet
"""

import numpy as np
import matplotlib.pyplot as plt

fs = 1000           
duration = 1      
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

freq = 10
original = np.sin(2 * np.pi * freq * t)
scaled = 3 * original

#result
plt.figure(figsize=(10, 4))
plt.plot(t, original, label='Original 10 Hz Sine')
plt.plot(t, scaled, label='Scaled (x3)', linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('10 Hz Sine Wave: Original and Scaled')
plt.legend()
plt.grid(True)
plt.show()
