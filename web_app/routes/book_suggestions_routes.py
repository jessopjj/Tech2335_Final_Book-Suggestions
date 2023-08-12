# this is the "web_app/routes/book_suggestions_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.book_suggestions import search_books, display_book_details, suggest_random_book

book_suggestions_routes = Blueprint("book_suggestions_routes", __name__)



@book_suggestions_routes.route("/")
@book_suggestions_routes.route("/books")
def form():
    print("BOOK FORM...")
    return render_template("book_suggestions_form.html")

@book_suggestions_routes.route("/books/readout", methods=["GET", "POST"])
def readout():
    print("BOOK READOUT...")
    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    query = request.data.get("query")

    try:

#ADD PYTHON CODE HERE

        flash("Fetched Book Query Data!", "success")
        return render_template("book_suggestions_readout",
                               
#AND HERE - all of the results above = themselves

        )
    except Exception as err:
        print("OOPS", err)

        flash("Book Query Data Error. Please try again.", "danger")
        return redirect("/")


#API  ROUTES - NEED TO FIGURE OUT

@book_suggestions_routes.route("/api/books.json")
def books_api():
    print("BOOK DATA (API)...")

    try:
        data = search_books()
        return data
    except Exception as err:
        print('OOPS', err)
        return {"message":"Book Query Data Error. Please try again."}, 404
