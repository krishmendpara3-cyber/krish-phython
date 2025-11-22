# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 22:12:56 2025

@author: mendp
"""

from plotnine.data import mpg
from plotnine import ggplot, aes, geom_point

ggplot(mpg) + aes(x="class", y="hwy") + geom_point()
