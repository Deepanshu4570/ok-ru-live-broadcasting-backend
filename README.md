# OK.ru Live Broadcasting Backend – Live Streaming Backend

## 📌 Project Overview

OK.ru Live Broadcasting Backend is a Python-based backend project for managing a live streaming platform. The project uses **Flask** to build REST APIs, **MySQL** to store and manage live stream information, **WebSocket** for real-time communication, and **FFmpeg** for video and audio stream processing.

The backend follows a structured **Route → Controller → Model → Database** architecture, making the application easier to maintain and extend.

## 🚀 Features

- Live stream management
- REST API development using Flask
- MySQL database integration
- Stream information storage and retrieval
- Route, Controller, and Model architecture
- JSON-based API responses
- WebSocket-based real-time communication
- Real-time viewer count and stream status updates
- FFmpeg-based video and audio processing
- RTMP stream processing foundation
- Modular backend project structure

## 🛠️ Technologies Used

- **Python** – Backend programming
- **Flask** – REST API development
- **MySQL** – Database management
- **XAMPP / Local MySQL server** environment
- **WebSocket / Flask-SocketIO** – Real-time communication
- **FFmpeg** – Video and audio processing
- **REST API** – Client-server communication
- **VS Code** – Development environment
- **Git & GitHub** – Version control

## 📂 Project Structure

```
ok_ru_backend/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── routes/
│   ├── __init__.py
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
```

## 🔄 Backend Architecture

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
```

### Live Streaming

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

### Real-Time Data

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
```

## 🔁 Request Flow

1. Client sends an API request.
2. Flask route receives the request.
3. Controller processes the request.
4. Model communicates with the database.
5. MySQL returns the required data.
6. Flask sends a JSON response to the client.

## 🎬 Live Streaming Flow

1. Streamer sends a live video using OBS or another streaming application.
2. The stream is received through an RTMP endpoint.
3. FFmpeg processes the video and audio stream.
4. The processed stream is prepared for delivery to viewers.
5. WebSocket handles real-time events such as viewer count, chat, and stream status.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ok_ru_backend
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install flask
pip install flask-socketio
pip install mysql-connector-python
```

## 🎥 FFmpeg Installation

FFmpeg is used for processing live video and audio streams. After installing FFmpeg, verify the installation:

```bash
ffmpeg -version
```

If FFmpeg is installed correctly, the terminal will display the FFmpeg version and configuration details.

### Example FFmpeg Command

```bash
ffmpeg -re -i input.mp4 -c:v libx264 -c:a aac -f flv rtmp://live.ok.ru/live/test
```

This command reads a video file, processes the video and audio, and sends the output to an RTMP streaming endpoint.

### Python FFmpeg Integration

```python
import subprocess

def broadcast_stream(input_file, rtmp_server_url, stream_key):
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

## 🔌 WebSocket

WebSocket provides a persistent connection between the client and server for real-time communication. In the OK.ru Live Broadcasting Backend, WebSocket can be used for:

- Live chat
- Real-time viewer count
- Stream status updates
- Notifications
- Live interaction events

### Flask-SocketIO Example

```python
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
```

The WebSocket connection allows the server to send updates to connected clients without requiring continuous HTTP requests.

## 🗄️ MySQL Setup

Start MySQL from XAMPP or your local server, then create the database:

```sql
CREATE DATABASE ok_ru_db;
USE ok_ru_db;

CREATE TABLE streams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    rtmp_url VARCHAR(255) NOT NULL,
    stream_key VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'active'
);
```

### 🔌 Database Configuration

Update `database/mysql_db.py` according to your MySQL configuration:

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="ok_ru_db"
)

cursor = conn.cursor()
```

## ▶️ Run the Application

Start MySQL and make sure FFmpeg is available in your system PATH, then start the Flask server:

```bash
python app.py
```

The application will run at: `http://127.0.0.1:5000`

## 🔗 API Endpoints

### Get All Streams

**Endpoint:** `GET /streams`

```
http://127.0.0.1:5000/streams
```

### Start Broadcast

**Endpoint:** `POST /streams/start`

**Example Payload:**

```json
{
    "title": "Frontend Live Test",
    "input_file": "sample.mp4",
    "rtmp_url": "rtmp://vsu.okcdn.ru/input",
    "stream_key": "your_stream_key"
}
```

## 📡 WebSocket Events

| Event | Purpose |
|---|---|
| `join_stream` | Join a live room and trigger viewer updates |
| `viewer_update` | Update live viewer count |
| `stream_started` | Notify clients when a stream starts |
| `stream_stopped` | Notify clients when a stream stops |
| `notification` | Send real-time notifications |

## 🧪 Testing

The API can be tested using:

- Web browser for GET requests & testing frontend interface (`http://127.0.0.1:5000`)
- Postman
- Thunder Client
- cURL

Example:

```bash
curl http://127.0.0.1:5000/streams
```

WebSocket functionality can be tested using a compatible WebSocket client or a frontend application connected to the Flask-SocketIO server.

## 🔮 Future Enhancements

- User registration and authentication
- JWT authentication
- Stream key generation
- RTMP server integration
- Start/stop stream APIs
- Live viewer management
- Real-time chat
- Stream analytics
- Multi-platform streaming (YouTube/Facebook/Twitch integration)
- Stream recording using FFmpeg
- Multiple video quality/transcoding support
- Admin dashboard
- Docker deployment
- Production WSGI server configuration

## 🎯 Project Objective

The main objective of this project is to develop a modular and scalable backend for a live broadcasting platform targeting OK.ru using Python, Flask, MySQL, WebSocket, and FFmpeg. The architecture provides a foundation for integrating live video streaming, stream management, real-time communication, authentication, analytics, multimedia processing, and other platform services.

## 👩‍💻 Author

**Deepanshu Kashyap**
Backend Development | AI/ML | Data Analytics

## 📄 License

This project is intended for learning, development, and demonstration purposes.