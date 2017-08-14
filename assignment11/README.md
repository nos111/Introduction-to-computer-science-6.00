This is the code of a robot that clean a room. The robot will take the measures of the room. Walk over it and clean every tile that he passes on. He will keep track of the tiles he was on and that has been cleaned in order to minimize repeated movements. 

The robot follow this cleaning strategy:
1- Check if the tile in front of you is clean
2- if clean move your direction by 30 degrees
3- repeat number 2 until you find a dirty tile
4- if no dirty tiles are found and the whole surrounding is checked: move to a random tile
5- repeat the earlier steps
6- if the robot hits a wall, he will change the direction by 30 degrees until he finds a tile.

I have tried different angels and from the results I got, 30 degrees gave the best results and the fastest cleaning.

The function ‘updatePositionAndClean’ in the robot class controls the movement strategy of the robot.

In each function is a short explanations of what the functions is expected to do.
Each step is also explained in the inline comments.

If you uncomment the ‘anim’ in the ‘runSimulation’ you will be able to see the robot moving in the room:

Photo of robot movement
<img src='https://github.com/nos111/MIT-OCW/blob/master/Introduction%20to%20Computer%20Science%20(fall%202008)/assignment11/images/RobotMovementSimulation.jpg?raw=true'>


Functions to provide analytical data are provided:
-“showPlot1”  Produces a plot showing dependence of cleaning time on room size.
<img src='https://github.com/nos111/MIT-OCW/blob/master/Introduction%20to%20Computer%20Science%20(fall%202008)/assignment11/images/GraphTimeXRoomSize.jpg?raw=true'>

- “showPlot2’ Produces a plot showing dependence of cleaning time on number of robots.
<img src='https://github.com/nos111/MIT-OCW/blob/master/Introduction%20to%20Computer%20Science%20(fall%202008)/assignment11/images/GraphTimeVSRobotsNumber.jpg?raw=true'>


- “showPlot3” Produces a plot showing dependence of cleaning time on room shape.
<img src="https://github.com/nos111/MIT-OCW/blob/master/Introduction%20to%20Computer%20Science%20(fall%202008)/assignment11/images/GraphTimeVSRoomSizeRatio.jpg?raw=true">

- “showPlot4” Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
<img src="https://github.com/nos111/MIT-OCW/blob/master/Introduction%20to%20Computer%20Science%20(fall%202008)/assignment11/images/GraphTimeVSPercentageCleaned.png?raw=true">

- "showPlot5" Produces a plot comparing the two robot strategies.
