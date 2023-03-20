from flask import Flask, render_template
from jinja2 import FileSystemLoader

app = Flask(__name__)

app.jinja_loader = FileSystemLoader('../frontend/public')

@app.route("/")
def index():
    return render_template("index.html")
if __name__ == "__main__":
    app.run()