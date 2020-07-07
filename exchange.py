from flask import Flask, render_template
import bkdb

app = Flask(__name__)

@app.route("/")
def hello():
    dt = bkdb.data()
    mon = bkdb.view("EUR")
    items=[mon, dt]
    return render_template("home.html", items=items)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
