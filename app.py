from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Honey : My Brest Friend, Whould You wanna Join Tonight"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

