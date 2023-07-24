import datetime
import pytest
import csv
import tempfile
from customer import show_all_customers, write_csv
from io import StringIO


def test_write_csv():

    headers = ["Name", "Age", "Country"]
    data = [
        ["Donald Trump", "77", "USA"],
        ["Vladímir Putin", "70", "Russia"],
    ]

                                                                                
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        file_name = temp_file.name

        write_csv(file_name, headers, data)

       
        with open(file_name, 'r') as csv_file:
            reader = csv.reader(csv_file)
            read_data = list(reader)
        
        assert read_data[0] == headers
        assert read_data[1:] == data


def test_show_all_customers():
    headers = ["Name", "Customer Number", "Age", "Gender", "Email", "Address", "Phone", "Country", "State", "City", "Zip Code"]
    data = [
        ["John Doe", "1", 30, "Male", "john@example.com", "123 Main St", "1234567890", "USA", "California", "Los Angeles", "90001"],
        ["Joseph Smith", "2", 25, "Female", "jo.smith@example.com", "456 Seven St", "9876543210", "USA", "Vermont", "Sharon", "05065"],
    ]
    
    print("Running test for show_all_customers...")
    print()
    
    show_all_customers(headers, data)
    
    print()
    print("Test complete.")

pytest.main(["-v", "--tb=line", "-rN", __file__])