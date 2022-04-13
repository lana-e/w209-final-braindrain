from flask import Flask, render_template
import json
app = Flask(__name__)

# read file
with open('./static/dashboard-lana.json', 'r') as spec_lana:
    dash_lana = spec_lana.read()

with open('./static/dashboard-li.json', 'r') as spec_li:
    dash_li = spec_li.read()

@app.route("/")
def index():
    return render_template("index.html", dash_lana=dash_lana, dash_li=dash_li)

if __name__ == "__main__":
    app.run()
