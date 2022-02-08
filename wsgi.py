from flask import Flask, render_template

from src.resources.smoke import Smoke

app = Flask(__name__, template_folder='static')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/smoke')
def smoke():
    return Smoke().get()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
