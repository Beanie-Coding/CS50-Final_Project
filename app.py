import json
import sqlite3
from flask import Flask, render_template, session, redirect, url_for, request


# configure application
app = Flask(__name__)
app.secret_key = "Final Project!"

# set language to default

# this function expects a language keyword argument
def lang_select(f):
    def wrapper(*args, **kwargs):
        print("start")
        if "language" not in session:
            session["language"] = "en-us"
            with open(f"translations/en-us.json", "r", encoding="utf-8") as file:
                page_data = json.load(file)
        elif "language" not in kwargs:
            with open("translations/en-us.json", "r", encoding="utf-8") as file:
                page_data = json.load(file)
        else:
            session["language"] = kwargs["language"]
            with open(f"translations/{session.get("language")}.json", "r", encoding="utf-8") as file:
                page_data = json.load(file)
        rv = f(page_data)
        print("end")
        return rv
    return wrapper


@app.route("/")
@app.route("/<language>/")
@lang_select
def index(render_data):
    return render_template("index.html", content_title=render_data["index_title"], content_body=render_data["index_body"])


if __name__ == "__main__":
    app.run(debug=True)
