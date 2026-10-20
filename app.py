import os
import sqlite3
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
DB_PATH = os.environ.get('NOTES_DB', '/tmp/notes.db')

def connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT NOT NULL)')
    conn.commit()
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = connection()
    if request.method == 'POST':
        content = request.form.get('content', '').strip()
        if content:
            conn.execute('INSERT INTO notes(content) VALUES (?)', (content,))
            conn.commit()
        conn.close()
        return redirect(url_for('index'))
    notes = conn.execute('SELECT id, content FROM notes ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', notes=notes)

@app.post('/delete/<int:note_id>')
def delete(note_id):
    conn = connection()
    conn.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', '5000')))
