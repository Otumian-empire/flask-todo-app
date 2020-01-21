from flask import Flask, flash, jsonify, render_template, request, url_for, redirect

from model import Task, Time

app = Flask(__name__)
app.debug = True
app.secret_key = 'DH23%$ERTH:<LKH%$^7oiPJHv@#swreBF^IOUjmok;POP'


# home page
@app.route('/')
def home_page():
    return render_template('index.html', title='TO-DO-APP')


# history
@app.route('/history')
def history():
    return render_template('history.html', title='History')


# insert item
@app.route('/add', methods=['POST'])
def add_task():

    status = 0
    payload = ''

    if not request.method == 'POST':
        flash("Request Method Error", 'danger')
        return url_for("home_page")

    if request.form.get('item'):
        payload = request.form.get('item')
        status = 1
    else:
        payload = "Empyty field"

    return jsonify({'status': status, 'payload': payload})


# read items
@app.route('/read', methods=['POST'])
def read_task():
    status = 1
    payload = [
        {
            'id': 1,
            'item': "Call Dr. Amevor"
        },
        {
            'id': 2,
            'item': "Read Akiola Math"
        },
        {
            'id': 3,
            'item': "ask Adeleke to review you android code"
        },
        {
            'id': 4,
            'item': "Submit your project for review"
        },
        {
            'id': 5,
            'item': "Clearn your room, shame on you"
        }
    ]

    return jsonify({'status': status, 'payload': payload})


# update item
@app.route('/update/<task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    return f"update {task_id}"


# delete item
@app.route('/delete/<task_id>', methods=['GET', 'POST'])
def delete_task(task_id):
    return f"delete {task_id}"


if __name__ == "__main__":
    app.run()
