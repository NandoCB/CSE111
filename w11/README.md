CSE 111 Proposal for a Student Chosen Program
	
customer.py

2. What real-world problem will your program address or help to solve?

This program addresses the real-world problem of managing customer data in a business or organization. It provides various functions to add, search, display, edit, and delete customer records. By using this program, businesses can efficiently organize and manipulate customer information, enabling them to provide better customer service, targeted marketing, and data analysis.

Some specific problems that this program can help solve include:
A. Adding new customers: The program allows users to add new customer details, ensuring that essential information such as name, address, and contact details are entered correctly.
B. Searching for customers: Users can search for customers based on their name, customer number, or phone number. This helps in quickly retrieving customer information for various purposes, such as addressing customer inquiries or verifying customer details.
C. Displaying all customers: The program provides a function to display all customer records in a well-formatted manner. This enables users to have a comprehensive view of the customer base and easily access customer information when needed.
D. Deleting existing customers: Users can delete customer records from the database, ensuring that outdated or incorrect information is removed from the system.
E. Editing existing customers: The program allows users to update customer details, such as name, age, gender, contact information, and address. This helps in keeping customer information up to date and accurate.

Overall, this program provides a convenient and efficient way to manage customer data, leading to improved customer relationship management and enhanced business operations.

3. What will you learn from developing this program?

Developing this program will provide me several learning opportunities, including:

F. File Handling: I will learn how to read data from and write data to CSV files using Python's csv module. This involves understanding the structure of CSV files, handling file exceptions, and using file operations effectively.

G. Data Manipulation: I will learn how to manipulate data in lists and perform operations such as adding, searching, deleting, and editing records. This will improve my skills in working with structured data and implementing data management operations.

H. User Input and Validation: I will learn how to prompt users for input and validate the input to ensure it meets specific requirements. This includes checking for required fields, handling invalid data types, and providing appropriate error messages.

I. Program Flow and Logic: I will gain experience in designing the flow and logic of a program, including implementing menus, conditionals, loops, and function calls. This will improve my understanding of control structures and program organization.

J. Exception Handling: I will learn how to handle exceptions, such as file not found errors or invalid input, using try-except blocks. This helps in making the program more robust by handling potential errors gracefully.

K. Data Formatting and Output: I will practice formatting data for display, including aligning columns and presenting data in a readable format. This enhances your skills in data presentation and output formatting.

L. Real-World Application: By addressing the problem of managing customer data, I will gain insight into how programming can be applied to real-world scenarios. This experience can be valuable for future projects or when working with data management systems in various domains.

Overall, developing this program will provide hands-on experience in working with files, data manipulation, user input, program flow, and real-world problem-solving. These skills can be applied to a wide range of programming tasks and help me become a more proficient developer.

4. What Python modules will your program use?
	csv, datetime, pytest


5. Will you separate your Python program into functions that each perform a single task?

Yes, my Python program will be separated into functions, with each function performing a single task. Let's break down the program into its individual functions and their respective tasks:

M. read_csv(): This function reads the contents of a CSV file and returns the headers and data as separate lists. It handles the file reading and exception handling.

N. write_csv(): This function writes the headers and data to a CSV file. It takes the file name, headers, and data as input and uses the `csv` module to write the data to the file.

O. add_new_customer(): This function adds a new customer to the data list. It prompts the user for input, validates the input, generates a new customer number, and returns the customer details as a list.

P. delete_existing_customer(): This function deletes an existing customer from the data list based on their name and customer number. It prompts the user for input, searches for the customer in the data list, removes the customer if found.

Q. search_customer(): This function searches for a customer based on their name, customer number, or phone number. It prompts the user for input, searches the data list for matching customers, and displays the results.

R. show_all_customers(): This function displays all the customer records in a formatted manner. It takes the headers and data as input, retrieves the current date and time, and prints the customer details along with the total number of customers.

S. edit_existing_customer(): This function allows the user to edit an existing customer's details. It prompts the user for input, searches for the customer in the data list, displays their current details, prompts for the field to update, and updates the corresponding field.

T. main(): This function serves as the entry point of the program. It initializes the file name, reads the CSV file, and starts an infinite loop to present a menu of options to the user. It calls the relevant functions based on the user's choice.

The separation of tasks into individual functions will help in modularizing the program and making it more organized, readable, and maintainable. Each function will focus on a specific task, making the code easier to understand and modify. It will also allow for code reuse and enhances the program's overall structure.