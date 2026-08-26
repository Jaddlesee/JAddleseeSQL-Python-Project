import pandas
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

pandas.options.display.max_rows = None

customerData = pandas.read_csv('D:\\SQL-Python-Project\\JAddleseeSQL-Python-Project\\mockdata\\Customers.csv')
#bringing in customer data from csv file

membershipData = pandas.read_csv('D:\\SQL-Python-Project\\JAddleseeSQL-Python-Project\\mockdata\\Membership_Values.csv')
#bringing in membership data from csv file

if customerData["member_id"].duplicated().any():
    raise ValueError("Duplicate membership IDs")
#validating that there are no dupes

if (customerData["age"] < 0).any():
    raise ValueError("Invalid age values")
#validating that there are no negative ages

customerData["member_since"] = pandas.to_datetime(customerData["member_since"], format='%Y/%m/%d')
#python recognises the date format as a string so this manually converts it to a date format

# print(customerData.dtypes)
# type check

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="membAnalysis"
)

print("Successfully connected to MySQL!")

SQLcursor = connection.cursor();
SQL = """INSERT INTO members (member_id, first_name, last_name, age, email, member_since, membership_status, membership_level) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

print("Rows in dataframe:", len(customerData))

values = [];

for _, row in customerData.iterrows(): 
   values.append((int(row['member_id']), row['first_name'], row['last_name'], int(row['age']), row['email'], row['member_since'].date(), row['membership_status'], row['membership_level']))

SQLcursor.executemany(SQL, values)
print("Rows processed:", SQLcursor.rowcount)


connection.commit()

print("Data committed")
