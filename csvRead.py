import pandas

pandas.options.display.max_rows = None

customerData = pandas.read_csv('D:\\SQL-Python-Project\\JAddleseeSQL-Python-Project\\mockdata\\Customers.csv')

print(customerData.to_string())
