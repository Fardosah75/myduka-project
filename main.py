#import the class Flask from the framework flask
from flask import Flask,render_template,request,redirect,url_for
from database import fetch_data,insert_products
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

#create a route to add products/receive products from the ui to the serverside
@app.route('/add_products',methods=['GET','POST']) 
#create the function to receive data from the modal on the form 
def add_products():
    
    #check the method used,import request from flask
    if request.method=='POST':
        #get the inputs from the form using name attributes and store them in a variable
        pname=request.form['name']
        bp=request.form['buyingprice']
        sp=request.form['sellingprice']

        #store the new products in a variable
        new_product=(pname,bp,sp)
        # import from database.py &call the insert function to insert into the database
        insert_products(new_product)
        #redirect to the product page to see the inserted value
    return redirect(url_for('products'))


         


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

app.run(debug=True)