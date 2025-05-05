from flask import Flask
app = Flask('kettle')

@app.route("/")
def hello():
    return "Hello, Docker World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
