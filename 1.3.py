def calculate_bill(units_consumed):
    # Base rates for units consumed
    if units_consumed <= 200:
        total_bill = units_consumed * 0.50
    else:
        total_bill = (200 * 0.50) + (units_consumed - 200) * 1.00
    
    # If the bill exceeds Rs. 400, add 15% surcharge
    if total_bill > 400:
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
