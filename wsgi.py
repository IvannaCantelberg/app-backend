# from src import create_app

from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    from src.routes import smoke
    app.register_blueprint(smoke.bp)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
