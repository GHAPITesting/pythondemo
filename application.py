from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello New World! from GitHub Actions"

# run the app.
if __name__ == "__main__":
    application.run(host="0.0.0.0",port="5000")
