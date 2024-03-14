def print_day_of_week(week_no):
    match week_no:
        case 1:
            print(week_no, "is Monday")
        case 2:
            print(week_no, "is Tuesday")
        case 3:
            print(week_no, "is Wednesday")
        case 4:
            print(week_no, "is Thursday")
        case 5:
            print(week_no, "is Friday")
        case 6:
            print(week_no, "is Saturday")
        case 7:
            print(week_no, "is Sunday")
        case _:
            print("Invalid week number. Please enter a number between 1 and 7.")

# Get user input
a = int(input("Enter week no => "))

# Call the function with the input
print_day_of_week(a)
