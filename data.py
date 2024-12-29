import streamlit as st
import mysql.connector
import pandas as pd





mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Naveen@123",
            database="retail_orders",
            autocommit=True
        )
mycursor = mydb.cursor(dictionary=True)
#st.success("Connected to the database successfully!")
        

st.title("RETAIL ORDER DATA ANALYSIS") 
st.subheader("Description:")
st.write("A retail data analysis project involves collecting and analyzing data from a retail business to gain insights that can help improve operations, customer experience, and profitability. ")
st.header("Asked Queries:")
  

mycursor.execute('use retail_orders')


if st.button("Query 1"):
     st.write("Find top 10 highest revenue generating products:")
     mycursor.execute('''SELECT data_2.product_id, SUM(data_2.sale_price * data_2.quantity) AS revenue
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY data_2.product_id
ORDER BY revenue DESC
LIMIT 10;
''')
     st.table(mycursor)  

     
if st.button("Query 2"):
    st.write("Find the top 5 cities with the highest profit margins:")
    mycursor.execute('''SELECT data_1.city, SUM(data_2.profit) AS total_profit
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY data_1.city
ORDER BY total_profit DESC
LIMIT 5;
    ''')
    st.table(mycursor)
if st.button("Query 3"):
    st.write("Calculate the total discount given for each category:")
    mycursor.execute('''SELECT data_1.category, SUM(data_2.discount) AS total_discount
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY data_1.category;
    ''')
    st.table(mycursor)

if st.button("Query 4"):
    st.write("Find the average sale price per product category:")
    mycursor.execute('''SELECT data_1.category, AVG(data_2.sale_price) AS avg_sale_price
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY data_1.category;
    ''')
    st.table(mycursor)

if st.button("Query 5"):
    st.write("Find the region with the highest average sale price:")
    mycursor.execute('''SELECT data_1.region, AVG(data_2.sale_price) AS avg_sale_price
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY data_1.region
ORDER BY avg_sale_price DESC
LIMIT 1;
    ''')
    st.table(mycursor)

if st.button("Query 6"):
    st.write("Find the total profit per category:")
    mycursor.execute('''SELECT data_1.category, SUM(data_2.profit) AS total_profit
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY data_1.category;
    ''')
    st.table(mycursor)

if st.button("Query 7"):
    st.write("Identify the top 3 segments with the highest quantity of orders:")
    mycursor.execute('''SELECT data_2.segment, SUM(data_2.quantity) AS total_quantity
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY data_2.segment
ORDER BY total_quantity DESC
LIMIT 3;
    ''')
    st.table(mycursor)

if st.button("Query 8"):
    st.write("Determine the average discount percentage given per region:")
    mycursor.execute('''SELECT data_1.region, AVG(data_2.discount_percent) AS avg_discount_percent
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY data_1.region;
    ''')
    st.table(mycursor)

if st.button("Query 9"):
    st.write("Find the product category with the highest total profit:")
    mycursor.execute('''SELECT data_1.category, SUM(data_2.profit) AS total_profit
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY data_1.category
ORDER BY total_profit DESC
LIMIT 1;
   ''' )
    st.table(mycursor)

if st.button("Query 10"):
    st.write("Calculate the total revenue generated per year:")
    mycursor.execute('''SELECT YEAR(data_1.order_date) AS year, 
       SUM(data_2.sale_price * data_2.quantity) AS total_revenue
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY YEAR(data_1.order_date)
ORDER BY YEAR(data_1.order_date);
    ''')
    st.table(mycursor)

st.header("Own Queries:")

if st.button("Query 11"):
    st.write("Find the top 5 lowest revenue generating products:")
    mycursor.execute('''SELECT data_2.product_id, SUM(data_2.sale_price * data_2.quantity) AS revenue
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY data_2.product_id
ORDER BY revenue ASC
LIMIT 5;''')
    st.table(mycursor)

if st.button("Query 12"):
    st.write("Find the top 5 cities with the lowest profit margins:")
    mycursor.execute('''SELECT data_1.city, SUM(data_2.profit) AS total_profit
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY data_1.city
ORDER BY total_profit ASC
LIMIT 5;
    ''')
    st.table(mycursor)

if st.button("Query 13"):
    st.write("Calculate the total discount given for each category:")
    mycursor.execute('''SELECT data_1.category, SUM(data_2.discount) AS total_discount
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY data_1.category;
    ''')
    st.table(mycursor)

if st.button("Query 14"):
    st.write("Find the average sale price per product category:")
    mycursor.execute('''SELECT data_1.category, AVG(data_2.sale_price) AS avg_sale_price
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY data_1.category;
   ''' )
    st.table(mycursor)

if st.button("Query 15"):
    st.write("Find the region with the lowest average sale price:")
    mycursor.execute('''SELECT data_1.region, AVG(data_2.sale_price) AS avg_sale_price
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY data_1.region
ORDER BY avg_sale_price ASC
LIMIT 1;
    ''')
    st.table(mycursor)

if st.button("Query 16"):
    st.write("Find the total profit for each category:")
    mycursor.execute('''SELECT data_1.category, SUM(data_2.profit) AS total_profit
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY data_1.category;
   ''' )
    st.table(mycursor)

if st.button("Query 17"):
    st.write("Identify the top 3 segments with the lowest quantity of orders:")
    mycursor.execute('''SELECT data_2.segment, SUM(data_2.quantity) AS total_quantity
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY data_2.segment
ORDER BY total_quantity ASC
   ''' )
    st.table(mycursor)

if st.button("Query 18"):
    st.write("Determine the average discount percentage given for total revenue:")
    mycursor.execute('''SELECT SUM(data_2.sale_price * data_2.quantity) AS total_revenue,
       AVG(data_2.discount_percent) AS avg_discount_percent
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id;
    ''')
    st.table(mycursor)

if st.button("Query 19"):
    st.write("Find the product category with the lowest total profit:")
    mycursor.execute('''SELECT data_1.category, SUM(data_2.profit) AS total_profit
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY data_1.category
ORDER BY total_profit ASC
LIMIT 1;
   ''' )
    st.table(mycursor)

if st.button("Query 20"):
    st.write("Calculate the total revenue generated per day:")
    mycursor.execute('''SELECT data_1.order_date, SUM(data_2.sale_price * data_2.quantity) AS total_revenue
FROM data_1
JOIN data_2 ON data_1.order_id = data_2.order_id
GROUP BY data_1.order_date
ORDER BY data_1.order_date;
    ''')
    st.table(mycursor)


























