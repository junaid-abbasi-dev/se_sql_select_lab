import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')


df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName FROM employees;
""", conn).head(23)


df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber FROM employees
""", conn).head(23)


df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID FROM employees;
""", conn)

# product_data = pd.read_sql("""
# SELECT productName, productLine AS planes
#   CASE productLine
#     WHEN productLine = 'planes' 
#     THEN productLine = 'planes'
#     ELSE 'Not Planes'
#   FROM products;

df_executive = pd.read_sql("""
    SELECT jobTitle AS role, 
        CASE 
            WHEN jobTitle = "President"
            OR jobTitle = "VP Sales"
            OR jobTitle = "VP Marketing"
            THEN "Executive"
            ELSE "Not Executive"
        END
    FROM employees;
""", conn).head(5)


df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) as name_length FROM employees;
""", conn)


df_short_title = pd.read_sql("""
    SELECT substr(jobTitle, 0, 3) AS short_title FROM employees;
""", conn)


sum_total_price = pd.read_sql("""
    SELECT round(priceEach * quantityOrdered) AS total_amount FROM orderDetails;
""", conn).sum()

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql("""
    SELECT orderDate,
        STRFTIME('%d', orderDate) AS day,
        STRFTIME('%m', orderDate) AS month,
        STRFTIME('%Y', orderDate) AS year
    FROM orders;
""", conn)



order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn) 
# print("------------------Order Details Data------------------")
# print(order_details)
# print("----------------End Order Details Data----------------")

# print("total price")
# print(sum_total_price)

print(df_day_month_year)