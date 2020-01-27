## Algorithms
This folder contains all the files for the algorithms. The algorithms we use are:
* random
* random with use of an archive (Smart Caby algorithm)
* breadthfirst
* breadthfirst with priority queue and look ahead
* A star reverse with look ahead

### Random algorithm
The random algorithm randomily chooses a car of the given board. It then randomily chooses a direction, for vertical cars up and down, for the horizontal cars left and right. After that it calculates the maximal amount of steps the car can move, and randomily chooses a step between 1 and the maximal amount of steps. The algorithm continues these steps until the red car is in the exit. 

### Smart Caby algorithm
The smart caby algorithm is an alternative of the random algorithm using an archive. The archive contains all the states the algorithm already visited. The algortihm skips moves that result in the same state that are already in the archive.

### Breadthfirst
The breadthfirst algorithm explores all the the connected states layerwise starting at the begin state. The connected states are all possible different states by moving one car. The algroithm first moves horizontally and visits all the states at the current layer, and then moves to the next layer by moving an extra car.

### Breadthfirst with priority queue and look ahead
The breadthfirst algorithm with priority queue is an alternative of the breadthfirst. The breadthfirst algorithm with priority queue makes use of a priority queue. The priority queue is an queue orded with states based on a selected value. These values are calculated on an amount of moves given in the look ahead method. The total value is compared and the state with the best f-value is choosen. 

### A star reverse with look ahead
The A star reverse algorithm starts using the random algorithm to find the final state. When the final state is found a star starts both at the begin state and at the final state. After this it starts to make moves in both states toward each other so that they meet in the middle. In doing so it used the look ahead method in both the beginning and end states. The f value is calculated based on the amount of cars that have overlapping positions with each other in both the beginning and end state. The algorithm also stops searching when the red car has a free path to the exit. The A star uses the x_checker to check wether the red car has a way to get to the exit.
