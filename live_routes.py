from flask import Blueprint, jsonify, request
from controllers.live_controller import handle_get_streams, handle_start_broadcast

live_bp = Blueprint('live', __name__)

@live_bp.route("/streams", methods=["GET"])
def get_streams():
    data = handle_get_streams()
    return jsonify(data)

@live_bp.route("/streams/start", methods=["POST"])
def start_broadcast_endpoint():
    data = request.json
    title = data.get("title", "Untitled Live Stream")
    input_file = data.get("input_file")
    rtmp_url = data.get("rtmp_url")
    stream_key = data.get("stream_key")
    
    response = handle_start_broadcast(title, input_file, rtmp_url, stream_key)
    return jsonify(response)