from flask import Flask, render_template, url_for


app = Flask(__name__)
app.debug = True


# home page
@app.route('/')
def home_page():
    return render_template('app.html', title='TO-DO-APP')


# history
@app.route('/history/')
def history():
    return render_template('history.html', title='History')


# insert item
@app.route('/add/', methods=['GET', 'POST'])
def add_task():
    return "new task"


# read item
@app.route('/read/')
@app.route('/read/<task_id>/')
def read_task(task_id=''):
    return f"read {task_id}"


# update item
@app.route('/update/<task_id>/', methods=['GET', 'POST'])
def update_task(task_id):
    return f"update {task_id}"


# delete item
@app.route('/delete/<task_id>/', methods=['GET', 'POST'])
def delete_task(task_id):
    return f"delete {task_id}"


if __name__ == "__main__":
    app.run()
