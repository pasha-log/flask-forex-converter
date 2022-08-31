from flask import Flask, request, render_template, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", 'fjkdsgs')
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

c = CurrencyRates()

@app.route("/", methods=['POST']) 
def main_page():
     
    return render_template('base.html') 


