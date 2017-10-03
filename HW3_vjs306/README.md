This is my ReadMe for HW3

__Assignment 1.__

Matt and I started working on it on Saturday after bootcamp.   Mainly the effort consisted of understanding the assignment and analyzing Federica's code.

I downloaded the sample code and structure and ran it while in parallel created a new notebook for the Assignment. 

With Matt we discussed the Central Limit theorem and how as the sample gets bigger the mean of the sample gets closer to the mean of the population. We also used wikipedia to understand what the PDF's where for each of the distributions. 

Since we were going to be using random samples we set a seed and agreed to the same value to verify the codes were working as expected. For the Normal distribution we just set the Standard deviation to a fix value so it was easier to see. 

_Next_ I used the '?' for each of the distributions to understand what are the input values that each of the distributions was expecting, and Wikipedia also served to confirm the same.   In the chi square example provided it is mentioned that the degrees of freedom is the same as the mean ... _luckily_, when trying to find the 5th distribution this made sense.

During Saturday we were not able to find a 5th distribution, but on Sunday Matt found that Gumbel distribution uses basic math. I wanted to calculate the euler constant using a particular formula or python function, but in the essence of time we just copied the value. 

For the histogram of all of the 500 samples (100 per distribution) we can see most of the samples concentrate (in a Gaussian way) to the mean of the population. Which is what we wanted to prove all along according to the Central Limit Theorem.

__Assignment 2.__

For Assignment 2 I started with the download of the data on Sunday, given the difficulties with navigation straight on Data Facility, I downloaded the files directly from citibike. Important highlight is that I discovered not all files there are the same, some are .zip, some .csv.zip. The code as I currently have it works only for .zip files, if I wanted to be able to extract regardless I would have to implement like Federica does, but in the essence of time it will only work on .zip files. 

We agreed on the Hypothesis and Null Hypothesis to be around the Idea of womer riders are in average younger than male riders. 

On Monday we met with Matt and Kent to work on Assignment 2. Displaying the tables and the columns I wanted was easy as it was the same as last week, but I had trouble keeping up and fully understanding how to extract the data. Specifically: 

fem_count = (cBdata['age'][cBdata['gender'] == 2].groupby(cBdata['age']).count())/gen_count[2]

male_count = (cBdata['age'][cBdata['gender'] == 1].groupby(cBdata['age']).count())/gen_count[1]

it is the same logic used later to get the average.  This was not easy for me to understand from what Matt and Kent were doing.  I understand the purpose of it, by looking at the outcome it is displaying the normalized number of riders per age. 

And then we are displaying the average age of Male and Females, which is up to the point of this week's homework.

__Assignment 3.__



discovering that the format
