def print_pyramid_for_401_600_units():
    print("   0-200 units: Rs. 0.50 per unit")
    print("  201-400 units: Rs. 0.65 per unit (in excess of 200)")
    print("  401-600 units: Rs. 0.80 per unit (in excess of 400)")
    
    # Printing a pyramid to visually represent the range of 401-600 units
    rows = 6
    for i in range(1, rows + 1):
        # Spaces to align the pyramid
        print(' ' * (rows - i), end='')

        # Stars to represent units in excess of 400 (401-600 range)
        print('*' * (2 * i - 1))

    print("  Represents the range of 401-600 units at Rs. 0.80 per unit")

# Call the function to print the pyramid
print_pyramid_for_401_600_units()
