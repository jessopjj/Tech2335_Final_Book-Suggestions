# this is the "web_app/routes/book_suggestions_routes.py" file...

from flask import Blueprint, request, render_template

book_suggestions_routes = Blueprint("book_suggestions_routes", __name__)

@book_suggestions_routes.route("/")
@book_suggestions_routes.route("/books")
def index():
    print("Book Bestie")
    #return "Welcome Home"
    return render_template("book_suggestions_page.html")
