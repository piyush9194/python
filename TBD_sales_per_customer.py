
with open("/Users/piygupta/Desktop/Pythonlearning/python_exercise/customers.csv") as customer_data:
    count = 0
    cust = []
    for row in customer_data:
        if count == 0:
            list_a = row.split(",")
            list_a[-1]=list_a[-1][:-1]
            count +=1
        else:
            record = row.split(",")
            i = 0
            dict_a = {}
            for item in list_a:

                if item == "address":
                    key,value  = item,str(record[i][:-1])
                else:
                    key, value = item, str(record[i])

                dict_a[key]=value
                i+=1
            cust.append(dict_a)

    print(cust)



with open("/Users/piygupta/Desktop/Pythonlearning/python_exercise/sales.csv") as sales_data:
    count = 0
    sales = []
    for row in sales_data:
        if count == 0:
            list_a = row.split(",")
            list_a[-1]=list_a[-1][:-1]
            count +=1
        else:
            record = row.split(",")
            i = 0
            dict_b = {}
            for item in list_a:

                if item == "quantity":
                    key,value  = item,str(record[i][:-1])
                else:
                    key, value = item, str(record[i])

                dict_b[key]=value
                i+=1
            sales.append(dict_b)

    print(sales)

    list_f = []
    for item in cust:

        cust_id = item['customer_id']
        cust_name = item['name']
        email = item['email']
        address = item['address']

        for element in sales:
            if element['customer_id'] == cust_id:
                quantity = element['quantity']
                value  = int(quantity)
                dict_c = {}
                dict_c['customer_id'] = cust_id
                dict_c['cust_name'] = cust_name
                dict_c['email'] = email
                dict_c['address'] = address
                dict_c['quantity']= value

                list_f.append(dict_c)


    print("result")
    print(list_f)

    [{'customer_id': '1', 'cust_name': 'Rike Weiss', 'email': 'rike.weiss@email.com', 'address': 'Berlinerstraße 1',
      'quantity': 10},
     {'customer_id': '1', 'cust_name': 'Rike Weiss', 'email': 'rike.weiss@email.com', 'address': 'Berlinerstraße 1',
      'quantity': 3},
     {'customer_id': '1', 'cust_name': 'Rike Weiss', 'email': 'rike.weiss@email.com', 'address': 'Berlinerstraße 1',
      'quantity': 1},
     {'customer_id': '2', 'cust_name': 'Max Musterman', 'email': 'max.musterman@email.com','address': 'Berlinerstraße 1',
      'quantity': 5},
     {'customer_id': '3', 'cust_name': 'Hildegard Hartmann', 'email': 'hildegard.hartmann@email.com','address': 'Torstraße 25',
      'quantity': 7},
     {'customer_id': '4', 'cust_name': 'Kora Schegtel', 'email': 'kora.schegtel@email.com','address': 'Oranienstraße 10',
      'quantity': 1}]



import csv
from collections import OrderedDict

with open('/Users/piygupta/Desktop/Pythonlearning/python_exercise/customers.csv') as f:
    r = csv.reader(f)
    dict2 = {row[0]: row[1:] for row in r}

print(dict2)

with open('/Users/piygupta/Desktop/Pythonlearning/python_exercise/sales.csv') as f:
    r = csv.reader(f)
    dict1 = OrderedDict((row[0], row[1:]) for row in r)



result = OrderedDict()
for d in (dict1, dict2):
    for key, value in d.iteritems():
        result.setdefault(key, []).extend(value)

print(result)


with open('ab_combined.csv', 'wb') as f:
    w = csv.writer(f)
    for key, value in result.iteritems():
        w.writerow([key] + value)

















