from flask import Flask, render_template


# configure application
app = Flask(__name__)
app.secret_key = "Final Project!"


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
