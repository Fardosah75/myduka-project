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
myproducts=fetch_products()
print(myproducts)

#display sales on the terminal
def fetch_sales():

    curr.execute('select * from sales;')
    sales=curr.fetchall()
    return sales
mysales=fetch_sales()
print(mysales)

#display stock on the terminal
def fetch_stocks():

    curr.execute('select * from stock;')
    stocks=curr.fetchall()
    return stocks
mystocks=fetch_stocks()
print(mystocks)

#def fetch_data(table_name):
   # curr.execute(f'select * from {table_name}')
    #data=curr.fetchall()
    #return data
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
mystocks=fetch_stocks()
print(mystocks)


#insert products
def insert_products(values):
    query='insert into products(name,buying_price,selling_price)values(%s,%s,%s)'
    curr.execute(query,values)
    conn.commit()

new_product=('orange',200,400)
#insert_products(new_product)
myproducts=fetch_products()
print(myproducts)


#insert sales
def insert_sales(values):
    query='insert into sales(pid,quantity,created_at)values(%s,%s,now())'
    curr.execute(query,values)
    conn.commit()

new_sale=(2,5)
#insert_sales(new_sale)
mysales=fetch_sales()
print(mysales)


def product_profit():
    query=' select p.id,p.name,sum((p.selling_price-p.buying_price)*s.quantity) as total_profit from products as p inner join sales as s on p.id=s.pid group by p.id,p.name;'
    curr.execute(query)
    profit=curr.fetchall()
    return profit
myprofits=product_profit()
print(f'my products profit is{myprofits}')


def product_sales():
    query='select p.name,p.id,s.id,sum(p.selling_price *s.quantity) as total_sales from products as p inner join sales as s on p.id=s.pid group by p.name,p.id,s.id;'
    curr.execute(query)
    sales=curr.fetchall()
    return sales
mysale=product_sales()
print(f'my product sales is {mysale}')
