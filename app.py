from flask import Flask, render_template
from flask_socketio import SocketIO
from routes.live_routes import live_bp
from websocket.socket_handler import init_socket_events

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

app.register_blueprint(live_bp)
init_socket_events(socketio)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, debug=True)