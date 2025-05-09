from flask import Flask, request, jsonify

# Import movement function
from move_the_turtle import move_the_turtle

unwrapper = Flask(__name__)

# Serve the HTML page at the root URL
@unwrapper.route('/')

def index():
    return '''
    <html>
    <head>
        <title>Turtle Controller</title>
        <script>
            function sendCommand(direction) {
                fetch('http://127.0.0.1:5001/move_the_turtle', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ direction: direction })
                })
                .then(response => response.json())
                .then(data => {
                    alert("Turtle moved: " + data.result);
                })
                .catch(error => {
                    alert("Error: " + error);
                });
            }
        </script>
    </head>
    <body>
        <h2>Move the Turtle</h2>
        <button onclick="sendCommand('forward')">Forward</button>
        <button onclick="sendCommand('backward')">Backward</button>
        <button onclick="sendCommand('left')">Left</button>
        <button onclick="sendCommand('right')">Right</button>
    </body>
    </html>
    '''

if __name__ == '__main__':
    unwrapper.run(debug=True, port=5000)
