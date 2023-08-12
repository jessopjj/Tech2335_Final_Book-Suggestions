# this is the "web_app/routes/book_suggestions_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.book_suggestions import search_books, display_book_details, suggest_random_book

book_suggestions_routes = Blueprint("book_suggestions_routes", __name__)



@book_suggestions_routes.route("/")
@book_suggestions_routes.route("/books")
def index():
    print("Book Bestie")
    #return "Welcome Home"
    return render_template("book_suggestions_form.html")

@book_suggestions_routes.route("/books/search")
def book_suggestions_search():
    print("BOOK SUGGESTIONS SEARCH...")

    try:
        data = search_books()

#WORKING ON THIS!!!

        flash("Fetched Book Query Data!", "success")
        return render_template("book_suggestions_form.html",
            data = data
        )
    except Exception as err:
        print("OOPS", err)

        flash("Book Query Data Error. Please try again.", "danger")
        return redirect("/")


#API  ROUTES

@book_suggestions_routes.route("/api/books.json")
def books_api():
    print("BOOK DATA (API)...")

    try:
        data = search_books()
        return data
    except Exception as err:
        print('OOPS', err)
        return {"message":"Book Query Data Error. Please try again."}, 404
