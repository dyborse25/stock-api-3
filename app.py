from flask import Flask, jsonify, request
from flask_cors import CORS
import yfinance as yf
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/price', methods=['GET'])
def get_price():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'Missing symbol'}), 400

    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1d")
        price = hist['Close'].iloc[-1]
        return jsonify({'symbol': symbol, 'price': round(price, 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
