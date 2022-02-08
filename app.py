from flask import Flask, render_template


def create_app():
    app = Flask(__name__, template_folder='static', static_url_path='')

    @app.route('/')
    def index():
        return render_template('index.html')

    from src.routes import smoke
    app.register_blueprint(smoke.bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
