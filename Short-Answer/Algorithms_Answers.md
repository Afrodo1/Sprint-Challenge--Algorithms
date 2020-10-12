#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)The runtime complexity of this particular bit of psuedocode seems to be Exponential(O(c^n)). This can be seen with each increase of n the value of a becomes exponentially greater with each passthru.


b)The runtime complexity of this piece of pseudocode seems to align more with Constant(O(1) mainly due to the fact that as the value of n gets larger the value of J seems to remain fairly consistant. However there is also it Linear tendency due to the fact that the value of sum increases consitantly by a value of 1 for each iteration of j as it passes thru the range defined by n.


c)The runtime complexity of this piece of psuedocode seems to be linear. for every input of bunnies the return value is consistantly double the number of bunnies inputed.

## Exercise II

In order to accomplish the goal of dropping as few eggs as possible and minimizing the number of said dropped eggs that break, the best route to take in my opionion would be an algorithm that makes use of logarithmic runtime complexity. I would make use of a binary search starting from the middle floor and working my way up or down depending on whether or not the eggs broke. repeating the search by checking the "middle floor" between two endpoints, the "top floor" and "bottom floor" until i found the floor where eggs begin breaking when dropped.




