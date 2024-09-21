def add(x,y):
    return x+y

def sub(x,y):
    return x - y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print("\n================================")
print("Select Operation:")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

while True:
    choice = input("Enter yor choice (1/2/3/4)")

    if choice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter your first num:"))
            num2 = float(input("Enter your second num"))
        except ValueError:
            print("Invalid input. Enter a valid number")
            continue

        if choice == "1":
            print(num1, "+" , num2 , "=" ,add(num1,num2))
            continue
        elif choice == "2":
            print(num1 , "-" , num2 , "=" , sub(num1,num2))
            continue
        elif choice == "3":
            print(num1 , "*" , num2 , "=" , mul(num1,num2))
            continue
        elif choice == "4":
            print(num1 , "/" , num2 , "=" , div(num1,num2))
            continue

        nextCalcu = input("next calculation:(yes/no)")
        if nextCalcu == "no":
            break

    else:
        print("Invalid input")

