# Open the provinces.txt file for reading
with open("C:/Users/Fernando Cardozo/OneDrive/BYU/Web & Computer Programming/Spring 2023/CSE111/w9/provinces.txt", "rt") as file:
    # Read the contents of the file into a list
    provinces_list = file.read().splitlines()

# Print the entire list
print("Original list:")
print(provinces_list)

# Remove the first and last elements from the list
provinces_list.pop(0)
provinces_list.pop()

# Replace "AB" with "Alberta" in the list
provinces_list = [province.replace("AB", "Alberta") for province in provinces_list]

# Count the number of elements that are "Alberta"
count = provinces_list.count("Alberta")

# Print the modified list and the count
print("Modified list:")
print(provinces_list)
print("Count of 'Alberta':", count)
