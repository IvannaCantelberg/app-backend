from flask import Flask, render_template


def create_app():
    app = Flask(__name__, template_folder='../static', static_folder='../static')

    @app.route('/')
    def index():
        return render_template('index.html')

    from src.routes import smoke
    app.register_blueprint(smoke.bp)

    return app
