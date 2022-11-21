from collections import Counter


# happy numbers
# loop that continues until number = 1 happy
# example is 19
# number needs to reach 1 for it to be happy

# def sumofdigit(n):

#     res = 0
#     rem = 0
#     while n > 0:
#         res = n % 10
#         rem = rem + res*res
#         n = n // 10
#     return rem

# num = int(input("Please enter a number: "))
# result = num
# while result != 1 and result != 4:
#     result = sumofdigit(result)

# if result == 1:
#     print(f'{num} is a happy number')
# else:
#     print(f'{num} is not a happy number')   

# Python program to display all the prime numbers within a range



# def main():
#     for i in range(1, 101):
#         if [(i % j) == 0 for j in range(2, i)].count(False) == (i - 2):
#             print(f'{i} Prime Number')
#         else:
#             print(i)
# main()


# Fibonacci sequence
# fn = fn-1 + fn2 n>1
# in other words: f1-1+1 =2, f2-1+2=3, 2+3=5, f3-3+5 =8.  f4-5+8=13 so on and so on..
# series is the F1 number
# num1 and numb 2 are the numbers that are being added together
# def fibonacci(num):
#     num1 = 0
#     num2 = 1
#     series = 0
#     for i in range(num):
#         print(series, end=' ')
#         num1 = num2
#         num2 = series
#         series = num1 + num2
 
 
# # running function after takking user input
# num = int(input('Enter how many numbers needed in Fibonacci series- '))
# fibonacci(num)
    

# shoping_list = ["apples", "bananas", "carrots"]


# item = input("Enter the item that you would like to remove to shopping list: ")

# shoping_list.remove(item)
# print(shoping_list)

list =["cat", "dog" ,"bird", "parrot" ,"hi", "name" ,"cat", "heep", "hi", "parrot"]

count_a = list.count('cat')
print(f'{count_a=}')

thisList=[]
thisList.append("cat")
print(thisList)
thisList.remove("cat")
thisList.extend(("cat", "dog", "bird"))
print(thisList)

number = 3
possible_words=[]
for word in list:
    if len(word)==number:
        possible_words.append(word)
print(possible_words)

print("Duplicate animals")

for i in range(0, len(list)):
    for j in range(i+1, len(list)):
        if(list[i]==list[j]):
            print(list[j])