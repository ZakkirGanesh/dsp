[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> 

The PMF of generating 1000 random numbers between 0 and 1 was made up of 1000 spikes at each number in the list, each spike reaching the same probability of 0.001 (1/1000), implying that each number had an equal probability of being generated randomly.

<img src="/statistics/random_pmf.png"/>

The CDF of that same set of 1000 random numbers was a generally straight line diagonally increasing, each possible number generated proportional to its percentile rank. For example, if the number generated was 0.61, then it would generally be in the 61th percentile, because it is a greater value than roughly 61% of the other numbers generated.

<img src="/statistics/random_cdf.png"/>

