# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 16:30:18 2016

@author: azg
"""

import chap01soln
import thinkstats2
import thinkplot

resp = chap01soln.ReadFemResp()
resp_pmf = thinkstats2.Pmf(resp.numkdhh)
thinkplot.Pmf(resp_pmf, label="Number of Kids PMF")
thinkplot.show()
def BiasPmf(pmf, label=""):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf
biased_resp_pmf = BiasPmf(resp_pmf, label="Number of Kids Biased PMF")
thinkplot.Pmf(biased_resp_pmf)
thinkplot.show()
resp_pmf_mean = resp_pmf.Mean()
print(resp_pmf_mean)
biased_resp_pmf_mean = biased_resp_pmf.Mean()
print(biased_resp_pmf_mean)