from database.mysql_db import fetch_live_streams, save_stream_to_db

def get_streams_model():
    return fetch_live_streams()

def add_stream_model(title, rtmp_url, stream_key):
    save_stream_to_db(title, rtmp_url, stream_key)