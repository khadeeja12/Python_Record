fac_dict ={}

def fac(n):
    if n==0 or n==1:
        fac_dict[n] = 1
        return 1
    
    if n in fac_dict:
        return fac_dict[n]

    result = n * fac(n-1)
    fac_dict[n] = result
    return result

number = int(input("Enter a num to calculate factorial"))

fact = fac(number)
print(f"The factorial of {number} is {fact}")

print("\nStored factorial in dict: ",fac_dict)
