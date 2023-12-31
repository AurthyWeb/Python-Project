# -*- coding: utf-8 -*-
"""Python-Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tu0E_6ETwWFu8KxZGJr0NGvVZaCXt1Dd
"""

wedding_data = []


def add_marriage_details():
    groom_name = input("Enter Groom's Name: ")
    bride_name = input("Enter Bride's Name: ")
    date = input("Enter Wedding Date: ")
    venue = input("Enter Venue: ")

    try:
      total_budget = float(input("Enter Total Budget: "))
      catering_cost = float(input("Enter Catering Cost: "))
      shopping_cost = float(input("Enter Shopping Cost: "))

      total_expense = catering_cost + shopping_cost
    except ValueError:
         print("Invalid cost input. Please enter a valid number.")
         return

    wedding = {
        'Groom Name': groom_name,
        'Bride Name': bride_name,
        'Date': date,
        'Venue': venue,
        'Total Budget': total_budget,
        'Total Expense': total_expense
    }

    wedding_data.append(wedding)
    print("Marriage details added successfully!")


def show_details():
    for index, wedding in enumerate(wedding_data, 1):
        print(f"Marriage {index} details:")
        for key, value in wedding.items():
            print(f"{key}: {value}")
        print()


def update_details():
    groom_name = input("Enter Groom's Name to update details: ")
    for wedding in wedding_data:
        if wedding['Groom Name'] == groom_name:
            venue = input("Enter New Venue: ")
            total_budget = float(input("Enter New Total Budget: "))

            wedding['Venue'] = venue
            wedding['Total Budget'] = total_budget
            print("Details updated successfully!")
            return
    print("Marriage details not found.")


def delete_details():
    bride_name = input("Enter Bride's Name to delete details: ")
    for wedding in wedding_data:
        if wedding['Bride Name'] == bride_name:
            wedding_data.remove(wedding)
            print("Details deleted successfully!")
            return
    print("Marriage details not found.")


def calculate_remaining_amount():
    for wedding in wedding_data:
        total_budget = wedding['Total Budget']
        total_expense = wedding['Total Expense']
        remaining_amount = total_budget - total_expense
        print(f"Remaining Amount for {wedding['Groom Name']} and {wedding['Bride Name']} is: {remaining_amount}")


while True:
    print("\nWedding Event Management System")
    print("1. Add Marriage Details")
    print("2. Show Details")
    print("3. Update Details")
    print("4. Delete Details")
    print("5. Calculate Remaining Amount")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_marriage_details()
    elif choice == '2':
        show_details()
    elif choice == '3':
        update_details()
    elif choice == '4':
        delete_details()
    elif choice == '5':
        calculate_remaining_amount()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")







