from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Happy BirthDay Abhishek Bhaina. Haste rahiye muskurate rahiye, All the Very Best......"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

