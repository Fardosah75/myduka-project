#import the class Flask from the framework flask
from flask import Flask,render_template,request,redirect,url_for,session,flash
from database import fetch_data,insert_products,insert_sales,insert_stock,total_sales,total_profit,get_profit,get_sale,sales_day, profit_day,tprofit_day,tsale_day,month,insert_users,check_email,update_product,update_sales,recent_sales,top_selling,update_stock

from flask_bcrypt import Bcrypt

#instance of the class(object)
app=Flask(__name__)
#instance of the class-Bycrypt(object)
bycrypt=Bcrypt(app)
app.secret_key='remem2'

#creating a route
@app.route('/')
def home():


    return render_template ('index.html')

@app.route('/products')
def products():
    if 'email' in session:

        prods=fetch_data('products')
    else:
        flash('log in to access this page',"warning")    
        return redirect (url_for('log_in'))
    
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
        flash("product added successfully","info")
        #redirect to the product page to see the inserted value
    return redirect(url_for('products'))


@app.route('/update_products', methods=['GET', 'POST'])
def update_products():

    if request.method=='POST':
        #get the inputs from the form using name attributes and store them in a variable
        id=request.form['id']
        pname=request.form['name']
        bp=request.form['buyingprice']
        sp=request.form['sellingprice']


        update_product(pname,bp,sp,id)

        flash('product update successfully','success')

        return redirect(url_for('products'))
    return redirect(url_for('products'))






         


@app.route('/sales')
def sales():
    if 'email' in session:

        sale=fetch_data('sales')
        #1.fetch products on the sales route for select element(part1.select element)
        product=fetch_data('products')
        #print (sale)
        #2.pass the variable in reneder_template function(part 2.select element)
        return render_template ('sales.html',sale=sale, products=product)
    else:
        flash('log in to access this page',"warning")
        return redirect(url_for('log_in'))
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

@app.route('/update_sales',methods=['GET','POST'])
def update_sale():
    if request.method=='POST':
        id=request.form['id']
        quant=request.form['quantity']

        update_sales(quant,id)

        flash('sales quantity updated successfully')

        return redirect(url_for('sales'))
    return redirect(url_for('sales'))      






@app.route('/stocks')
def stock():
    if 'email' in session:

        stocks=fetch_data('stock')
        #1.on stock route fetch products
        products=fetch_data('products')
        #print(stocks)
        #2.pass the pvariable to render template
        return render_template ('stock.html',stocks=stocks,product=products)
    else:
        flash('log in to access this page','warning')
        return redirect(url_for('log_in'))
#create a route that will receive data from the form to serverside with method
@app.route('/add_stocks',methods=['GET','POST'])

#create a function to receive data from the form on the modal
def add_stock():
    #check the method
    if request.method=='POST':
        #get the form inputs using the name attribute and store them in a variable
        #get the name attribute for select element
        pid=request.form['pid']
        stock_quantity=request.form['s_quantity']

        #store them in a variable
        new_stock=(pid,stock_quantity)
        #import the insert stock  function from database.py and call the function
        insert_stock(new_stock)
      #return/redirect the page to stock page by passing the function to fetch data for stock
    return redirect(url_for('stock'))   

@app.route('/edit_stock', methods=['GET', 'POST'])
def update_stocks():
    if request.method=='POST':
        id=request.form['id']
        quant=request.form['s_quantity']
        print(quant)

        update_stock(quant,id)

        flash('stock quantity updated successfully')

        return redirect(url_for('stock'))
    return redirect(url_for('stock'))

    #create a route for dashboard
     

@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        rsales=recent_sales()
        tpp=top_selling()
        

        mytotal=total_sales()
        mytotal=float(mytotal)
        myprofit=total_profit()
        #profit per product
        profit=get_profit()
        #empty lists to store product name and profits
        product_names=[]
        product_profits=[]
        
        
        for i in profit:
            product_names.append(i[0])
            product_profits.append(float(i[2]))
    #sales per product
        sale=get_sale()
        print(sale)
        pname=[]
        sales=[]
        
        for i in sale:
            pname.append(i[0])
            sales.append(float(i[1]))


        #sales per day
        psale=sales_day()
        dates=[]
        dsale=[]
        for i in psale:
            dates.append(str(i[0]))
            dsale.append(float(i[1]))

        #profit per day
        pro_day=profit_day()
        date=[]    
        dprofit=[]

        for i in pro_day:
            date.append(str(i[0]))
            dprofit.append(float(i[1]))

        #total profit per day for the card
        tp_day=tprofit_day()    

        #total sale per day for the card
        ts_day=tsale_day()

        #month extract
        mo=month()
    else:
        flash('log in to access this page',"warning")    
        return redirect(url_for('log_in'))
        

    return render_template('dashboard.html',mytotal_sale=mytotal,myprofits=myprofit,profit=profit,pnames=product_names, pprofit=product_profits, dates=dates,dsale=dsale,date=date,dprofit=dprofit,pname=pname,sales=sales,tp_day=tp_day,ts_day=ts_day,mo=mo,rsales=rsales,tpp=tpp)

#log in route
@app.route('/login',methods=['GET','POST'])
def log_in():
    if request.method=='POST':
        mail=request.form['email']
        password=request.form['password']

        check=check_email(mail)
        if check==None:
            flash('Account not found.Register ',"danger")
            return redirect(url_for('register'))
        else:
            if bycrypt.check_password_hash(check[3],password):
              #adding email to session  
                session['email']=mail
                flash('log in successful', "success")
                return redirect(url_for('dashboard')) 
            else:
                flash('wrong email or password', "danger")
                return redirect(url_for('log_in'))    

    return render_template('login.html')


#register route
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form['f_name'] 
        mail=request.form['email']
        password=request.form['password']

        hashed_password=bycrypt.generate_password_hash(password).decode('utf-8')
        new_user=(name,mail,hashed_password)
        check=check_email(mail)
        if check==None:
            insert_users(new_user)
            flash('user registered successfully',"success")

            return redirect(url_for('log_in'))

        else:
            flash('user exists,use a different email or log in',"danger")    
            return redirect(url_for('register'))



    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('email',None)
    flash('you have been logged out',"info")

    return redirect(url_for("log_in"))
app.run(debug=True)

