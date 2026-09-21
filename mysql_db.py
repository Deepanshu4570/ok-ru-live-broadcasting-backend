import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Deepanshu@1",
    database="ok_ru_db"
)

cursor = conn.cursor()

def fetch_live_streams():
    cursor.execute("SELECT id, title, rtmp_url, stream_key, status FROM streams")
    rows = cursor.fetchall()
    streams = []
    for row in rows:
        streams.append({
            "id": row[0],
            "title": row[1],
            "rtmp_url": row[2],
            "stream_key": row[3],
            "status": row[4]
        })
    return streams

def save_stream_to_db(title, rtmp_url, stream_key):
    cursor.execute(
        "INSERT INTO streams (title, rtmp_url, stream_key, status) VALUES (%s, %s, %s, %s)",
        (title, rtmp_url, stream_key, "active")
    )
    conn.commit()