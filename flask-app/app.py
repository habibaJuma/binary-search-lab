from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    return"Flask App!"

@app.route("/user/")
def hello():
    users = ["Habiba", "Juma","Khalid"]
    return render_template(
        'user.html', **locals())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

