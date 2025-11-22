# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 22:12:15 2025

@author: mendp
"""

from plotnine.data import economics
from plotnine import ggplot, aes, geom_line

(
    ggplot(economics)  # What data to use
    + aes(x="date", y="pop")  # What variable to use
    + geom_line()  # Geometric object to use for drawing
)