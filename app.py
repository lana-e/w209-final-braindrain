from flask import Flask, render_template
import json
app = Flask(__name__)

# read file
with open('./static/dashboard-lana.json', 'r') as spec_lana:
    dash_lana = spec_lana.read()

with open('./static/dashboard-li-jpn.json', 'r') as spec_li_jpn:
    dash_li_jpn = spec_li_jpn.read()
    
with open('./static/dashboard-li-usa.json', 'r') as spec_li_usa:
    dash_li_usa = spec_li_usa.read()

@app.route("/")
def index():
    return render_template("index.html", dash_lana=dash_lana, dash_li_jpn=dash_li_jpn, dash_li_usa=dash_li_usa)

if __name__ == "__main__":
    app.run()
