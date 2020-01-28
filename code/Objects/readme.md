## Objects

The objects folder contains all the objects for the rushhour project. 

### Board
The Board object will initiate a grid, which consists of a matrix, which consists of a list of lists. Upon this grid the algorithms will make calculations and “move” cars.
	The load_grid method initializes a board the size of which is specified within the infile and place a win location depending on the size.
	The set_winlocation method determines the coordinates the red car has to enter in order to win the game. The location is dependent on board size.
	The get_winloc method returns the win location, which is used in various objects.

### Car
The Car object is a representation of the cars on a game of Rushhour. It contains all information relevant to the cars, such as size, orientation, location and the type (is it a red car or not). All information is gathered from the csv file.
	The get_orientation method determines whether the car is vertically oriented or horizontally oriented. 
	The get_coords method determines the coordinates of a car in a Rushhour game.
	The make_coords method reads the coordinates of the cars from the csv file.
	the set_coords method takes the coordinates of the cars and places them accordingly on the grid. It does this when the game initializes and when a car is moved.


### Rushhour object
The Rushhour object holds all information which is relevant to the current game of Rushhour. It keeps track of the Board and the cars. 
	The load_cars method reads the cars from the csv file and arranges them in a dictionary, using the carname as a key and ascribing the carname and all other information as values. 
	The check_route method determines whether the current algorithm can actually perform the move it wants to do. It returns True when the move is possible and False when it is not. A move is possible when all constraints are satisfied. 
	The move method changes the location of a car object on the Board. 
	The choose_car method allows the algorithm to select a car available in the current game. 
	The check_win method checks whether the win condition (is the red car at the exit) is satisfied. 
	The print_game method prints the current state of the Rushhour game.
	The write_output method writes the moves that have been made into a csv file. 

### Route object
The Route object saves all the states which the current Rushhour game has entered in an archive. 
	The make_key method transforms the current state of a Rushhour game into a string, which can then be used to compare the state to later or earlier states.
	The add_move method adds the made move to a list, as well as which car it moved and how many steps it moved. 
	The save_state method calls upon the make_key method to save the current state in the archive, so it can later be referenced. 
	The get_state method checks whether or not a state exists within the archive. 

### Lookahead
The lookahead file contains two methods which allow an algorithm to create a limited depth-first search. 
	The get_next_state method returns the next state of a Rushhour game.
	The lookahead method creates children up to a pre-specified depth. 

