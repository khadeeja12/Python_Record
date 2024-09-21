def print_pyramid_for_601_above_units():
    print("  601+ units: Rs. 1.00 per unit (in excess of 600)")
    
    # Printing a pyramid to visually represent units above 600
    rows = 7
    for i in range(1, rows + 1):
        # Spaces to align the pyramid
        print(' ' * (rows - i), end='')

        # Stars to represent units in excess of 600
        print('*' * (2 * i - 1))

    print("  Represents the range of 601+ units at Rs. 1.00 per unit")

# Call the function to print the pyramid
print_pyramid_for_601_above_units()
