def calculate_bill(units_consumed):
    # Rates based on unit consumption
    if units_consumed <= 100:
        total_bill = units_consumed * 3
    elif units_consumed <= 200:
        total_bill = (100 * 3) + (units_consumed - 100) * 5
    else:
        total_bill = (100 * 3) + (100 * 5) + (units_consumed - 200) * 7

    # Check if surcharge is needed (if units > 300)
    if units_consumed > 300:
        surcharge = total_bill * 0.15
        total_bill += surcharge

    # Minimum bill condition
    if total_bill < 100:
        total_bill = 100

    return total_bill

# Input from user
units = float(input("Enter the number of units consumed: "))
bill = calculate_bill(units)
print(f"Total bill: Rs. {bill:.2f}")
