import json
from flask import Flask, jsonify, render_template


# configure application
app = Flask(__name__)
app.secret_key = "Final Project!"


@app.route("/")
def index():
    with open("translations/en-us.json", "r", encoding="utf-8") as file:
        content_dict = json.loads(file.read())
    return render_template("index.html", content_title=content_dict["index_main_title"], content_body=content_dict["index_main_body"])

if __name__ == "__main__":
    app.run(debug=True)
