from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')  # Main landing page

@app.route('/about')
def about():
    return render_template('sign.html')  # Login page

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@socketio.on('hand_gesture')
def handle_hand_gesture(data):
    print(f"Received hand gesture: {data}")
    # Additional actions based on hand gestures

@socketio.on('face_gesture')
def handle_face_gesture(data):
    print(f"Received face gesture: {data}")
    # Additional actions based on face gestures

if __name__ == '__main__':
    socketio.run(app, debug=True)
