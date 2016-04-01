[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> 
The actual PMF distribution of the variable "numkdhh" was:

[<img src="statistics/resp_pmf.png" title="resp pmf"/>]

The mean of the actual PMF was 1.024.

The observed PMF distribution was:

[<img src="statistics/biased_resp_pmf.png" title="biased resp pmf"/>]

The mean of the observed PMF was 2.404.

The probabilities in the observed PMF were higher than the actual PMF as the number of kids became greater, since the probability that a child is one of a larger number of siblings naturally increases as the number of kids in the family does. This also explains why a biased PMF will report a mean of 2.4 compared to 1.0.

I answered this question by simply building upon the existing code in "chap03ex.ipynb", and utilizing the BiasedPmf function defined in Chapter 3 of "Think Stats," as well as the chapter's listed code for creating step functions out of PMFs.
