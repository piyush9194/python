import pytest
from sales_per_customer import SalesPerCustomer


def test_merge_sales_and_customer_files():
    customer_csv_file = 'customers.csv'
    sales_csv_file = 'sales.csv'

    files = SalesPerCustomer(customer_csv_file,sales_csv_file)
    dst = files.merge_sales_and_customer_files(customer_csv_file,sales_csv_file)
    print(dst)
    expected = [['customer_id', 'name', 'email', 'address', 'sum(quantity)'],
                ['1', 'Rike Weiss', 'rike.weiss@email.com', 'Berlinerstraße 1', 14],
                ['2', 'Max Musterman', 'max.musterman@email.com', 'Berlinerstraße 1', 5],
                ['3', 'Hildegard Hartmann', 'hildegard.hartmann@email.com', 'Torstraße 25', 7],
                ['4', 'Kora Schegtel', 'kora.schegtel@email.com', 'Oranienstraße 10', 1]]

    assert dst == expected


class test_some_stuff():
    test_merge_sales_and_customer_files()
