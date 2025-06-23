from flask import Flask

app = Flask(__name__)

TAG = "fargate"

@app.route("/")
def home():
    return f"Hello Gwangju!", 200

@app.route("/health")
def health():
    return "OK", 200

@app.route("/tag")
def tag():
    return TAG, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

