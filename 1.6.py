def findSum():
    count =0
    sum =0

    for i in range(101,200):
        if i % 7 == 0:
            count +=1
            sum +=1

    print("Numbers of integers divisible by 7 between 100 and 200: ",count)
    print("Sum of integers divisible by 7 between 100 and 200: ",sum)
    
findSum()
