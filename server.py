from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def color():
    return render_template("index.html")
@app.route("/color", methods=["POST"])
def colorpicker():
    rgb = "rgb("+request.form["red"]+","+request.form["green"]+","+request.form["blue"]+")"
    return render_template("index.html", color=rgb)
app.run(debug=True)