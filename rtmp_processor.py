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