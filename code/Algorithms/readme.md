## Algorithms
This folder contains all the files for the algorithms. The algorithms we use are:
* random
* random with use of an archive (Smart Cabby algorithm)
* breadthfirst
* breadthfirst with priority queue and look ahead
* A* reverse with look ahead

### Random algorithm
The random algorithm randomly chooses a car on the given board. It then randomly chooses a direction, for vertical cars up and down, for the horizontal cars left and right. After that it calculates the maximum amount of steps the car can move, and randomly chooses a step between 1 and the maximal amount of steps. The algorithm continues these steps until the red car gets to the exit. 

### Smart Cabby algorithm
The smart cabby algorithm is an alternative to the random algorithm using an archive. It uses the same logic of the random algorithm with the added functionality of an archive. The archive contains all the states the algorithm already visited. The algortihm does not make moves that result in a state that is already in the archive. 

### Breadthfirst
The breadthfirst algorithm explores all the the connected states layerwise starting at the begin state. The connected states are all possible different states by moving one car. The algorithm first moves horizontally and visits all the states at the current layer, and then moves to the next layer by moving an extra car.

### Breadthfirst with priority queue and look ahead
The breadthfirst with priority queue is an alternative to the regular breadthfirst algorithm. This algorithm uses a priority queue which consists of child states, each with it's own f value. The child states are created N states deep. The f value is calculated with the number of moves used and the amount of cars in the way of the red car. By adding these two values up the calc_f_value function calculates the f value. Each child state has it's own f value and the algorithm chooses the child with the lowest value of f. 

### A* reverse with look ahead
The A* reverse algorithm starts using the random algorithm to find the final state. When the final state is found A* starts at working in the begin- and final state. After this it starts to make moves in both states toward each other so that they meet in the middle. In doing so it uses the look ahead method in both the states. The f value is calculated based on the amount of cars that have overlapping positions with each other in both states. The algorithm also stops searching when the red car has a free path to the exit. The A* uses the x_checker method to check wether the red car has a way to get to the exit. If it does it moves it towards the exit.
