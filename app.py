import os
from flask import (
    Flask, flash, render_template, redirect, request, jsonify, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGODB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():

    songs = mongo.db.songs.find()
    return render_template("index.html", songs=songs)



@app.route("/database", methods=["GET"])
def database():

    song = mongo.db.songs

    maximum = song.count()

    offset = int(request.args['offset'])
    limit = int(request.args['limit'])

    starting_id = song.find().sort('_id', 1)
    last_id = starting_id[offset]['_id']

    numb = song.find({'_id': {'$gte': last_id}}).sort('_id', 1).limit(limit)

    next_url = '/database?limit=' + str(limit) + '&offset=' + str(offset + limit)
    prev_url = '/database?limit=' + str(limit) + '&offset=' + str(offset - limit)

    return render_template("database.html",
                           numb=numb, prev_url=prev_url, next_url=next_url, offset=offset, limit=limit, maximum=maximum)


@app.route("/songs", methods=["GET"])
def songs():

    number = mongo.db.numbers

    maxixum = number.count()

    # offset = starting point
    page = int(request.args['page'])


    # limit = show amount of records on page
    limit = 10

    starting_id = number.find().sort('_id', 1)
    last_id = starting_id[page*10]['_id']

    numb = number.find(
        {'_id': {'$gte': last_id}}).sort('_id', 1).limit(limit)

    output = []

    for i in numb:
        output.append(i['number'])

    next_page = page + 1
    previous_page = page - 1

    print(next_page)
    next_url = '/songs?page=' + str(next_page)
    prev_url = '/songs?page=' + str(previous_page)

    return render_template("songs.html", a=output, next_url=next_url,
                           prev_url=prev_url, limit=limit, maximum=maxixum, page=page)


@app.route("/numbers", methods=["GET"])
def numbers():

    number = mongo.db.numbers

    maxixum = number.count()

    # offset = starting point
    offset = int(request.args['offset'])

    # limit = show amount of records on page
    limit = int(request.args['limit']) 

    starting_id = number.find().sort('_id', 1)
    last_id = starting_id[offset]['_id']

    numb = number.find(
        {'_id': {'$gte': last_id}}).sort('_id', 1).limit(limit)

    output = []

    for i in numb:
        output.append(i['number'])

    next_url = '/numbers?limit=' + str(
        limit) + '&offset=' + str(offset + limit)
    prev_url = '/numbers?limit=' + str(
        limit) + '&offset=' + str(offset - limit)

    return render_template("numbers.html", a=output, next_url=next_url, prev_url=prev_url, offset=offset, limit=limit, max=maxixum)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("search-query")
    songs = list(mongo.db.songs.find({"$text": {"$search": query}}))
    return render_template("index.html", songs=songs)


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash('Username already exists')
            return redirect(url_for("register"))

        regi = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "country_name": request.form.get("country").lower()
        }

        mongo.db.users.insert_one(regi)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Regristration succesful")
        return redirect(url_for("profile", username=session["user"]))

    countries = mongo.db.countries.find().sort("country_name", 1)
    return render_template("register.html", countries=countries)


@app.route("/login", methods=["GET", "POST"])
def login():
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

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:

        settings = mongo.db.users.find_one({"username": session["user"]})

        countries = mongo.db.countries.find().sort("country_name", 1)
        genders = mongo.db.genders.find().sort("gender", 1)

        return render_template(
            "profile.html", username=username, settings=settings, countries=countries, genders=genders)

    return redirect(url_for("login"))


@app.route("/update_profile/<username>", methods=["GET", "POST"])
def update_profile(username):

    if request.method == "POST":

        submit = {
            "$set": {"email": request.form.get(
                "email"), "gender": request.form.get(
                    "gender"), "country": request.form.get("country")}
        }

        mongo.db.users.update({"username": username}, submit)

        flash("Profile Successfully Updated")

    return redirect(url_for("index"))


@app.route("/get_countries")
def show_countries():
    countries = mongo.db.countries.find()
    return render_template("register.html", countries=countries)


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_song", methods=["GET", "POST"])
def add_song():
    # add a song to the database
    if request.method == "POST":

        x = datetime.datetime.now()
        date = str(x.day) + " " + str(x.strftime("%B")) + " " + str(x.year)

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
    return render_template("add_song.html", genres=genres, release_years=release_years)


@app.route("/edit_song/<song_id>", methods=["GET", "POST"])
def edit_song(song_id):
    if request.method == "POST":

        x = datetime.datetime.now()
        date = str(x.day) + " " + str(x.strftime("%B")) + " " + str(x.year)

        submit = {
            "$set": {"artist_name": request.form.get(
                "artist_name"), "song_name": request.form.get(
                    "song_name"), "uploaded_by": session["user"], "genre": request.form.get(
                        "genre"), "release_year": request.form.get(
                            "release_year"), "album_name": request.form.get(
                                "album_name"), "album_image": request.form.get(
                                    "album_image"), "song_length": request.form.get(
                                        "song_length"), "edit_date": date}
        }

        mongo.db.songs.update({"_id": ObjectId(song_id)}, submit)
        flash("Song Successfully Updated")
        return redirect(url_for("index"))
        
    genres = mongo.db.genres.find().sort("genre", 1)
    release_years = mongo.db.release_years.find().sort("release_year", 1)
    song = mongo.db.songs.find_one({"_id": ObjectId(song_id)})
    return render_template("edit_song.html", song=song, genres=genres, 
                           release_years=release_years)


@app.route("/delete_song/<song_id>")
def delete_song(song_id):
    mongo.db.songs.remove({"_id": ObjectId(song_id)})

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
