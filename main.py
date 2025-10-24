#import the class Flask from the framework flask
from flask import Flask,render_template
from database import fetch_data
#instance of the class(object)
app=Flask(__name__)

#creating a route
@app.route('/')
def home():
    return render_template ('index.html')

@app.route('/products')
def products():
    prods=fetch_data('products')
    
    return render_template ('products.html',product=prods)

@app.route('/sales')
def sales():
    sale=fetch_data('sales')
    #print (sale)
    return render_template ('sales.html',sale=sale)
@app.route('/stocks')
def stock():
    stocks=fetch_data('stock')
    #print(stocks)
    return render_template ('stock.html',stocks=stocks)

app.run()