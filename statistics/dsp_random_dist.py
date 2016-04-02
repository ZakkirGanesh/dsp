# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 22:08:35 2016

@author: azg
"""

import random
import thinkstats2
import thinkplot

random_list = [random.random() for _ in range(1000)]
random_list_pmf = thinkstats2.Pmf(random_list)
thinkplot.Pmf(random_list_pmf, linewidth=0.08, label="Random List PMF")
thinkplot.show()
random_list_cdf = thinkstats2.Cdf(random_list)
thinkplot.Cdf(random_list_cdf, label="Random List CDF")
thinkplot.show()
