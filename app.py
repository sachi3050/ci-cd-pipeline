from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
<<<<<<< HEAD
    return "Happy BirthDay Abhishek Bhaina. Haste rahiye muskurate rahiye, All the Very Best......"
=======
    return '''
    <h2>Happy Birthday Abhishek Bhaina!</h2>
    <p>Haste rahiye, muskurate rahiye, All the Very Best...</p>
    <img src="/static/image.jpg" alt="Birthday Image" width="400">
    '''
>>>>>>> 032db44 (Staged unstaged changes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

