from flask import (
    Flask, flash, jsonify, render_template, request, url_for, redirect)
import sqlite3


# application settions and database name
app = Flask(__name__)
app.debug = True
app.secret_key = 'DH23%$ERTH:<LKH%$^7oiPJHv@#swreBF^IOUjmok;POP'
DATABASE = 'to_do_app.sqlite3'


# home page
@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html', title='TO-DO-APP')


# history
@app.route('/history')
def history():
    return render_template('history.html', title='History')


# insert item
@app.route('/add', methods=['GET', 'POST'])
def add_task():

    status = 0
    payload = ''

    if request.method == 'POST':
        
        if request.form.get('item') and len(request.form.get('item').strip()) > 0:
            item = request.form.get('item').strip()

            with sqlite3.connect(DATABASE) as conn:
                cur = conn.cursor()

                cur.execute("INSERT INTO task(task) VALUES(?)", (item, ))
                if cur.rowcount > 0:
                    status = 1
                    conn.commit()
                    payload = 'Item added'

                cur.close()
        else:
            payload = "Empyty field"
    else:
        flash("Request Method Error", 'danger')
        # return url_for("home_page")

    return jsonify({'status': status, 'payload': payload})


# read items
@app.route('/read', methods=['GET'])
def read_task():
    status = 0
    payload = []

    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    with sqlite3.connect(DATABASE) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()

        cur.execute("SELECT id, task FROM task ORDER BY id DESC")
        if cur.arraysize > 0:
            status = 1
            payload = cur.fetchall()

        cur.close()

    return jsonify({'status': status, 'payload': payload})


# update item
@app.route('/update/<task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    return f"update {task_id}"


# delete item
@app.route('/delete/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    return f"delete {task_id}"


if __name__ == "__main__":
    app.run()
