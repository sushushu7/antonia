from flask import Flask, render_template
import random

app = Flask(__name__)

welcome_words = ["lovely", "marvelous", "spectacular",
                 "splendid", "wonderful", "grand",
                 "phenomenal", "fabulous", "divine",
                 "terrific", "glorious", "sensational",
                 "striking", "awe-inspiring", "astounding",
                 "bewildering", "stupendous", "tremendous",
                 "peachy", "brilliant", "bodacious",
                 "dandy", "fantabulous", "magnificent",
                 "stellar", "exceptional", "noble",
                 "thrilling", "elite", "crucial",
                 "vital", "essential", "exclusive"]


@app.route('/')
def home():
    welcome = random.choice(welcome_words)
    return render_template("index.html", welcome=welcome)


if __name__ == "__main__":
    app.run(debug=True)
