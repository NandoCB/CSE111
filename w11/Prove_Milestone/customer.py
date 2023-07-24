import csv
import datetime

################################################################################
# read_csv(): This function reads the contents of a CSV file
# returns the headers and data as separate lists.
################################################################################
def read_csv(file_name):
    try:
        with open("C:/Users/Fernando Cardozo/OneDrive/BYU/Web & Computer Programming/Spring 2023/CSE111/w11/Prove_Milestone/customer_data.csv", 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            headers = next(reader)                                              # Read CSV file headers
            data = list(reader)                                                 # Read data from CSV file into a list of lists
            return headers, data
    except FileNotFoundError:
        raise Exception("Invalid file/Database error")

################################################################################
# write_csv() – Writes headers and data to a CSV file. 
# uses the `csv` module to write the data to the file.
################################################################################

def write_csv(file_name, headers, data):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

################################################################################
# add_new_customer(): adds a new customer to the data list
################################################################################

def add_new_customer(headers, data):
    name = input("Name: ")
    address = input("Address: ")
                                                                             
    while not name or not address:                                             # Check if the name and address have been entered
        print("Name and address are required fields. Please try again.")
        name = input("Name: ")
        address = input("Address: ")
                                                                             
    customer_numbers = [int(row[1]) for row in data if row[1].isdigit()]                 # Gets the next available sequential number
    customer_number = str(max(customer_numbers) + 1) if customer_numbers else "1"
    
    age = input("Age: ")
    gender = input("Gender: ")
    email = input("E-mail: ")
    phone = input("Phone: ")
    country = input("Country: ")
    state = input("State: ")
    city = input("City: ")
    zip_code = input("Zip Code: ")
    
    ###### Verification of the data type for each field ######
    try:
        age = int(age)
    except ValueError:
        age = None
       
    while "@" not in email:                                                                         #email format
        print("Invalid email. Please enter a valid email address.")
        email = input("E-mail: ")
    
    valid_phone = False                                                                             #phone number format
    while not valid_phone:
        if all(char.isdigit() or char in ['+', '(', ')'] for char in phone):
            valid_phone = True
        else:
            print("Invalid phone number. Please enter only digits, +, or () are accepted.")
            phone = input("Phone: ")
     
    while not country.isalpha():                                                                    #Verify that the entered country 
        print("Invalid country name. Please enter only alphabetic characters.")                     #only contains letters
        country = input("Country: ")
    
    print("Customer added successfully!")
    new_customer = [name, customer_number, age, gender, email, address, phone, country, state, city, zip_code]
    data.append(new_customer)
    return new_customer

################################################################################
#delete_existing_customer(): deletes an existing customer from the data list
# based on their name and customer number.
################################################################################

def delete_existing_customer(headers, data):
    delete_name = input("Name: ")
    delete_customer_number = input("Customer Number: ")
    
    if not delete_name or not delete_customer_number:
        print("Unable to delete customer. Both name and customer number are required.")
        return data
    
    updated_data = []
    deleted_customer = None
    for row in data:                                                             # Check if customer name and number 
        if row[0] == delete_name and row[1] == delete_customer_number:           # have been entered
            deleted_customer = row           
            continue  # Skip the customer you want to delete
        updated_data.append(row)
    
    if deleted_customer:
        print("Customer deleted successfully!")
    else:
        print("Customer not found.")
    return updated_data, deleted_customer

################################################################################
# search_customer(): searches for a customer 
# based on their name, customer number, or phone number.
################################################################################
def search_customer(headers, data):
    search_name = input("Name: ")
    search_customer_number = input("Customer Number: ")
    search_phone = input("Phone: ")
    print()
    
    results = []
    for row in data:
        if (search_name and row[0] == search_name) or \
           (search_customer_number and row[1] == search_customer_number) or \
           (search_phone and row[6] == search_phone):
            results.append(row)

    if results:
        print("{:<20} {:<15} {:<10} {:<10} {:<30} {:<20} {:<15} {:<15} {:<15} {:<15} {:<10}".format(*headers))
        for row in results:
            print("{:<20} {:<15} {:<10} {:<10} {:<30} {:<20} {:<15} {:<15} {:<15} {:<15} {:<10}".format(*row))
        
    else:
        print("No matching customers found.")
        print()  

################################################################################
#show_all_customers(): Displays all the customer records in a formatted manner.
################################################################################
def show_all_customers(headers, data):
    current_date_and_time = datetime.datetime.now()
    print()
    print("All Customers:")
    print()
    
    print("{:<20} {:<15} {:<10} {:<10} {:<30} {:<35} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*headers))
    for row in data:
        name, customer_number, age, gender, email, address, phone, country, state, city, zip_code = row
        print("{:<20} {:<15} {:<10} {:<10} {:<30} {:<35} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            name, customer_number, age, gender, email, address, phone, country, state, city, zip_code
        ))
    print()
    print("Total Customers:", len(data))
    print(f"{current_date_and_time:%d/%m/%Y %H:%M:%S}")
    print()

################################################################################
#edit_existing_customer(): Allows the user to edit an existing customer's details.
################################################################################
def edit_existing_customer(headers, data):
    edit_name = input("Name: ")
    edit_customer_number = input("Customer Number: ")

    if not edit_name or not edit_customer_number:                                                   #Check if customer name and number 
        print("Unable to edit customer. Both name and customer number are required.")               #have been entered
        return data

    customer_found = False
    for row in data:
        if row[0].lower() == edit_name.lower() and row[1] == edit_customer_number:
            customer_found = True
            print("Current customer details:")
            print("Name:", row[0])
            print("Customer Number:", row[1])
            print("Age:", row[2])
            print("Gender:", row[3])
            print("E-mail:", row[4])
            print("Address:", row[5])
            print("Phone:", row[6])
            print("Country:", row[7])
            print("State:", row[8])
            print("City:", row[9])
            print("Zip Code:", row[10])

            field = input("Select field to update (Name, Age, Gender, E-mail, Address, Phone, Country, State, City, Zip Code): ")
            if field.lower() == "name":
                row[0] = input("New Name: ")
            elif field.lower() == "age":
                row[2] = input("New Age: ")
            elif field.lower() == "gender":
                row[3] = input("New Gender: ")
            elif field.lower() == "e-mail":
                row[4] = input("New E-mail: ")
            elif field.lower() == "address":
                row[5] = input("New Address: ")
            elif field.lower() == "phone":
                row[6] = input("New Phone: ")
            elif field.lower() == "country":
                row[7] = input("New Country: ")
            elif field.lower() == "state":
                row[8] = input("New State: ")
            elif field.lower() == "city":
                row[9] = input("New City: ")
            elif field.lower() == "zip code":
                row[10] = input("New Zip Code: ")
            else:
                print("Invalid field. No changes made.")

            write_csv(file_name, headers, data)                                     # Save the changes to the CSV file
            
            print("Client modified successfully")
            break

    if not customer_found:
        print("Customer not found.")

    return data

file_name = "customer_data.csv"
headers, data = read_csv(file_name)

################################################################################
#main(): Entry point of the program.
################################################################################

def main():
    while True:
        print("*********************************************************************")
        print("************************ Client Base Manager ************************")
        print("*********************************************************************")
        print()
        print("1. Add new customer")
        print("2. Search customer")
        print("3. Show all customers")
        print("4. Delete existing customer")
        print("5. Edit existing customer")
        print("6. Exit")
        print()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            new_customer = add_new_customer(headers, data)
            #data.append(new_customer)
            write_csv(file_name, headers, data)
        elif choice == "2":
            search_customer(headers, data)  
        elif choice == "3":
            show_all_customers(headers, data)
        elif choice == "4":
            delete_existing_customer(headers, data)
        elif choice == "5":
            edit_existing_customer(headers, data)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()