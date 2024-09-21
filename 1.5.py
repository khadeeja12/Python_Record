def print_numerical(rows):
    for i in range(1, rows + 1):
        for _ in range(rows-i):
            print(" ",end="")
        for j in range(1,2*i):
            print(j,end="")
        print()

while True:
    try:
        rows=(int(input("Enter the num of rows for the pyramid:")))
        if rows<=0:
            print("Please enter a positive integer")

        else:
            break
    except ValueError:
        print("Inavlid Input")

print_numerical(rows)
