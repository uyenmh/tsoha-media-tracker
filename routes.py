from app import app
from flask import render_template, request, redirect
import users
import shows

@app.route("/")
def index():
    return render_template("index.html", shows=shows.get_all_shows())    
    
@app.route("/add_show", methods=["GET", "POST"])
def add_show():
    users.require_role(2)

    if request.method == "GET":
        return render_template("add_show.html")

    if request.method == "POST":
        users.check_csrf()

        title = request.form["title"]
        if len(title) < 1 or len(title) > 100:
            return render_template("error.html", message="Title must be 1-100 characters")

        type = request.form["type"]
        
        description = request.form["description"]
        if len(description) > 10000:
            return render_template("error.html", message="Description is too long")
            
        release_date = request.form["release_date"]

        show_id = shows.add_show(title, type, description, release_date)
        return redirect("/show/"+str(show_id))
        
        
@app.route("/remove_show", methods=["GET", "POST"])
def remove_show():
    users.require_role(2)

    if request.method == "GET":
        all_shows = shows.get_all_shows()
        return render_template("remove_show.html", shows=all_shows)

    if request.method == "POST":
        users.check_csrf()

        if "show_id" in request.form:
            show_id = request.form["show_id"]
            shows.remove_show(show_id)

        return redirect("/")
        
        
@app.route("/show/<int:show_id>")
def show_show(show_id):
    info = shows.get_show_info(show_id)
#    reviews = shows.get_reviews(show_id)

    return render_template("show.html", id=show_id, title=info.title, type=info.type, description=info.description, release_date=info.release_date)    

    
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 1 or len(username) > 20:
            return render_template("error.html", message="Tunnuksessa tulee olla 1-20 merkkiä")

        password = request.form["password"]
        if len(password) < 8:
            return render_template("error.html", message="Salasanan täytyy olla vähintään 8 merkkiä")

        role = request.form["role"]
        if role not in ("1", "2"):
            return render_template("error.html", message="Tuntematon käyttäjärooli")

        if not users.register(username, password, role):
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        return redirect("/")
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return render_template("error.html", message="Väärä tunnus tai salasana")
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")


