def open_list(provinces):
    try:
        with open("C:/Users/Fernando Cardozo/OneDrive/BYU/Web & Computer Programming/Spring 2023/CSE111/w9/provinces.txt", "rt",) as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: {provinces} not found.")
        return []


def read_list(lines):
    province_list = [line.strip() for line in lines]
    print(province_list)
    
    if province_list:
        province_list.pop(0)
        province_list.pop()
        
        province_list = [province.replace('AB', 'Alberta') for province in province_list]
        
        count_alberta = province_list.count('Alberta')
        print(f"Number of 'Alberta' occurrences: {count_alberta} times in the modified list.")

    return province_list


# Main program
file_name = 'provinces.txt'
lines = open_list(file_name)
modified_list = read_list(lines)
