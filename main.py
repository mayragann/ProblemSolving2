#In number theory, a happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit
#On the other hand, 4 is not a happy number because the sequence starting with 4**2 he number that started the sequence,
#and so the process continues in an infinite cycle without ever reaching 1. A number which is not happy is called sad or unhappy.

# Here we will use the dynamic programming approach, and solve this using recursion
# Base case is, when n = 1, then return true
# When n is already visited, return false
# mark n as visited
# n := n as string, l := list of all digits in n
# temp := squared sum of all digits
# return function recursively with parameter temp and visited list

def isHappyNumber(n):    
    digit = 0
    sum = 0    
    while(n > 0):    
        digit = n % 10 
        sum = sum + (digit * digit)    
        n = n // 10   
    return sum    
        
num = int(input("Enter a number: "))    
result = num    
     
while(result != 1 and result != 4):    
    result = isHappyNumber(result)   
     
if(result == 1):    
    print( f'{num} is a Happy Number!!!')   
else:    
    print(f'{num} is an Unhappy Number!!!')