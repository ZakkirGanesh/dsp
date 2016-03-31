"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

df = nsfg.ReadFemPreg()
first_births = df[df.birthord == 1]
next_births = df[df.birthord > 1]
first_weights = first_births.totalwgt_lb
next_weights = next_births.totalwgt_lb

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    print(thinkstats2.CohenEffectSize(first_weights, next_weights))
    print('%s: All tests passed.' % script)

if __name__ == '__main__':
    main(*sys.argv)
