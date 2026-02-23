#import psycopg2
import psycopg2

#connect to the postgres database

conn=psycopg2.connect(
    host='localhost',
    user='postgres',
    port=5432,
    dbname='myduka_db',
    password='Adoshcamp'

)
#declare cursor to perform database operations

curr=conn.cursor()

#database operations
def fetch_products():

    curr.execute('Select * from products;')
    prods=curr.fetchall()
    return prods
#myproducts=fetch_products()
#print(myproducts)

#display sales on the terminal
def fetch_sales():

    curr.execute('select * from sales;')
    sales=curr.fetchall()
    return sales
#mysales=fetch_sales()
#print(mysales)

#display stock on the terminal
def fetch_stocks():

    curr.execute('select * from stock;')
    stocks=curr.fetchall()
    return stocks
#mystocks=fetch_stocks()
#print(mystocks)

def fetch_data(table_name):
    curr.execute(f'select * from {table_name}')
    data=curr.fetchall()
    return data
#myproducts=fetch_data('products')
#print(myproducts)
#mysales=fetch_data('sales')
#print(mysales)
#mystock=fetch_data('stock')
#print(mystock)

def insert_stock(values):
    query='insert into stock (pid,stock_quantity) values(%s,%s)'
    curr.execute(query,values)
    conn.commit()

new_stock=(4,30)   
#insert_stock(new_stock) 
#mystocks=fetch_stocks()
#print(mystocks)


#insert products
def insert_products(values):
    query='insert into products(name,buying_price,selling_price)values(%s,%s,%s)'
    curr.execute(query,values)
    conn.commit()

new_product=('orange',200,400)
#insert_products(new_product)
#myproducts=fetch_products()
#print(myproducts)


#insert sales
def insert_sales(values):
    query='insert into sales(pid,quantity,created_at)values(%s,%s,now())'
    curr.execute(query,values)
    conn.commit()

new_sale=(2,5)
#insert_sales(new_sale)
#mysales=fetch_sales()
#print(mysales)


def product_profit():
    query=' select p.id,p.name,sum((p.selling_price-p.buying_price)*s.quantity) as total_profit from products as p inner join sales as s on p.id=s.pid group by p.id,p.name;'
    curr.execute(query)
    profit=curr.fetchall()
    return profit
#myprofits=product_profit()
#print(f'my products profit is{myprofits}')


def product_sales():
    query='select p.name,p.id,s.id,sum(p.selling_price *s.quantity) as total_sales from products as p inner join sales as s on p.id=s.pid group by p.name,p.id,s.id;'
    curr.execute(query)
    sales=curr.fetchall()
    return sales
#mysale=product_sales()
#print(f'my product sales is {mysale}')


def total_sales():
    query=' select sum(quantity*selling_price) as total_sales from products as p inner join sales as s on p.id=s.pid;'
    curr.execute(query)
    sale=curr.fetchone()
    return sale[0]

    
#mytotal=total_sales()
#mytotal=(mytotal)
#print(f'my total sale is ({mytotal}')

#total profit
def total_profit():
    query=' select sum(total_profit) as total_profit from(select p.id, sum((p.selling_price - p.buying_price)*s.quantity) as total_profit from products as p join sales as s on p.id=s.pid group by p.id);'
    curr.execute(query)
    profit=curr.fetchone()
    return profit[0]
#profit per product
def get_profit():
    query='select p.name,p.id, sum((p.selling_price - p.buying_price)* s.quantity) as profits from products as p join sales as s on p.id=s.pid group by p.name,p.id;'
    curr.execute(query)
    profits=curr.fetchall()
    return profits
profit=get_profit()
#print(f'my profit is{profit}')

#sales per product
def get_sale():
    query=' select p.name, sum(quantity*selling_price) as total_sales from products as p inner join sales as s on p.id=s.pid group by p.name;'
    curr.execute(query)
    sales=curr.fetchall()
    return sales
#sale=get_sale()
#print(f'my sales per product is {sale}')


#sales per day
def sales_day():
    query='select DATE(s.created_at) as day, sum(p.selling_price*s.quantity) from products as p join sales as s on p.id=s.pid group by DATE(s.created_at);'
    curr.execute(query)
    data=curr.fetchall()
    return data
#dsale=sales_day()
#print(dsale)

#profit per day
def profit_day():
    query='select DATE(s.created_at) as day, sum((p.selling_price - p.buying_price)*s.quantity) from products as p join sales as s on p.id=s.pid group by DATE(s.created_at);'
    curr.execute(query)
    data1=curr.fetchall()
    return data1
#total profit per day
def tprofit_day():
    query=' select  sum((p.selling_price - p.buying_price)*s.quantity) from products as p join sales as s on p.id=s.pid where DATE(s.created_at)=CURRENT_DATE'
    curr.execute(query)
    data2=curr.fetchone()
    return data2 [0]

#TOTAL SALE PER DAY
def tsale_day():
    query='select sum(p.selling_price*s.quantity) from products as p join sales as s on p.id=s.pid where DATE(s.created_at)=CURRENT_DATE;'
    curr.execute(query)
    data3=curr.fetchone()
    return data3 [0]

def month():
    query='select DISTINCT  Extract(month from s.created_at) as month_name from sales as s;'
    curr.execute(query)
    data4=curr.fetchall()
    return data4

def insert_users(values):
    query='insert into users(full_name,email,password) values(%s,%s,%s)'
    curr.execute(query,values)
    conn.commit()

def check_email(email):
    query='select * from users where email=%s'
    #the comma and brackests makes the email a tuple
    curr.execute(query,(email,))
    data=curr.fetchone()
    return data


def update_product(a,b,c,d):
    query="update products set name=%s, buying_price=%s, selling_price=%s where id=%s"
    curr.execute(query,(a,b,c,d))
    conn.commit()

def update_sales(a,b):
    query="update sales set quantity=%s where id=%s"
    curr.execute(query,(a,b))
    conn.commit()   


def recent_sales():
    query='select s.id,p.name,s.created_at from sales as s join products as p on p.id=s.pid group by p.name,s.id,p.id order by created_at desc limit 10;'
    curr.execute(query)
    data4=curr.fetchall()
    return data4    

def top_selling():
    query=' select p.name,p.id,count (s.id) from sales as s join products as p on p.id=s.pid group by p.name, p.id order by count(s.id) desc limit 10 ;'
    curr.execute(query)
    data5=curr.fetchall()
    return data5


def update_stock(a,b):
    query="update stock set stock_quantity=%s where id=%s"
    curr.execute(query,(a,b))
    conn.commit()  


    







