# OK.ru Live Broadcasting Backend – Live Streaming Backend

📌 Project Overview

OK.ru Live Broadcasting Backend is a Python-based backend project for managing a live streaming platform. The project uses Flask to build REST APIs, MySQL to store and manage live stream information, WebSocket for real-time communication, and FFmpeg for video and audio stream processing.
The backend follows a structured Route → Controller → Model → Database architecture, making the application easier to maintain and extend.

🚀 Features

Live stream management
REST API development using Flask
MySQL database integration
Stream information storage and retrieval
Route, Controller, and Model architecture
JSON-based API responses
WebSocket-based real-time communication
Real-time viewer count and stream status updates
FFmpeg-based video and audio processing
RTMP stream processing foundation
Modular backend project structure

🛠️ Technologies Used

Python – Backend programming
Flask – REST API development
MySQL – Database management
XAMPP / Local MySQL server environment
WebSocket / Flask-SocketIO – Real-time communication
FFmpeg – Video and audio processing
REST API – Client-server communication
VS Code – Development environment
Git & GitHub – Version control

📂 Project Structure

ok_ru_backend/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── routes/
│   ├── **init**.py
│   └── live_routes.py
│
├── controllers/
│   └── live_controller.py
│
├── models/
│   └── live_model.py
│
├── database/
│   └── mysql_db.py
│
├── streaming/
│   └── rtmp_processor.py
│
├── websocket/
│   └── socket_handler.py
│
└── README.md

🔄 Backend Architecture

```
                     Client
                       │
                       ▼
                Flask REST API
                       │
                       ▼
                     Routes
                       │
                       ▼
                  Controllers
                       │
                       ▼
                     Models
                       │
                       ▼
                MySQL Database


                LIVE STREAMING

```

Streamer / OBS
│
│ RTMP
▼
Streaming Server
│
▼
FFmpeg
│
├── Video Processing
├── Audio Processing
└── Stream Conversion
│
▼
Live Stream
│
▼
Viewers

```
                REAL-TIME DATA

```

Viewer / Streamer
│
▼
WebSocket
│
├── Live Chat
├── Viewer Count
├── Stream Status
└── Notifications

Request Flow

Client sends an API request.
Flask route receives the request.
Controller processes the request.
Model communicates with the database.
MySQL returns the required data.
Flask sends a JSON response to the client.
Live Streaming Flow

Streamer sends a live video using OBS or another streaming application.
The stream is received through an RTMP endpoint.
FFmpeg processes the video and audio stream.
The processed stream is prepared for delivery to viewers.
WebSocket handles real-time events such as viewer count, chat, and stream status.

⚙️ Installation

1. Clone the Repository

git clone cd ok_ru_backend

2. Create a Virtual Environment

python -m venv venv

Activate it on Windows:
venv\Scripts\activate

3. Install Dependencies

pip install flask
pip install flask-socketio
pip install mysql-connector-python

🎥 FFmpeg Installation

FFmpeg is used for processing live video and audio streams.
After installing FFmpeg, verify the installation:
ffmpeg -version

If FFmpeg is installed correctly, the terminal will display the FFmpeg version and configuration details.
Example FFmpeg Command

ffmpeg -re -i input.mp4 -c:v libx264 -c:a aac -f flv rtmp://live.ok.ru/live/test

This command reads a video file, processes the video and audio, and sends the output to an RTMP streaming endpoint.
Python FFmpeg Integration

import subprocessdef broadcast_stream(input_file, rtmp_server_url, stream_key):

```
full_rtmp_url = f"{rtmp_server_url}/{stream_key}"

command = [
    "ffmpeg",
    "-re",
    "-i", input_file,
    "-c:v", "libx264",
    "-c:a", "aac",
    "-f", "flv",
    full_rtmp_url
]

process = subprocess.Popen(command)
return process

```

🔌 WebSocket

WebSocket provides a persistent connection between the client and server for real-time communication.
In the OK.ru Live Broadcasting Backend, WebSocket can be used for:
Live chat
Real-time viewer count
Stream status updates
Notifications
Live interaction events
Flask-SocketIO Example

active_viewers = 0

def init_socket_events(socketio):
@socketio.on("join_stream")
def handle_join(data):
global active_viewers
active_viewers += 1
socketio.emit(
"viewer_update",
{"viewers": active_viewers}
)

The WebSocket connection allows the server to send updates to connected clients without requiring continuous HTTP requests.

🗄️ MySQL Setup

Start MySQL from XAMPP or your local server.
Open your database client and create the database:
CREATE DATABASE ok_ru_db;

Select the database:
USE ok_ru_db;

Create the streams table:
CREATE TABLE streams (
id INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(255) NOT NULL,
rtmp_url VARCHAR(255) NOT NULL,
stream_key VARCHAR(255) NOT NULL,
status VARCHAR(50) DEFAULT 'active'
);

🔌 Database Configuration

Update database/mysql_db.py according to your MySQL configuration:
import mysql.connector

conn = mysql.connector.connect(
host="localhost",
user="root",
password="your_password",
database="ok_ru_db"
)

cursor = conn.cursor()

▶️ Run the Application

Start MySQL and make sure FFmpeg is available in your system PATH.
Start the Flask server:
python app.py

The application will run at:
[http://127.0.0.1:5000](http://127.0.0.1:5000?utm_source=gemini)

🔗 API Endpoints

Get All Streams

Endpoint:
GET /streams

Example:
[http://127.0.0.1:5000/streams](http://127.0.0.1:5000/streams?utm_source=gemini)

Start Broadcast

Endpoint:
POST /streams/start

Example Payload:
{
"title": "Frontend Live Test",
"input_file": "sample.mp4",
"rtmp_url": "rtmp://vsu.okcdn.ru/input",
"stream_key": "your_stream_key"
}

📡 WebSocket Events

Example WebSocket events that can be implemented:
EventPurposejoin_streamJoin a live room and trigger viewer updatesviewer_updateUpdate live viewer countstream_startedNotify clients when a stream startsstream_stoppedNotify clients when a stream stopsnotificationSend real-time notifications

🧪 Testing

The API can be tested using:
Web browser for GET requests & testing frontend interface (`[http://127.0.0.1:5000](http://127.0.0.1:5000)`)
Postman
Thunder Client
cURL
Example:
curl [http://127.0.0.1:5000/streams](http://127.0.0.1:5000/streams?utm_source=gemini)

WebSocket functionality can be tested using a compatible WebSocket client or a frontend application connected to the Flask-SocketIO server.

🔮 Future Enhancements

User registration and authentication
JWT authentication
Stream key generation
RTMP server integration
Start/stop stream APIs
Live viewer management
Real-time chat
Stream analytics
Multi-platform streaming
YouTube/Facebook/Twitch integration
Stream recording using FFmpeg
Multiple video quality/transcoding support
Admin dashboard
Docker deployment
Production WSGI server configuration

🎯 Project Objective

The main objective of this project is to develop a modular and scalable backend for a live broadcasting platform targeting OK.ru using Python, Flask, MySQL, WebSocket, and FFmpeg.
The architecture provides a foundation for integrating live video streaming, stream management, real-time communication, authentication, analytics, multimedia processing, and other platform services.

👩‍💻 Author
Deepanshu Kashyap
Backend Development | AI/ML | Data Analytics

📄 License
This project is intended for learning, development, and demonstration purposes.