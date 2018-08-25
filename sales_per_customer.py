"""This module takes two csv customer and sales as input and returns the report sales_per_customer"""

import csv

CUSTOMER_CSV_FILE ='customers.csv'
SALES_CSV_FILE ='sales.csv'




class SalesPerCustomer:


    """This module takes two csv customer and sales as input and returns the report sales_per_customer"""

    def __init__(self, customer_csv_file, sales_csv_file):
        self.sales_csv_file = sales_csv_file
        self.customer_csv_file = customer_csv_file


    def read_csv_file(filename):
        with open(filename, newline ='')  as csv_file:
            csv_table = []
            csv_reader = csv.reader(csv_file,delimiter =',')
            for row in csv_reader:
                csv_table.append(row)
        return(csv_table)



    def merge_sales_and_customer_files(self,customer_csv_file,sales_csv_file):
        # Read the customer file
        print("Step 1: Reading Customer file")
        cust_table = SalesPerCustomer.read_csv_file(customer_csv_file)
        rows = len(cust_table)
        print("Step 1: Successfully read " +str(rows)+" rows from the Customer file")
        #Read the sales file
        print("Step 2: Reading Sales file")
        sales_table = SalesPerCustomer.read_csv_file(sales_csv_file)
        rows = len(sales_table)
        print("Step 3: Successfully read " +str(rows)+" rows from the Sales file")


        # Grab the index of customer id column in the customer table
        cust_key_ind= cust_table[0].index("customer_id")

        # Grab the index of customer id column in the sales table
        sales_key_ind = sales_table[0].index("customer_id")

        # Grab the index of quantity column in the customer table
        quantity_index = sales_table[0].index("quantity")
        print("Step 4: Started merging customer and sales table")

        output_table = []

        dict_a ={}
        for sales_row in sales_table:
            key=sales_row[0]
            if key!= 'customer_id':
                value=int(sales_row[-1])
                if key in dict_a:
                    dict_a[key]= dict_a.get(key, 0) + value
                else:
                    dict_a[key] = value
        print(dict_a)

        count, sum_quantity = 0,0
        for cust_row in cust_table:
            result = None
            cust_id=cust_row[cust_key_ind]
            if count == 0:
                header="sum(quantity)"
                result = cust_row + list([header])
            else:
                if cust_id in dict_a:
                    sum_quantity = dict_a[cust_id]
                    result = cust_row + list([sum_quantity])
            count+=1

        #append the result in the final output
            if result is not None:
                output_table.append(result)
        print(output_table)
        return (output_table)

        # for cust_row in cust_table:
        #     count,sum_quantity,result= 0,0,None
        #     for sales_row in sales_table:
        #         if cust_row[cust_key_ind] == sales_row[sales_key_ind]:
        #             curr_quantity = sales_row[quantity_index]
        #         #Header row to be added only once
        #             if count == 0:
        #                 header="sum(" +curr_quantity +")"
        #                 result = cust_row + list([header])
        #             else:
        #                 sum_quantity += int(curr_quantity)
        #                 result = cust_row + list([sum_quantity])
        #         count+=1
        #
        # #append the result in the final output
        #     if result is not None:
        #         output_table.append(result)
        #
        # rows  = len(output_table)
        # print("Step 5: The final output has "+str(rows)+" rows")
        # return(output_table)


    def create_output_file(self,output_table):

        with open("sales_per_customer.csv", "w") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(output_table)


        csvFile.close()
        return("Sucessfully created sales_per_customer.csv")




if __name__ == "__main__":

    try:

        files=SalesPerCustomer(CUSTOMER_CSV_FILE, SALES_CSV_FILE)
        output_table=files.merge_sales_and_customer_files(CUSTOMER_CSV_FILE, SALES_CSV_FILE)

        MESSAGE = files.create_output_file(output_table)
        print(MESSAGE)

    except Exception as exp:
        raise(exp)