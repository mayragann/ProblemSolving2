#loop that continues until number = 1 happy
#example is 19
#number needs to reach 1 for it to be happy

def sumofdigit(n):

    res = 0
    rem = 0
    while n > 0:
        res = n % 10
        rem = rem + res*res
        n = n // 10
    return rem

num = int(input("Please enter a number: "))
result = num
while result != 1 and result != 4:
    result = sumofdigit(result)

if result == 1:
    print(f'{num} is a happy number')
else:
    print(f'{num} is not a happy number')   