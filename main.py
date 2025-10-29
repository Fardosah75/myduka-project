#import the class Flask from the framework flask
from flask import Flask,render_template,request,redirect,url_for
from database import fetch_data,insert_products,insert_sales,insert_stock
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
    #1.fetch products on the sales route for select element(part1.select element)
    product=fetch_data('products')
    #print (sale)
    #2.pass the variable in reneder_template function(part 2.select element)
    return render_template ('sales.html',sale=sale, products=product)

#create a route that receives data from the form using a method
@app.route('/add_sales',methods=['GET','POST'])
#create the function to receive data from the modal on the form
def add_sales():
    #check the method
    if request.method=='POST':
        #get the inputs from the form using name attributes and store them in a variable
        #3.get the id(part 3 select element)
        pid=request.form['pid']
        quant=request.form['quantity']

        #store the new sales in a variable
        new_sales=(pid,quant)
        # import from database.py &call the insert function to insert into the database
        insert_sales(new_sales)
        #redirect to the product page to see the inserted value
    return redirect(url_for('sales'))    






@app.route('/stocks')
def stock():
    stocks=fetch_data('stock')
    #print(stocks)
    return render_template ('stock.html',stocks=stocks)

#create a route that will receive data from the form to serverside with method
@app.route('/add_stocks',methods=['GET','POST'])

#create a function to receive data from the form on the modal
def add_stock():
    #check the method
    if request.method=='POST':
        #get the form inputs using the name attribute and store them in a variable
        pid=request.form['pid']
        stock_quantity=request.form['s_quantity']

        #store them in a variable
        new_stock=(pid,stock_quantity)
        #import the insert stock  function from database.py and call the function
        insert_stock(new_stock)
      #return/redirect the page to stock page by passing the function to fetch data for stock
    return redirect(url_for('stock'))    



app.run(debug=True)