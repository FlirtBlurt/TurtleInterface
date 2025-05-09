
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from flask import Flask, request, jsonify
from flask_cors import CORS

# Start ROS2 system
rclpy.init()


class ControlTheTurtle(Node):
    def __init__(self):
        super().__init__('control_the_turtle')

        # Create publisher to send messages
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def move(self, direction):
        msg = Twist()  # Create an empty message to control movement

        # Set values based on direction
        if direction == 'forward':
            msg.linear.x = 2.0  # Move forward
        elif direction == 'backward':
            msg.linear.x = -2.0  # Move backward
        elif direction == 'left':
            msg.angular.z = 1.8  # Turn left
        elif direction == 'right':
            msg.angular.z = -1.8  # Turn right
        else:
            return "Invalid direction"  # If the command is not recognized

        self.publisher_.publish(msg)  # Send the message to the simulated turtle
        return "Command sent"

# Create a class object
turtle_node = ControlTheTurtle()

# Create a Flask web app
app = Flask(__name__)
CORS(app)

# Create a route to accept commands to move the turtle
@app.route('/move_the_turtle', methods=['POST'])

def move_the_turtle():

    data = request.json  # Read the data sent from the user
    command = data.get('direction', '')  # Get the 'command' from the data

    # Ask the turtle to move in the given direction
    result = turtle_node.move(command)

    # Send back a message saying whether the command worked
    return jsonify({'result': result})

# This function starts the web server so it can accept commands
def main():
    app.run(host='0.0.0.0', port=5001)  # Start the Flask app on port 5001

# This ensures the server starts when the file is run
if __name__ == '__main__':
    main()
