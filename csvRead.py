import pandas
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
"""
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
"""

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="membAnalysis"
)
#checking it connects to the database
#print("Successfully connected to MySQL!")

SQLcursor = connection.cursor();
#connection variable

"""SQL = ""INSERT INTO members (member_id, first_name, last_name, age, email, member_since, membership_status, membership_level) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""

print("Rows in dataframe:", len(customerData))

values = [];

for _, row in customerData.iterrows(): 
   values.append((int(row['member_id']), row['first_name'], row['last_name'], int(row['age']), row['email'], row['member_since'].date(), row['membership_status'], row['membership_level']))


tierSQL = ""
INSERT INTO membTiers (
    tier_name,
    monthly_price,
    pContent_access,
    discount_access,
    pApp_access,
    helper_access
)
VALUES (%s, %s, %s, %s, %s, %s)
""
tierValues = []
for _, row in membershipData.iterrows():
    tierValues.append((
        row["membership_tier"],
        float(row["monthly_cost"]),
        row["pContent_access"],
        row["discount_access"],
        row["pApp_access"],
        row["helper_access"]
    ))


SQLcursor.executemany(tierSQL, tierValues)
SQLcursor.executemany(SQL, values)
print("Rows processed:", SQLcursor.rowcount)
"""
query = """SELECT
    t.tier_name AS MembershipTier,
    COUNT(m.member_id) AS MemberCount
FROM membTiers t
LEFT JOIN members m
    ON m.tier_id = t.tier_id
GROUP BY t.tier_id, t.tier_name"""

SQLcursor.execute(query)
results = SQLcursor.fetchall()
for row in results:
    tier = row[0]
    count = row[1]
    print(f"{tier}: {count} members")

#connection.commit()
# commit the additions to the database
#print("Data committed")
