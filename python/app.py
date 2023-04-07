from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('temperature.db')
    conn.execute('CREATE TABLE IF NOT EXISTS temperature (timestamp TEXT, value INTEGER)')
    conn.execute('CREATE TABLE IF NOT EXISTS message (id INTEGER PRIMARY KEY, body TEXT)')
    conn.execute("INSERT INTO message (body) VALUES ('Hello World')")
    conn.close()

@app.route('/api/temperature', methods=['GET'])
def get_temperature_data():
    conn = sqlite3.connect('temperature.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM temperature")
    rows = cursor.fetchall()
    conn.close()
    return jsonify({"temperature_readings": rows})

@app.route('/api/temperature', methods=['POST'])
def save_temperature():
    temperature = request.form['temperature']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect('temperature.db')
    conn.execute("INSERT INTO temperature (timestamp, value) VALUES (?, ?)", (timestamp, temperature))
    conn.commit()
    conn.close()
    return "Temperature saved", 200

@app.route('/api/message', methods=['GET'])
def get_message_from_db():
    conn = sqlite3.connect('temperature.db')
    cursor = conn.cursor()
    cursor.execute("SELECT body FROM message WHERE id = 1")
    result = cursor.fetchone()
    conn.close()
    if result is not None:
        message_body = result[0]
        return jsonify({"message": message_body})
    else:
        return jsonify({"message": "No message found"})

@app.route('/api/message', methods=['POST'])
def set_message():
    message_body = request.form['body']
    conn = sqlite3.connect('temperature.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM message")
    count = cursor.fetchone()[0]
    if count == 0:
        conn.execute("INSERT INTO message (body) VALUES (?)", (message_body,))
    else:
        conn.execute("UPDATE message SET body = ? WHERE id = 1", (message_body,))
    conn.commit()
    conn.close()
    return "Message updated", 200

@app.route('/delete_all', methods=['POST'])
def delete_all():
    conn = sqlite3.connect('temperature.db')
    conn.execute("DELETE FROM temperature")
    conn.commit()
    conn.close()
    return "All records deleted", 200

@app.route('/', methods=['GET'])
def get_temperature_list():
    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0')