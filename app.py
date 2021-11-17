# File: app.py
# Author: Maurice Vossen
# Date: November 2021

import os
import datetime
import math
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


@app.route("/", methods=["GET", "POST"])
def index():
    '''
    This function loads the index page which loads the results.html page
    '''

    # Set page title
    title = 'Citypop Central | Home'

    # Load the 8 latest songs from the database
    random_songs = mongo.db.songs.find().sort("_id", -1).limit(8)

    # Return information to front-end of website
    return render_template("results.html", title=title,
                           random_songs=random_songs)


@app.route('/about')
def about():
    '''
    This function loads the about.html page
    '''

    # Set page title
    title = 'Citypop Central | About'

    # Return information to front-end of website
    return render_template("about.html", title=title)


@app.route("/results", methods=["GET", "POST"])
def results():
    '''
    This function loads the index and results page
    '''

    # Set page title
    title = 'Citypop Central | Results'

    # Get search keyword(s) from textfield
    query = request.form.get("search-query")

    # Get search keyword(s) from address bar
    search = request.args.get('search')

    # Get page number from address bar
    page = request.args.get('page')

    # Determine whether search keyword is coming from textfield or address bar
    if search is None:
        query = request.form.get("search-query")
    else:
        query = request.args.get('search')

    # If search keyword is given
    if query:

        # Search in database
        songs_query = mongo.db.songs.find({"$text": {"$search": query}})

        # Sort result(s) by Artist Name
        songs_query.sort('artist_name')

        # Count the number of the records found in database
        number_of_results = songs_query.count()

        if number_of_results == 0:
            flash("No results found")
            return redirect(url_for("index"))

        # Convert to list
        songs_query = list(songs_query)

        # Declare search records data
        output = []

        # Start from page 0
        if page is None:
            page = 0

    # Check user input from the address bar
        # If non-numeric pages are selected from the address bar
        # by direct user input
        if not str(page).isnumeric():
            return redirect(url_for("index"))

        # If pages lower than 0 are selected
        if int(page) < 0:
            return redirect(url_for("index"))

    # Pagination from here

        # Set the number of records per page
        limit = 2

        # Determine number of pages needed for results
        number_of_pages = math.ceil(number_of_results / limit)

        # If user selects higher page number than available
        if int(page) >= number_of_pages:
            return redirect(url_for("index"))

        # Append the limited search records to a specific page, e.g. first 10
        # results on page 0, next 10 results on page 1
        if (int(page) + 1) * limit < number_of_results:
            for i in range(int(page) * limit, (int(page) * limit) + limit):
                output.append(songs_query[i])
        else:
            for i in range(int(page) * limit, number_of_results):
                output.append(songs_query[i])

        # Set the pagination anchor link for the previous page
        if int(page) >= 1:

            # set link for address bar
            previous_page = f"/results?search={query}\
                &page={str(int(page) - 1)}"

            # Set link text front-end
            previous_page_text = 'Prev page'

        else:

            # Set link for address bar and link front-end not needed for page 0
            previous_page = ''
            previous_page_text = ''

        # Set the pagination anchor link for the next page
        next_page_text = ''

        if int(page) < number_of_pages - 1:

            # set link for address bar
            next_page = f"/results?search={query}&page={str(int(page) + 1)}"

            # Set link text front-end
            next_page_text = 'Next page'

        else:

            # Set link for address bar and link front-end not
            # needed for last page
            next_page_text = ''
            next_page = ''

        # Set separation pipe front-end, only when
        # there is a previous and next page
        if previous_page_text and next_page_text:
            separator = '|'
        else:
            separator = ''

        # Set the start record number, depending on which page you are
        start_result = (int(page) * limit) + 1

        # Set the end record number, depending on which page you are
        if (int(page) + 1) * limit < number_of_results:
            end_result = start_result + (limit - 1)
        else:
            end_result = number_of_results

        # Set the shown search records (depending on page),
        # to be shown in front-end
        if number_of_results != 0:
            current_results = f"Result : {str(start_result)}\
                 to {str(end_result)}"
        else:
            current_results = ''

        result_numbers = []

        for i in range(start_result, end_result + 1):
            result_numbers.append(i)

        # Set the number of records found in database, to be shown in front-end
        number_of_results = 'Number of results : ' + str(number_of_results)

        # Return information to front-end of website
        return render_template("results.html", songs=output,
                               previous_page=previous_page,
                               previous_page_text=previous_page_text,
                               next_page=next_page,
                               next_page_text=next_page_text,
                               number_of_results=number_of_results,
                               separator=separator,
                               current_results=current_results,
                               result_numbers=result_numbers, title=title)

    # Return information to front-end of website
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    '''
    This function loads and handles the register.html page
    '''
    # Set page title
    title = 'Citypop Central | Register'

    if request.method == "POST":

        # Check whether both passwords textfield the same password is given
        if request.form.get("password") != \
                request.form.get("password-confirm"):

            # Flash message failed, return register page
            flash('Passwords do not match')
            return redirect(url_for("register"))

        # Check whether given username already exist in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # If username already exists
        if existing_user:

            # Flash message username already exists
            flash('Username already exists')
            return redirect(url_for("register"))

        # Check whether given email address already exist in the database
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email")})

        # If email address already exists
        if existing_email:

            # Flash message email address already exists
            flash('Email address already exists')
            return redirect(url_for("register"))

        # If username does not exist, create user
        regi = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower(),
            "country_name": request.form.get("country").lower(),
            "gender": request.form.get("gender").lower(),
            "share_email": request.form.get("share-email")
        }

        # Add new user to database
        mongo.db.users.insert_one(regi)

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()

        # Flash message registration succesful
        flash("Registration succesful")

        # Return to newly created profile page
        return redirect(url_for("profile", username=session["user"]))

    # Load available country names and gender from database to register page
    countries = mongo.db.countries.find().sort("country_name", 1)
    genders = mongo.db.genders.find().sort("gender", 1)

    # Return information to front-end of website
    return render_template("register.html", countries=countries,
                           genders=genders, title=title)


@app.route("/login", methods=["GET", "POST"])
def login():
    '''
    This function loads and handles the login.html page
    '''

    # Set page title
    title = 'Citypop Central | Login'

    if request.method == "POST":

        # Check whether username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # In case username exists in database
        if existing_user:

            # Check login password
            if check_password_hash(existing_user["password"], request.form.get(
               "password")):

                # Password correct, set session cookie
                session["user"] = request.form.get("username").lower()

                # Flash message login succesful
                flash("Welcome back {}".format(request.form.get("username")))

                # Return to the index page
                return redirect(url_for("index", username=session["user"]))

            else:
                # Invalid password given
                # Flash message password or username not correct
                flash("Incorrect username and/or password")

                # Return to login page
                return redirect(url_for("login"))

        else:

            # In case username does not exist in database
            # Flash message password or username not correct
            flash("Incorrect username and/or password")

            # Return to login page
            return redirect(url_for("login"))

    # Return information to front-end of website
    return render_template("login.html", title=title)


@app.route("/profile", methods=["GET", "POST"])
def profile():
    '''
    This function loads the profile.html page
    '''

    # Is user is logged in
    if 'user' in session:

        # Set page title
        title = 'Citypop Central | Profile'

        # Set username front-end
        username = request.form.get("username")

        # Get username from database
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        # Get all user settings from database
        user_settings = mongo.db.users.find_one({"username": session["user"]})

        # Get all countries from database
        countries = mongo.db.countries.find().sort("country_name", 1)

        # Get all genders from database
        genders = mongo.db.genders.find().sort("gender", 1)

        # Get all uploaded songs by user from database
        my_songs = mongo.db.songs.find({"uploaded_by": session["user"]}).sort(
                   "artist_name", 1)

        # Return information to front-end of website
        return render_template(
            "profile.html", username=username, settings=user_settings,
            countries=countries, genders=genders, title=title,
            my_songs=my_songs)

    # In case not logged in go to login page
    return redirect(url_for("login"))


@app.route("/update_profile/<username>", methods=["GET", "POST"])
def update_profile(username):
    '''
    This function updates the profile.html page
    '''

    if request.method == "POST":

        # Check whether both passwords textfield the same password is given
        if request.form.get("password") != \
                request.form.get("password-confirm"):

            # Flash message failed, return register page
            flash('Passwords do not match')
            return redirect(url_for("profile"))

        # Update profile settings
        submit = {
            "$set": {"email": request.form.get(
                "email"), "country_name": request.form.get("country"),
                "share_email": request.form.get("share-email"),
                "password": generate_password_hash(
                    request.form.get("password"))}
                }

        # Update profile settings in the database
        mongo.db.users.update({"username": username}, submit)

        # Flash message profile has been updated successfully
        flash("Profile successfully updated")

    # Return to the index page
    return redirect(url_for("index"))


@app.route("/delete-profile")
def delete_profile():
    '''
    This function deletes your profile page
    '''

    # Is user is logged in
    if 'user' in session:

        # Delete user from database
        mongo.db.users.remove({"username": session["user"]})

        # Remove session cookie
        session.pop("user")

        # Flash message profile has been deleted
        flash("Your profile has been deleted")

        # Return to register page
        return redirect(url_for("register"))

    else:
        # Return to index page
        return redirect(url_for("index"))


@app.route("/logout")
def logout():
    '''
    Thus function logges you out
    '''

    # Is user is logged in
    if 'user' in session:

        # Remove user from session cookies
        # Flash message you have been logged out
        flash("You have been logged out")

        # Remove session cookie
        session.pop("user")

        # Redirect to the login page
        return redirect(url_for("login"))

    else:
        # Redirect to the login page
        return redirect(url_for("login"))


@app.route("/add_song", methods=["GET", "POST"])
def add_song():
    '''
    This function loads the add_song.html page and
    adds a song into the database
    '''

    # Set page title
    title = 'Citypop Central | Add Song'

    # Is user is logged in
    if 'user' in session:

        if request.method == "POST":

            # Get date of today
            date_time_now = datetime.datetime.now()

            # Convert to '13 November 2019'
            date = str(date_time_now.day) + " " +\
                str(date_time_now.strftime("%B")) + " "\
                + str(date_time_now.year)

            # Create data memory for song
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

            # Insert the song into the database
            mongo.db.songs.insert_one(song)

            # Flash message song added succesfully
            flash('Song has been added to the database')

            # Return to index page
            return redirect(url_for("index"))

        # Add allowable release years from database to front-end
        release_years = mongo.db.release_years.find().sort("release_year", 1)

        # Add allowable gender names from database to front-end
        genres = mongo.db.genres.find().sort("genre", 1)

        # Return information to front-end of website
        return render_template(
            "add_song.html", genres=genres,
            release_years=release_years, title=title)

    else:
        # Redirect to the index page
        return redirect(url_for("index"))


@app.route("/edit_song", methods=["GET", "POST"])
def edit_song():
    '''
    This function loads the song you want to edit from the database
    '''

    # Set page title
    title = 'Citypop Central | Edit Song'

    # Get song id from address bar
    song_id = request.args.get('song_id')

    # Get the song from the database
    song = mongo.db.songs.find_one({"_id": ObjectId(song_id)})

    # Song uploaded by this user before
    uploaded_by = song["uploaded_by"]

    # If user is logged in
    if 'user' in session:

        if session['user'] != 'admin':

            # Logged in user is not the same as user who uploaded the song
            if uploaded_by != session["user"]:

                # Flash message not allowed to update song
                flash("You are not allowed to update this song")

                # Redirect to the index page
                return redirect(url_for("index"))
    else:

        # Flash message not allowed to update song for non-logged in persons
        flash("You are not allowed to update this song")

        # Redirect to the index page
        return redirect(url_for("index"))

    # Add allowable genre names from database to front-end
    genres = mongo.db.genres.find().sort("genre", 1)

    # Add allowable release names from database to front-end
    release_years = mongo.db.release_years.find().sort("release_year", 1)

    # Return information to front-end of website
    return render_template("edit_song.html", song=song, genres=genres,
                           release_years=release_years, title=title)


@app.route("/update_song/<song_id>", methods=["GET", "POST"])
def update_song(song_id):
    '''
    This function updates a specific song in the database
    '''

    if request.method == "POST":

        # Get date of today
        date_time_now = datetime.datetime.now()

        # Convert to '13 November 2019'
        date = str(date_time_now.day) + " " + str(
            date_time_now.strftime("%B")) + " " + str(date_time_now.year)

        # Import data from form
        submit = {
            "$set": {
                "artist_name": request.form.get("artist_name"),
                "song_name": request.form.get("song_name"),
                "genre": request.form.get("genre"),
                "release_year": request.form.get("release_year"),
                "album_name": request.form.get("album_name"),
                "album_image": request.form.get("album_image"),
                "song_length": request.form.get("song_length"),
                "youtube": request.form.get("youtube"),
                "edit_date": date
                    }
                }

        # Update song in database
        mongo.db.songs.update({"_id": ObjectId(song_id)}, submit)

        # Flash message song successfully updated
        flash("Song successfully updated")

    # Return to index page
    return redirect(url_for("index"))


@app.route("/delete_song/<song_id>")
def delete_song(song_id):
    '''
    This function deletes a specific song in the database
    '''

    # Get the song from the database
    song = mongo.db.songs.find_one({"_id": ObjectId(song_id)})

    # Song uploaded by this user before
    uploaded_by = song["uploaded_by"]

    # If a user is logged in
    if 'user' in session:

        # If admin or orginial user who uploaded the song is logged in
        if session['user'] == 'admin' or session['user'] == uploaded_by:

            # Delete song from database
            mongo.db.songs.remove({"_id": ObjectId(song_id)})

            # Flash message song removed from database
            flash("Song removed from database")
            return redirect(url_for("index"))

    # Flash message not allowed to delete this song
    flash("You are not allowed to delete this song")
    return redirect(url_for("index"))


@app.route("/userinfo")
def userinfo():
    '''
    This function loads the userinfo.html page of a specific user
    '''

    # Set page title
    title = 'Citypop Central | User Information'

    # Get user name from address bar
    user = request.args.get("user")

    # Find user name from address bar in database
    existing_user = mongo.db.users.find_one({"username": user})

    # If user does not exist
    if existing_user is None:
        user = 'user does not exist'

        # Return information to front-end of website
        return render_template("userinfo.html",
                               user=user, existing_user=existing_user)

    # Return user information to front-end of website
    return render_template("userinfo.html", user=user,
                           existing_user=existing_user, title=title)


@app.route("/youtube")
def youtube():
    '''
    This function opens a specific YouTube song
    '''

    # Set page title
    title = 'Citypop Central | Youtube'

    # Get Youtube link ID from address bar
    link = request.args.get("link")

    # Create YouTube link to open video
    link = f"https://www.youtube.com/embed/{link}"

    # Return information to front-end of website
    return render_template("youtube.html", title=title, link=link)


@app.route("/my_songs")
def mysongs():
    '''
    This function opens the my_songs.html page
    '''

    # Set page title
    title = 'Citypop Central | My Songs'

    # If user is logged in
    if 'user' in session:

        if session["user"] == 'admin':
            # Import all songs when logged in as admin
            my_songs = mongo.db.songs.find().sort("artist_name", 1)
        else:
            # Import my uploaded songs from database
            my_songs = mongo.db.songs.find(
                {"uploaded_by": session["user"]}).sort("artist_name", 1)

    else:

        # If no user is logged in return to index page
        return redirect(url_for("index"))

    # Return information to front-end of website
    return render_template("my_songs.html", my_songs=my_songs, title=title)


@app.route("/users", methods=["GET", "POST"])
def users():
    '''
    This function opens the users.html page
    which is only accessible by the admin
    '''

    # Set page title
    title = 'Citypop Central | Users'

    if 'user' in session:
        if session["user"] == 'admin':

            # Load all users on screen
            all_users = mongo.db.users.find().sort("username", 1)

        else:
            # Flash message no acces for other users
            flash("You have no access to this page")

            # Return to main page
            return redirect(url_for("index"))
    else:
        # Flash message no access for visitors
        flash("You have no access to this page")

        # Return to main page
        return redirect(url_for("index"))

    # Return information to front-end of website
    return render_template("users.html", all_users=all_users, title=title)


@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    '''
    This function deletes a specific user in the database
    '''

    # Delete user from database
    mongo.db.users.remove({"_id": ObjectId(user_id)})

    # Flash message user deleted from database
    flash('User has been deleted from the database')

    # Return to index page
    return redirect(url_for("users"))


@app.route("/settings")
def settings():
    '''
    This function shows all settings to the admin
    '''

    # Set page title
    title = 'Citypop Central | Settings'

    if 'user' in session:
        if session["user"] == 'admin':

            # Load all settings on screen

            # Get all the countries from the database
            countries = mongo.db.countries.find().sort("country_name", 1)

            # Get all the genders from the database
            genders = mongo.db.genders.find().sort("gender", 1)

            # Get all the genres from the database
            genres = mongo.db.genres.find().sort("genre", 1)

            # Get all the release years from the database
            release_years = mongo.db.release_years.find().sort(
                "release_year", 1)

        else:
            # Flash message no acces for other users
            flash("You have no access to this page")

            # Return to main page
            return redirect(url_for("index"))
    else:
        # Flash message no access for visitors
        flash("You have no access to this page")

        # Return to main page
        return redirect(url_for("index"))

    # Return information to front-end of website
    return render_template("settings.html", countries=countries,
                           genders=genders, genres=genres,
                           release_years=release_years, title=title)


@app.route("/delete_country", methods=["GET", "POST"])
def delete_country():
    '''
    This function removes a specific country from the database
    '''

    if request.method == "POST":

        # Delete country from database
        mongo.db.countries.remove(
            {"country_name": request.form.get("remove-country")})

        # Flash message country removed from database
        flash("Country removed from the database")

        # Return to index page
        return redirect(url_for("settings"))

    else:
        # Flash message no access
        flash("You have no access to this page")

        # Return to main page
        return redirect(url_for("index"))


@app.route("/delete_gender", methods=["GET", "POST"])
def delete_gender():
    '''
    This function removes a specific gender from the database
    '''

    if request.method == "POST":

        # Delete gender from database
        mongo.db.genders.remove({"gender": request.form.get("remove-gender")})

        # Flash message gender removed from database
        flash("Gender removed from the database")

        # Return to index page
        return redirect(url_for("settings"))

    else:
        # Flash message no access
        flash("You have no access to this page")

        # Return to main page
        return redirect(url_for("index"))


@app.route("/delete_genre", methods=["GET", "POST"])
def delete_genre():
    '''
    This function removes a specific genre from the database
    '''

    if request.method == "POST":

        # Delete genre from database
        mongo.db.genres.remove({"genre": request.form.get("remove-genre")})

        # Flash message genre removed from database
        flash("Genre removed from the database")

        # Return to index page
        return redirect(url_for("settings"))

    else:
        # Flash message no access
        flash("You have no access to this page")

        # Return to main page
        return redirect(url_for("index"))


@app.route("/delete_release_year", methods=["GET", "POST"])
def delete_release_year():
    '''
    This function removes a specific release year from the database
    '''

    if request.method == "POST":

        # Delete release year from database
        mongo.db.release_years.remove(
            {"release_year": request.form.get("remove-release-year")})

        # Flash message release year removed from database
        flash("Release year removed from the database")

        # Return to settings page
        return redirect(url_for("settings"))

    else:
        # Flash message no access
        flash("You have no access to this page")

        # Return to main page
        return redirect(url_for("index"))


@app.route("/add_country", methods=["GET", "POST"])
def add_country():
    '''
    This function adds a new country to the database
    '''

    if request.method == "POST":

        # Create data memory for country
        new_country = {
            "country_name": request.form.get("add-country")
        }

        # Insert the country into the database
        mongo.db.countries.insert_one(new_country)

        # Flash message country added to database
        flash("Country added to the database")

        # Return to index page
        return redirect(url_for("settings"))

    else:
        # Flash message no access
        flash("You have no access to this page")

        # Return to main page
        return redirect(url_for("index"))


@app.route("/add_gender", methods=["GET", "POST"])
def add_gender():
    '''
    This function adds a new gender to the database
    '''

    if request.method == "POST":

        # Create data memory for gender
        new_gender = {
            "gender": request.form.get("add-gender")
        }

        # Insert the gender into the database
        mongo.db.genders.insert_one(new_gender)

        # Flash message gender added to database
        flash("Gender added to the database")

        # Return to index page
        return redirect(url_for("settings"))

    else:
        # Flash message no access
        flash("You have no access to this page")

        # Return to main page
        return redirect(url_for("index"))


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    '''
    This function adds a new genre to the database
    '''

    if request.method == "POST":

        # Create data memory for genre
        new_genre = {
            "genre": request.form.get("add-genre")
        }

        # Insert the genre into the database
        mongo.db.genres.insert_one(new_genre)

        # Flash message genre added to database
        flash("Genre added to the database")

        # Return to index page
        return redirect(url_for("settings"))

    else:
        # Flash message no access
        flash("You have no access to this page")

        # Return to main page
        return redirect(url_for("index"))


@app.route("/add_release_year", methods=["GET", "POST"])
def add_release_year():
    '''
    This function adds a new release year to the database
    '''

    if request.method == "POST":

        # Create data memory for release year
        new_release_year = {
            "release_year": request.form.get("add-release-year")
        }

        # Insert the release year into the database
        mongo.db.release_years.insert_one(new_release_year)

        # Flash message release year added to database
        flash("Release year added to the database")

        # Return to index page
        return redirect(url_for("settings"))

    else:
        # Flash message no access
        flash("You have no access to this page")

        # Return to main page
        return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(e):
    '''
    This function handles 404 errors
    '''

    # Set page title
    title = 'Citypop Central | 404 error'

    # Return information to front-end of website
    return render_template('404.html', title=title), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
