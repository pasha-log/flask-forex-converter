from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import (CurrencyRates, CurrencyCodes, RatesNotAvailableError)
from decimal import Decimal
from functions import currencies, check_if_valid_currency_code, calculate_conversion_and_check_amount
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", 'fjkdsgs')
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

@app.route("/") 
def main_page():
    """Brings client to home page with forex form"""
    
    return render_template('base.html') 

@app.route("/", methods=["POST"]) 
def conversion_page():
    """Handles conversion_result and error messages"""
    symbol = CurrencyCodes()
    currency_from = str(request.form['currency_from'])
    currency_to = str(request.form['currency_to'])
    amount = request.form['amount']
    symbol = symbol.get_symbol(currency_to)
    print(request.form)
    check_if_valid_currency_code(currency_from, currency_to)
    calculate_conversion_and_check_amount(currency_from, currency_to, amount, symbol)
    return redirect('/') 



