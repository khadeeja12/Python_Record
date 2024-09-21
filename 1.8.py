def rev_num(n):
    return int(str(n)[::-1])
def is_paliandrome(n):
    return str(n) == str(n)[::-1]

def add_paliandrome(n):
    while not is_paliandrome(n):
        revd_num = rev_num(n)
        print(f"{n} + {revd_num} = {n + revd_num}")
        n+=revd_num
    return n

number = int(input("Enter a num:"))
result = add_paliandrome(number)
print(f"The paliandrome is:{result}")
