# app.py
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def show_orders():
    df = pd.read_csv('orders.csv')  # Assuming Function saved it here
    orders = df.to_dict(orient='records')
    return render_template('orders.html', orders=orders)

if __name__ == '__main__':
    app.run()
