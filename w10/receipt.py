import csv
import datetime


def read_dictionary(file_path, key_index):
    data_dict = {}
    with open(file_path, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header row
        for row in reader:
            key = row[key_index]
            data_dict[key] = row
    return data_dict

def main():
    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.datetime.now()

    print("\nWelcome to ZION STORE")
    print("************************")
    print("\nOrdered items: ")

    try:
        products_dict = read_dictionary("C:/Users/Fernando Cardozo/OneDrive/BYU/Web & Computer Programming/Spring 2023/CSE111/w9/Prove_Milestone_Text_Files/products.csv", 0)

        with open("C:/Users/Fernando Cardozo/OneDrive/BYU/Web & Computer Programming/Spring 2023/CSE111/w9/Prove_Milestone_Text_Files/request.csv", "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            # for the requested elements
            REQUESTED_PRODUCT_INDEX = 0
            REQUESTED_QUANTITY_INDEX = 1

            # for the products_dict elements
            PRODUCT_NAME_INDEX = 1
            PRODUCT_COST_INDEX = 2

            # counter for the amount of ordered items
            ordered_items_total = 0
            subtotal = 0

            for row_list in reader:
                requested_product_number = row_list[REQUESTED_PRODUCT_INDEX]
                requested_quantity = row_list[REQUESTED_QUANTITY_INDEX]

                for key, product in products_dict.items():
                    name = product[PRODUCT_NAME_INDEX]
                    cost = float(product[PRODUCT_COST_INDEX])

                    if requested_product_number == key:
                        ordered_items_total += int(requested_quantity)

                        # Check if today is Tuesday or Wednesday
                        if current_date_and_time.weekday() in [1, 2]:
                            cost *= 0.9  # Apply 10% discount

                        same_item_total = cost * float(requested_quantity)
                        subtotal += same_item_total
                        print(
                            f"- {name}: {requested_quantity} | ${cost:.2f}")
            tax = subtotal * 0.06
            total = subtotal + tax
            print(f"\n-----------------")
            print(f"\nNumber of items: {ordered_items_total}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Sales Tax: {tax:.2f}")
            print(f"Total: ${total:.2f}")
            print(f"\nThank you for shopping at ZION STORE!")
            print('Tuesday or Wednesday 10% off all products')
            print(f"{current_date_and_time:%d/%m/%Y %H:%M:%S}")

    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("Please choose a different file.")

    except KeyError as key_err:
        print(type(key_err).__name__, key_err)
        print("Please enter a valid ID.")


if __name__ == "__main__":
    main()