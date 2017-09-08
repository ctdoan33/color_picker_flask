from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def color():
    return render_template("index.html")
@app.route("/color", methods=["POST"])
def colorpicker():
    r = request.form["red"]
    g = request.form["green"]
    b = request.form["blue"]
    rgb = "rgb("+r+","+g+","+b+")"
    return render_template("index.html", color=rgb)
app.run(debug=True)