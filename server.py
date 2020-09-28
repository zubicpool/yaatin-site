from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/resume")
def resume():
    return render_template("resume.html")
@app.route("/about")
def about():
    return render_template("#about")
if __name__ == "__main__":
    app.run(debug=True)