#  Algorithms
This folder contains all the files for the algorithms. The algorithms are random, 
random with use of an archive (Smart Caby algorithm), breadfirst, breadfirst with a priority queue. 

### Random algorithm
The random algorithm randomily chooses a car of the given board. It then randomily chooses a direction, for vertical cars up and down, for the horizontal cars left and right. After that it calculates the maximal amount of steps the car can move, and randomily chooses a step between 1 and the maximal amount of steps. The algorithm continues these steps until the red car is in the exit. 


### Smart Caby algorithm
The smart caby algorithm is an alternative of the random algorithm using an archive. The archive contains all the states the algorithm already visited. The algortihm skips moves that result in the same state that are already in the archive.

### Breadthfirst

The breadthfirst algorithm explores all the the connected states layerwise starting at the begin state. The connected states are all possible different states by moving one car. The algroithm first moves horizontally and visits all the states at the current layer, and then moves to the next layer by moving an extra car.

### Breadthfirst with priority queue
The breadthfirst algorithm with priority queue is an alternative of the breadthfirst. The breadthfirst algorithm with priority queue makes use of a priority queue. The priority queue is an queue orded with states based on a selected value. The state with the "best" value is chosen first. 