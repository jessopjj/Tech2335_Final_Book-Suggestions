# this is the "web_app/__init__.py" file...
import os

from flask import Flask

from web_app.routes.book_suggestions_routes import book_suggestions_routes

SECRET_KEY = os.getenv("SECRET_KEY", default="Quick Key") # set this to something else on production!!!

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    app.register_blueprint(book_suggestions_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)