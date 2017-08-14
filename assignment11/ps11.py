# Problem Set 11: Simulating robots
# Name:
# Collaborators:
# Time:

import math
import random
import ps11_visualize
import numpy as np

import matplotlib.pyplot as plt




# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = round(speed * math.cos(math.radians(angle)))
        delta_x = round(speed * math.sin(math.radians(angle)))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)


# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        # TODO: Your code goes here
        self.width = width
        self.height = height
        #map the tiles into an object with the keys as the x values and y values
        #the key is a tuble of the x and y
        #true is cleaned false is not cleaned
        self.tiles = {}
        for x in range (0, width):
            for y in range(0, height):
                key = (int(x),int(y))
                self.tiles[key] = False
            
        
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        # TODO: Your code goes here
        tileToClean = (int(pos.getX()),int(pos.getY()))
        self.tiles[tileToClean] = True
        
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # TODO: Your code goes here
        
        try:
            return self.tiles[(m,n)]
        except KeyError:
            return False
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here
        return int(len(self.tiles.keys()))
    
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here
        cleanedTiles = 0
        for tile in self.tiles.keys():
            if self.tiles[tile] == True:
                cleanedTiles = cleanedTiles + 1

        return int(cleanedTiles)
    
    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        # TODO: Your code goes here
        randomX = random.randrange(1,self.width + 1)
        randomY = random.randrange(1,self.height + 1)
        return Position(randomX, randomY)
    
    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        # TODO: Your code goes here
        try:
            self.tiles[(pos.getX(),pos.getY())]
            return True
        except KeyError:
            return False

class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        # TODO: Your code goes here
        self.speed = speed
        self.room = room
        self.d = random.randrange(0,361)
        self.p = self.room.getRandomPosition()
        
    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        # TODO: Your code goes here
        return self.p
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        # TODO: Your code goes here
        return self.d
    
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        # TODO: Your code goes here
        self.p = position
        
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        # TODO: Your code goes here
        self.d = direction


class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # TODO: Your code goes here
        #check if the tile I'm on hasn't been cleaned than mark it as clean
        if self.room.isTileCleaned(self.getRobotPosition().getX(),self.getRobotPosition().getY()) == False:
            #print 'tile was not clean'
            self.room.cleanTileAtPosition(self.getRobotPosition())
        #initiate condition to keep looping until we get a new good position
        doesItExist = False
        #initiate variable to check if the robot checked his whole surrounding
        checked_tiles = 0
        while doesItExist == False:
            checkPosition = self.getRobotPosition().getNewPosition(self.d, self.speed)        
            #check if the position exists
            if self.room.isPositionInRoom(checkPosition)== True:
                #check if it hasn't been cleaned before
                if self.room.isTileCleaned(checkPosition.getX(),checkPosition.getY()) == False:
                    #print checkPosition.getX(),checkPosition.getY()
                    #if it's dirty, move to it
                    self.setRobotPosition(checkPosition)
                    #mark it as clean
                    self.room.cleanTileAtPosition(self.getRobotPosition())
                    doesItExist = True
                else:
                    checked_tiles = checked_tiles + 1
                    #assuming the difference between the random angels is 30
                    #on average. We can assumen that within 12 movements
                    #the robot will cover the whole circle around him
                    #11 checks are enough otherwise he will go back in the same
                    #direction and he will be stuck 
                    if checked_tiles == 11:
                        self.setRobotDirection(random.randrange(0,361))
                        self.setRobotPosition(checkPosition)
                        #print checkPosition.getX(),checkPosition.getY()
                        checked_tiles = 0
                        doesItExist = True
            #change the angel if it doesn't qualify
            self.setRobotDirection(self.d + 30)
                     
        
# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    """

    #initiate results list
    endResults = []
    trialResults = []
    #initiate one room
    room = RectangularRoom(width, height)
    
    #initiate the num of robots and add them to a list
    robotsList = []
    for x in range(0, num_robots):
        robotsList.append(robot_type(room, speed))

    #initiate while loop for the num trials
    while num_trials > 0:
        #anim = ps11_visualize.RobotVisualization(num_robots, width, height, 0.4) 
    #Move the robots with the update and clean method in each trial
        while True:
            for robot in robotsList:
                robot.updatePositionAndClean()
            #anim.update(room, robotsList) 
            #Save the percentagle of clean tiles at the end of each trial in a list
            
            #print room.getNumCleanedTiles()
            cleanedPercentage = float(room.getNumCleanedTiles()) / float(room.getNumTiles())
            trialResults.append(cleanedPercentage)
            #print cleanedPercentage
            #check if it meets minimum coverage
            #if it does initiate new robots and add the results to the list
            if cleanedPercentage >= min_coverage:
                num_trials = num_trials - 1
                #anim.done() 
                endResults.append(trialResults)
                #print len(trialResults)
                trialResults = []
                room = RectangularRoom(width, height)
                robotsList = []
                for x in range(0, num_robots):
                    robotsList.append(robot_type(room, speed))
                break
    return endResults


# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means

""""
Hint: for plots 1-3, it may be useful to write a helper function that computes the average length
of all the lists in the list of lists returned by runSimulation. For plot 4, you may find the function
we have provided, computeMeans, to be helpful.
"""
def computeAverageOfLists(listOfLists):
    total = 0
    for trial in listOfLists:
        total = total + len(trial)
    return total / len(listOfLists)

    


# === Problem 4
def showPlot1(numberOfRobots, percentageToClean, roomSizeArray, robotType, show):
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    timeNeededArray = []
    roomSizeText = []
    plotX = []
    x = 0
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for room in roomSizeArray:
        avg = runSimulation(numberOfRobots,
                            1.0,
                            room['width'],
                            room['height'],
                            percentageToClean,
                            100,
                            robotType,
                            True)
        timeNeededArray.append(computeAverageOfLists(avg))
        roomSizeText.append(str(room['width']) + 'x' + str(room['height']))
        plotX.append(x)
        x = x + 1
    print timeNeededArray
    print roomSizeText
    plt.plot(plotX, timeNeededArray, marker='o')
    for point in plotX:
        ax.annotate(roomSizeText[point], xy=(point, timeNeededArray[point]), textcoords='data')
    plt.ylabel('Time needed to clean the room')
    plt.xlabel('Room size')
    plt.grid()
    if show == True:
        plt.show()

roomPlot1 = [{'width': 5, 'height': 5},
                 {'width': 10, 'height':10},
                 {'width': 15, 'height':15},
                 {'width': 20, 'height': 20},
                 {'width': 25, 'height': 25}
                 ]
#showPlot1(1, 0.75, roomPlot1, Robot, True)

    
def showPlot2(numberRobots, room, percentageToClean, robotType, show):
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    timeNeeded = []
    numberOfRobots = []
    for robot in range(1, numberRobots + 1):
        avg = runSimulation(robot, 1.0, room[0]['width'], room[0]['height'], percentageToClean, 100, robotType, True)
        timeNeeded.append(computeAverageOfLists(avg))
        numberOfRobots.append(robot)
    plt.plot(numberOfRobots, timeNeeded, marker='o')
    plt.ylabel('Time needed to clean the room')
    plt.xlabel('Robots count')
    plt.grid()
    if show == True:
        plt.show()
   
roomPlot2 = [{'width': 25, 'height': 25}]

#showPlot2(10,roomPlot2, 0.75, Robot, True)
        

def showPlot3(numberOfRobots, roomSizeArray, percentageToClean, robotType, show):
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    timeNeededArray = []
    roomSizeText = []
    plotX = []
    x = 0
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for room in roomSizeArray:
        avg = runSimulation(1, 1.0, room['width'], room['height'], percentageToClean, 100, robotType, True)
        timeNeededArray.append(computeAverageOfLists(avg))
        roomSizeText.append(str(room['width']) + 'x' + str(room['height']))
        plotX.append(room['width'] / room['height'])
        x = x + 1
    print timeNeededArray
    print roomSizeText
    plt.plot(plotX, timeNeededArray, marker='o')
    for point in range(0, len(plotX)):
        ax.annotate(roomSizeText[point], xy=(plotX[point], timeNeededArray[point]), textcoords='data')
    plt.ylabel('Time needed to clean the room')
    plt.xlabel('Room ratio')
    plt.grid()
    if show == True:
        plt.show()

roomsPlot3 = [{'width': 20, 'height': 20},
              {'width': 25, 'height':16},
              {'width': 40, 'height':10},
              {'width': 50, 'height': 8},
              {'width': 80, 'height': 5},
              {'width': 100, 'height': 4}
                 ]
#showPlot3(2, roomsPlot3, 0.75, Robot, True)

def showPlot4(numberOfRobots, room, percentageToClean, robotType, show):
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    # TODO: Your code goes here
    for robots in range (1, numberOfRobots + 1):
        timeNeededArray = []
        percentageCleanedArray = []
        for percentage in range(1, 101):
            avg = runSimulation(robots, 1.0, room['width'], room['height'], percentage / 100, 100, robotType, True)
            timeNeededArray.append(computeAverageOfLists(avg))
            percentageCleanedArray.append(percentage / 100)
            
        plt.plot(percentageCleanedArray, timeNeededArray, marker='o')
        
    plt.ylabel('Time needed to clean the room')
    plt.xlabel('Percentage Cleaned')
    plt.grid()
    if show == True:
        plt.show()

showPlot4(1, {'width': 25, 'height': 25}, 0.75, Robot, True)


# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    # TODO: Your code goes here
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # TODO: Your code goes here
        #check if the tile I'm on hasn't been cleaned than mark it as clean
        if self.room.isTileCleaned(self.getRobotPosition().getX(),self.getRobotPosition().getY()) == False:
            #print 'tile was not clean'
            self.room.cleanTileAtPosition(self.getRobotPosition())
        #initiate condition to keep looping until we get a new good position
        doesItExist = False
        checked_tiles = 0
        while doesItExist == False:
            checkPosition = self.getRobotPosition().getNewPosition(self.d, self.speed)        
            #check if the position exists
            if self.room.isPositionInRoom(checkPosition)== True:
                #check if it hasn't been cleaned before
                if self.room.isTileCleaned(checkPosition.getX(),checkPosition.getY()) == False:
                    #print checkPosition.getX(),checkPosition.getY()
                    #if it's dirty, move to it
                    self.setRobotPosition(checkPosition)
                    #mark it as clean
                    self.room.cleanTileAtPosition(self.getRobotPosition())
                    doesItExist = True
                else:
                    checked_tiles = checked_tiles + 1
                    #assuming the difference between the random angels is 30
                    #on average. We can assumen that within 12 movements
                    #the robot will cover the whole circle around him
                    #11 checks are enough otherwise he will go back in the same
                    #direction and he will be stuck 
                    if checked_tiles == 11:
                        self.setRobotDirection(random.randrange(0,361))
                        self.setRobotPosition(checkPosition)
                        #print checkPosition.getX(),checkPosition.getY()
                        checked_tiles = 0
                        doesItExist = True
            #change the angel if it doesn't qualify
            self.setRobotDirection(random.randrange(0,361))

#avg = runSimulation(1, 1.0, 10, 15, 0.75 , 100, RandomWalkRobot, True)
##
##total = 0
##for trial in avg:
##    total = total + len(trial)
##print total / len(avg)
## 


# === Problem 6

def showPlot5(method, robotTypesArray,numberOfRobots, room, percentageToClean):
    """
    Produces a plot comparing the two robot strategies.
    """
    for robot in robotTypesArray:
        method(numberOfRobots, room, percentageToClean, robot, False)
    plt.show()
showPlot5(showPlot1, [RandomWalkRobot,Robot],1 , 1.0, roomPlot1)
        
