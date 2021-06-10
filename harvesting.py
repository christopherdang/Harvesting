from flask import Flask, redirect, url_for, render_template, request, send_file

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def default():
    if request.method == "POST":
        company = request.form["company"]
        username = request.form["username"]
        password = request.form["password"]

        return render_template("home.html", company=company, username=username, password=password)

    else:
        return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/idenColor")
def idenColor():
    return render_template("idenColor.html")

@app.route("/idenColorGame")
def idenColorGame():
    return render_template("idenColorGame.html")

if __name__ == "__main__":
    app.run(debug="True")