pip3 install Flask
pip3 install dnspython
pip3 install pymongo
pip3 install flask_pymongo

pkill -9 python3

hard reload: control + shift + R


<!-- {{ url_for('delete_song', song_id=song._id) }} -->


        # mongo.db.users.update({"username": username}, submit)
        # mongo.db.users.update_one(
        #    {"username": "mark"}, {"$set": {"email": "peitje@gmail.com"}})


             #submit = {
        #    "username": session["user"],
        #    "password": generate_password_hash("Delusso666!"),
        #    "gender": request.form.get("gender"),
        #    "country": request.form.get("country"),
        #    "email": request.form.get("email")
        # }