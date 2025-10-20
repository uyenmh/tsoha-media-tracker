from app import app
from flask import render_template, request, redirect
import users
import shows

@app.route("/")
def index():
    return render_template("index.html", shows=shows.get_all_shows(), keyword=None)    
    
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
    reviews = shows.get_reviews(show_id)
    
    return render_template("show.html", id=show_id, title=info[0], type=info[1], description=info[2], release_date=info[3], reviews=reviews)    
    
@app.route("/review", methods=["GET", "POST"])
def review():
    users.require_role(1)
    users.check_csrf()

    show_id = request.form["show_id"]
    stars = int(request.form["stars"])

    comment = request.form["comment"]
    if len(comment) > 1000:
        return render_template("error.html", message="The comment is too long")
    if comment == "":
        comment = "-"
        
    user_id = users.user_id()

    if shows.has_user_reviewed(show_id, user_id):
        return render_template("error.html", message="You have already reviewed this show")

    shows.add_review(show_id, user_id, stars, comment)

    return redirect("/show/"+str(show_id))

@app.route("/remove_own_review", methods=["POST"])
def remove_own_review():
    users.require_role(1)
    users.check_csrf()

    show_id = request.form["show_id"]
    user_id = users.user_id()

    shows.remove_own_review(show_id, user_id)

    return redirect("/show/"+str(show_id))

@app.route("/remove_review_admin", methods=["POST"])
def remove_review_admin():
    users.require_role(2)
    users.check_csrf()

    review_id = request.form["review_id"]
    shows.remove_review_admin(review_id)

    show_id = request.form["show_id"]

    return redirect("/show/"+str(show_id))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 1 or len(username) > 20:
            return render_template("error.html", message="The username must have 1-20 characters")

        password = request.form["password"]
        if len(password) < 8:
            return render_template("error.html", message="The password must be at least 8 characters long")

        role = request.form["role"]
        if role not in ("1", "2"):
            return render_template("error.html", message="Unknown user role")

        if not users.register(username, password, role):
            return render_template("error.html", message="Registration failed")
        return redirect("/")
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return render_template("error.html", message="Incorrect username or password")
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/search", methods=["POST"])
def search():
    keyword = request.form["keyword"]
    results = shows.search_shows(keyword)
    return render_template("index.html", shows=results, keyword=keyword)
