from models.live_model import get_streams_model, add_stream_model
from streaming.rtmp_processor import broadcast_stream

def handle_get_streams():
    streams = get_streams_model()
    return {
        "status": "success",
        "data": streams
    }

def handle_start_broadcast(title, input_file, rtmp_url, stream_key):
    if not rtmp_url or not stream_key:
        return {
            "status": "error",
            "message": "RTMP URL and Stream Key are required"
        }, 400
        
    add_stream_model(title, rtmp_url, stream_key)
    process = broadcast_stream(input_file, rtmp_url, stream_key)
    
    return {
        "status": "success",
        "message": "Live broadcast started successfully",
        "destination": f"{rtmp_url}/{stream_key}"
    }