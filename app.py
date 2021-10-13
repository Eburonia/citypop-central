import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

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


@app.route("/show_songs")
def show_songs():
    songs = mongo.db.songs.find()
    return render_template("songs.html", songs=songs)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("search-query")
    songs = list(mongo.db.songs.find({"$text": {"$search": query}}))
    return render_template("songs.html", songs=songs)


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
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(regi)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Regristration succesful")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


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
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                        "profile", username=session["user"]))

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

        return render_template(
            "profile.html", username=username, settings=settings)

    return redirect(url_for("login"))


@app.route("/update_profile/<username>", methods=["GET", "POST"])
def update_profile(username):

    if request.method == "POST":
        submit = {
            "username": session["user"],
            "password": generate_password_hash("Delusso666!"),
            "gender": request.form.get("gender")
        }
        mongo.db.users.update({"username": username}, submit)
        flash("Profile Successfully Updated")

    return redirect(url_for("index"))




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
        song = {
            "artist_name": request.form.get("artist_name"),
            "song_name": request.form.get("song_name"),
            "uploaded_by": session["user"]
        }
        mongo.db.songs.insert_one(song)
        return redirect(url_for("show_songs"))

    return render_template("add_song.html")


@app.route("/edit_song/<song_id>", methods=["GET", "POST"])
def edit_song(song_id):
    if request.method == "POST":
        submit = {
            "artist_name": request.form.get("artist_name"),
            "song_name": request.form.get("song_name"),
            "uploaded_by": session["user"]
        }
        mongo.db.songs.update({"_id": ObjectId(song_id)}, submit)
        flash("Song Successfully Updated")

    song = mongo.db.songs.find_one({"_id": ObjectId(song_id)})
    return render_template("edit_song.html", song=song)


@app.route("/delete_song/<song_id>")
def delete_song(song_id):
    mongo.db.songs.remove({"_id": ObjectId(song_id)})

    return redirect(url_for("show_songs"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
