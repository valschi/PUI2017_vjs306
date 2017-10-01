This is my ReadMe for HW3

__Assignment 1.__

Matt and I started working on it on Saturday after bootcamp.   Mainly the effort consisted of understanding the assignment and analyzing Federica's code.

I downloaded the sample code and structure and ran it while in parallel created a new notebook for the Assignment. 

With Matt we discussed the Central Limit theorem and how as the sample gets bigger the mean of the sample gets closer to the mean of the population. We also used wikipedia to understand what the PDF's where for each of the distributions. 

Since we were going to be using random samples we set a seed and agreed to the same value to verify the codes were working as expected. For the Normal distribution we just set the Standard deviation to a fix value so it was easier to see. 

_Next_ I used the '?' for each of the distributions to understand what are the input values that each of the distributions was expecting, and Wikipedia also served to confirm the same.   In the chi square example provided it is mentioned that the degrees of freedom is the same as the mean ... _luckily_, when trying to find the 5th distribution this made sense.

During Saturday we were not able to find a 5th distribution, but on Sunday Matt found that Gumbel distribution uses basic math. I wanted to calculate the euler constant using a particular formula or python function, but in the essence of time we just copied the value. 

For the histogram of all of the 500 samples (100 per distribution) we can see most of the samples concentrate (in a Gaussian way) to the mean of the population. Which is what we wanted to prove all along according to the Central Limit Theorem.
