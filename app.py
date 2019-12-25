from flask import Flask, render_template, url_for


app = Flask(__name__)
app.debug = True


@app.route('/')
def home_page():
    return render_template('app.html', title='TO-DO-APP')


@app.route('/history')
def history():
    return render_template('history.html', title='History')


if __name__ == "__main__":
    app.run()
