import os
from flask import Flask, request, jsonify, send_from_directory
import sqlite3
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / 'frontend'
DIST_DIR = FRONTEND_DIR / 'dist'
DB_PATH = BASE_DIR / 'messages.db'

app = Flask(__name__, static_folder=str(DIST_DIR), static_url_path='')


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with get_db_connection() as conn:
        conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            '''
        )
        conn.commit()


@app.route('/')
def index():
    if DIST_DIR.exists():
        return send_from_directory(str(DIST_DIR), 'index.html')
    return send_from_directory(str(BASE_DIR), 'index.html')


@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json(force=True) or {}
    name = (data.get('name') or '').strip()
    email = (data.get('email') or '').strip()
    message = (data.get('message') or '').strip()

    if not name or not email or not message:
        return jsonify({'error': 'Name, email, and message are required.'}), 400

    created_at = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')

    with get_db_connection() as conn:
        conn.execute(
            'INSERT INTO messages (name, email, message, created_at) VALUES (?, ?, ?, ?)',
            (name, email, message, created_at)
        )
        conn.commit()

    return jsonify({'status': 'success', 'message': 'Saved to backend database.'}), 201


@app.route('/api/messages', methods=['GET'])
def get_messages():
    with get_db_connection() as conn:
        rows = conn.execute('SELECT id, name, email, message, created_at FROM messages ORDER BY id DESC').fetchall()
        messages = [dict(row) for row in rows]
    return jsonify({'messages': messages})


@app.route('/api/messages/clear', methods=['POST'])
def clear_messages():
    with get_db_connection() as conn:
        conn.execute('DELETE FROM messages')
        conn.commit()
    return jsonify({'status': 'cleared'})


@app.route('/<path:filename>')
def serve_file(filename):
    if DIST_DIR.exists():
        candidate = DIST_DIR / filename
        if candidate.exists():
            return send_from_directory(str(DIST_DIR), filename)
        return send_from_directory(str(DIST_DIR), 'index.html')
    return send_from_directory(str(BASE_DIR), filename)


if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
