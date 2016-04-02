# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 23:15:45 2016

@author: azg
"""

import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)

dist.mean(), dist.std()

dist.cdf(mu-sigma)

shortest = dist.cdf(177.8)
tallest = dist.cdf(185.44)
print(tallest - shortest)