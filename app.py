from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'songs.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/add_song', methods=['POST'])
def add_user():
    data = request.get_json()
    title = data.get('title')
    url = data.get('url')

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO songs (title, url) VALUES (?, ?)', (title, url))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Song added successfully'}), 201

@app.route('/songs', methods=['GET'])
def get_users():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, url FROM songs')
    songs = cursor.fetchall()
    conn.close()

    return jsonify(songs)

@app.route('/', methods=['GET'])
def home():

    return jsonify(status_code="200",msg="ok")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
