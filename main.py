from database import create_tables
import models


def menu():
    while True:
        print("\n--- Blood Bank System ---")
        print("1. Add Donor")
        print("2. View Donors")
        print("3. Search Donor")
        print("4. Add Blood Stock")
        print("5. Request Blood")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Name: ")
            age = int(input("Age: "))
            group = input("Blood Group: ")
            contact = input("Contact: ")
            models.add_donor(name, age, group, contact)

        elif choice == '2':
            for donor in models.view_donors():
                print(donor)

        elif choice == '3':
            group = input("Enter Blood Group: ")
            print(models.search_donor(group))

        elif choice == '4':
            group = input("Blood Group: ")
            units = int(input("Units: "))
            models.add_blood_stock(group, units)

        elif choice == '5':
            group = input("Blood Group: ")
            units = int(input("Units needed: "))
            if models.request_blood(group, units):
                print("Request fulfilled")
            else:
                print("Insufficient stock")

        elif choice == '6':
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    create_tables()
    menu()