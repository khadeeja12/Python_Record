def sum(x):
    if x==0:
        return 0
    else:
        return x +sum(x-1)

result = sum(10)

print("The sum of num from 0 to 10:", result)
