# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 18:53:38 2025

@author: Meet
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000           
t = np.linspace(0, 1, fs, endpoint=False)  
f1 = 5  
f2 = 10  
sine1 = np.sin(2 * np.pi * f1 * t)
sine2 = np.sin(2 * np.pi * f2 * t)

# Add the two signals
combined_signal = sine1 + sine2

#result
plt.figure(figsize=(10, 4))
plt.plot(t, combined_signal)
plt.title('Sum of 5 Hz and 10 Hz Sine Waves')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
