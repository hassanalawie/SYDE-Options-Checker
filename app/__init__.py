from flask import Flask

# Initialize the Flask app
def create_app():
    app = Flask(__name__)

    # Register routes
    from app.routes import bp
    app.register_blueprint(bp)

    return app
