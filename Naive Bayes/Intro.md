To calculate the probability that an event will occur, given that another event has already occurred, we use Bayes’s Theorem. To calculate the probability of hypothesis(h) being true, given our prior knowledge(d),
we use Bayes’s Theorem as follows:

P(h|d)= (P(d|h) P(h)) / P(d)
where:

P(h|d) = Posterior probability. The probability of hypothesis h being true, given the data d, where P(h|d)= P(d1| h) P(d2| h)….P(dn| h) P(d)
P(d|h) = Likelihood. The probability of data d given that the hypothesis h was true.
P(h) = Class prior probability. The probability of hypothesis h being true (irrespective of the data)
P(d) = Predictor prior probability. Probability of the data (irrespective of the hypothesis)
This algorithm is called ‘naive’ because it assumes that all the variables are independent of each other, which is a naive assumption to make in real-world examples.
