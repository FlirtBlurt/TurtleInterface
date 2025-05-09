# Turtle Controller Flask App

This is a simple Python Flask app that serves a webpage to control the TurtleSim robot using ROS 2.


## Folder Structure

turtle_flask_webapp/
├── move_the_turtle.py
├── json_unwrapper.py
├── README.md


## Requirements
- Ubuntu (i used via WSL)
- Python 3.13 (any python 3.0+ version will do)
- Flask, flask-cors, requests
- ROS 2 Jazzy
- rclpy, turtlesim package, geometry_msgs


## Instructions for Setup

1. Clone the project files.
2. Navigate to project folder (turtle_flask_webapp).
3. Create a virtual environment.
4. Install the required packages.


## How to Run

1. Start the TurtleSim node in one terminal:

	source /opt/ros/jazzy/setup.bash
	ros2 run turtlesim turtlesim_node
 
2. In another terminal, start the ROS movement server:

	python3 move_the_turtle.py

3. In the third terminal, launch the web interface:
	
	python3 json_unwrapper.py

3. Open your browser and visit:
	
	http://127.0.0.1:5000

Click the buttons to move the turtle.

## Notes
Make sure you are running this inside a ROS 2 sourced environment.
