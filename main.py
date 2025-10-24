#import the class Flask from the framework flask
from flask import Flask,render_template
#instance of the class(object)
app=Flask(__name__)

#creating a route
@app.route('/')
def home():
    return render_template ('index.html')

@app.route('/products')
def prods():
    return render_template ('products.html')

@app.route('/sales')
def sale():
    return render_template ('sales.html')
@app.route('/stocks')
def stock():
    return render_template ('stock.html')

app.run()