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