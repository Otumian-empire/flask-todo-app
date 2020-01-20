from flask import Flask, flash, jsonify, render_template, request, url_for

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
        # item = request.form.get('item')

        # if Task().insert_task(item):
        #     flash("item added", 'success')
        #     # return url_for('home_page')
        #     return "success"

        payload = request.form.get('item')
        status = 1

    # else:
    #     payload = "click the button"

    return jsonify({'status': status, 'payload': payload})


# # read item
# @app.route('/read')
# @app.route('/read/<task_id>')
# def read_task(task_id=''):
#     return f"read {task_id}"


# # update item
# @app.route('/update/<task_id>', methods=['GET', 'POST'])
# def update_task(task_id):
#     return f"update {task_id}"


# # delete item
# @app.route('/delete/<task_id>', methods=['GET', 'POST'])
# def delete_task(task_id):
#     return f"delete {task_id}"


if __name__ == "__main__":
    app.run()
