from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return '''
    <h2>Happy Birthday Abhishek Bhaina!</h2>
    <p>Haste rahiye, muskurate rahiye, All the Very Best...</p>
    <img src="/static/image.jpg" alt="Birthday Image" width="400">
    '''

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
