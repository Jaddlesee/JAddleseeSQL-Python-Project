import pandas

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


print(customerData.dtypes)



