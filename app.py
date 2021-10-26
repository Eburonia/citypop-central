import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import math

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGODB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/", methods=["GET", "POST"])
def index():

    title = 'Citypop Central | Home'

    return render_template("results.html", title=title)


@app.route("/results", methods=["GET", "POST"])
def results():

    title = 'Citypop Central | Results'

    query = request.form.get("search-query")

    # query variables
    # keyword to search for
    search = request.args.get('search')

    # page number of results
    page = request.args.get('page')

    if search is None:
        query = request.form.get("search-query")
    else:
        query = request.args.get('search')

    if query:

        songs_query = mongo.db.songs.find({"$text": {"$search": query}})
        songs_query.sort('artist_name')
        number_of_results = songs_query.count()

        songs_query = list(songs_query)

        output = []

        if page is None:
            page = 0

        # Pagination

        # Limit the amount of results per page
        limit = 2

        # Determine number of pages needed for results
        number_of_pages = math.ceil(number_of_results / limit)

        if((int(page) + 1) * limit < number_of_results):
            for i in range(int(page) * limit, (int(page) * limit) + limit):
                output.append(songs_query[i])
        else:
            for i in range(int(page) * limit, number_of_results):
                output.append(songs_query[i])

        # Determine previous page link for pagination

        if int(page) >= 1:

            previous_page = f"/results?search={query}\
                &page={str(int(page) - 1)}"
            previous_page_text = 'Prev Page'

        else:

            previous_page = ''
            previous_page_text = ''

        # Determine next page link for pagination
        next_page_text = ''

        if int(page) < number_of_pages - 1:

            next_page = f"/results?search={query}&page={str(int(page) + 1)}"
            next_page_text = 'Next Page'

        else:

            next_page_text = ''
            next_page = ''

        # Seperation pipe
        if previous_page_text and next_page_text:
            separator = '|'
        else:
            separator = ''

        start_result = (int(page) * limit) + 1

        if((int(page) + 1) * limit < number_of_results):
            end_result = start_result + (limit - 1)
        else:
            end_result = number_of_results

        if number_of_results != 0:

            current_results = f"Result : {str(start_result)}\
                 to {str(end_result)}"
        else:
            current_results = ''

        result_numbers = []

        for i in range(start_result, end_result + 1):
            result_numbers.append(i)

        number_of_results = 'Number of results : ' + str(number_of_results)

        return render_template("results.html", songs=output, search=search,
                               previous_page=previous_page,
                               previous_page_text=previous_page_text,
                               next_page=next_page,
                               next_page_text=next_page_text,
                               number_of_results=number_of_results,
                               separator=separator,
                               current_results=current_results,
                               result_numbers=result_numbers, title=title)

    return render_template("results.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    title = 'Citypop Central | Register'

    if request.method == "POST":

        if request.form.get("password") != \
                request.form.get("password-confirm"):

            flash('Passwords do not match')
            return redirect(url_for("register"))

        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash('Username already exists')
            return redirect(url_for("register"))

        regi = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower(),
            "country_name": request.form.get("country").lower(),
            "gender": request.form.get("gender").lower()
        }

        mongo.db.users.insert_one(regi)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration succesful")
        return redirect(url_for("profile", username=session["user"]))

    countries = mongo.db.countries.find().sort("country_name", 1)
    genders = mongo.db.genders.find().sort("gender", 1)

    return render_template("register.html", countries=countries,
                           genders=genders, title=title)


@app.route("/login", methods=["GET", "POST"])
def login():

    title = 'Citypop Central | Login'

    if request.method == "POST":
        # check whether username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                        "index", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html", title=title)


@app.route("/profile", methods=["GET", "POST"])
def profile():

    username = request.form.get("username")

    title = 'Citypop Central | Profile'

    # grab the session user's username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:

        settings = mongo.db.users.find_one({"username": session["user"]})

        countries = mongo.db.countries.find().sort("country_name", 1)
        genders = mongo.db.genders.find().sort("gender", 1)

        return render_template(
            "profile.html", username=username, settings=settings,
            countries=countries, genders=genders, title=title)

    return redirect(url_for("login"))


@app.route("/update_profile/<username>", methods=["GET", "POST"])
def update_profile(username):

    if request.method == "POST":

        submit = {
            "$set": {"email": request.form.get(
                "email"), "gender": request.form.get(
                    "gender"), "country_name": request.form.get("country")}
        }

        mongo.db.users.update({"username": username}, submit)

        flash("Profile Successfully Updated")

    return redirect(url_for("index"))


@app.route("/delete-profile")
def delete_profile():

    mongo.db.users.remove({"username": session["user"]})
    session.pop("user")

    flash("Your profile has been deleted")
    return redirect(url_for("register"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_song", methods=["GET", "POST"])
def add_song():

    title = 'Citypop Central | Add Song'

    # Add a song to the database
    if request.method == "POST":

        date_time_now = datetime.datetime.now()
        date = str(date_time_now.day) + " " +\
            str(date_time_now.strftime("%B")) + " " + str(date_time_now.year)

        song = {
            "artist_name": request.form.get("artist_name"),
            "song_name": request.form.get("song_name"),
            "youtube": request.form.get("youtube"),
            "uploaded_by": session["user"],
            "genre": request.form.get("genre"),
            "upload_date": str(date),
            "album_name": request.form.get("album_name"),
            "release_year": request.form.get("release_year"),
            "album_image": request.form.get("album_image"),
            "song_length": request.form.get("song_length")
        }

        mongo.db.songs.insert_one(song)
        return redirect(url_for("index"))

    release_years = mongo.db.release_years.find().sort("release_year", 1)
    genres = mongo.db.genres.find().sort("genre", 1)

    return render_template("add_song.html", genres=genres,
                           release_years=release_years, title=title)


@app.route("/edit_song/<song_id>", methods=["GET", "POST"])
def edit_song(song_id):

    if request.method == "POST":

        x = datetime.datetime.now()
        date = str(x.day) + " " + str(x.strftime("%B")) + " " + str(x.year)

        submit = {
            "$set": {"artist_name": request.form.get(
                "artist_name"), "song_name": request.form.get(
                "song_name"), "uploaded_by": session["user"],
                "genre": request.form.get(
                "genre"), "release_year": request.form.get(
                "release_year"), "album_name": request.form.get(
                "album_name"), "album_image": request.form.get(
                "album_image"), "song_length": request.form.get(
                "song_length"), "edit_date": date}
        }

        mongo.db.songs.update({"_id": ObjectId(song_id)}, submit)
        flash("Song Successfully Updated")
        return redirect(url_for("results"))

    genres = mongo.db.genres.find().sort("genre", 1)
    release_years = mongo.db.release_years.find().sort("release_year", 1)
    song = mongo.db.songs.find_one({"_id": ObjectId(song_id)})
    return render_template("edit_song.html", song=song, genres=genres,
                           release_years=release_years)


@app.route("/delete_song/<song_id>")
def delete_song(song_id):
    mongo.db.songs.remove({"_id": ObjectId(song_id)})

    return redirect(url_for("results"))


@app.route("/userinfo")
def userinfo():

    title = 'Citypop Central | User Information'

    user = request.args.get("user")

    existing_user = mongo.db.users.find_one({"username": user})

    if existing_user is None:
        user = 'user does not exist'
        return render_template("userinfo.html",
                               user=user, existing_user=existing_user)

    return render_template("userinfo.html", user=user,
                           existing_user=existing_user, title=title)


@app.route("/youtube")
def youtube():

    title = 'Citypop Central | Youtube'

    link = request.args.get("link")

    return render_template("youtube.html", title=title, link=link)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
