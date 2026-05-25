"""
while loops practicing
"""

# age = 33
# while age>28:
#     print("get marriage as soon as possible")
#     break


#Q) Print 1 to 10 numbers but skip 5
# i = 1
# while i<=10:
#     if i==5:
#         i +=1
#         continue
#     print(i)
#     i +=1
#
#Q) Print even numbers between 1 to 50 numbers?
# i = 0
# l=[]
# while i < 50:
#     if i%2 !=0:
#         l.append(i)
#         # i +=1
#         # continue
#     i +=1
# print(l)

# i = 1
# l = []
# while i <= 50:
#     if i % 2 == 0:
#         l.append(i)
#         i += 1
#         continue
#     i += 1
# print(l)


# i = 0
# l = []
# while i <50:
#     if i%2==0:
#         i +=1
#         l.append(i)
#         continue
#     i +=1
# print(l)

# i=0
# l=[]
# while i <=50:
#     if i%2==0:
#         l.append(i)
#     i +=1
# print(l)

# i = 0
# while i <= 10:
#     i += 1
#     if i == 5:
#         break
#     print(i)
#
#
# i = 1
# while i<=100:
#     if i%19 ==0:
#         print("First Multiple of 19 is:",i)
#         break
#     i=i+1
#
#
# i=0
# list1=[]
# while i<=15:
#     if i==15:
#         break
#     i+=1
#     list1.append(i)
# print(list1)





# i=2
# list2=[]
# while i <=100:
#     j=2
#     while j<i:
#         if i%j==0:
#             break
#         j +=1
#     if j ==i:
#         list2.append(i)
#     i +=1
# print(list2)

#Q) Print Prime Numbers with in 100 by using while and for loops?
# x = int(input("Enter the Number:"))
# i =2
# while i<=x:
#     j=2
#     while j<i:
#         if i%j==0:
#             break
#         j +=1
#     if j==i:
#         print(i, end=',')
#     i+=1


#*by using for loop*

# for num in range(2,100):
#     for j in range(2,100):
#         if num%j==0:
#             break
#     if num == j:
#         print(num,end=' ')              #result:2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
#



# number=int(input("\nEnter the number:"))
# for i in range(2,number):
#     for j in range(2,number):
#         if i%j==0:
#             break
#     if i==j:
#         print(i, end=',')               #result:Enter the number:65
#                                         # 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,



# #Q) Print the prime numbers with in given range of user input?
# x=int(input("Enter starting number:"))
# y=int(input("Enter the last number:"))
#
# if x<y:
#     while x<= y:
#         i=2
#         while i<=x:
#             if x%i==0:
#                 break
#             i+=1
#         if x==i:
#             print(x, end=" ")
#         x +=1
# else:
#     print("Invalid Input")
#
#
# """improved method"""
#
# x = int(input("Enter starting number: "))
# y = int(input("Enter the last number: "))
#
# if x < y:
#     while x <= y:
#         if x > 1:
#             i = 2
#             while i * i <= x:
#                 if x % i == 0:
#                     break
#                 i += 1
#             else:
#                 print(x, end=" ")
#         x += 1
# else:
#     print("Invalid Input")




#Q) Print the prime numbers with in given range of user input using for loop?
# a=int(input("Enter starting number:"))
# b=int(input("Enter the last number:"))
# if a<b:
#     for i in range(a,b):
#         for j in range(2,b):
#             if i%j==0:
#                 break
#         if i == j:
#             print(i,end=' ')
# else:
#     print("Invalid Input")




# def greetings():
#     print("\nHi Abdul! How are you?")
# greetings()
#
#
# def finding_evenodd(x):
#     if x%2 ==0:
#         print("{} is Even Number".format(x))
#     else:
#         print("{} is Odd Number".format(x))
# finding_evenodd(348)
#
#
# def check_evenodd(x):
#     if x%2 ==0:
#         print(f"{x} is Even Number")
#     else:
#         print(f"{x} is Odd Number")
# check_evenodd(57)                       #result: 57 is Odd Number
# check_evenodd(846)                      #result: 846 is Even Number

# number = 124
# print(dir(number))


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))


# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://www.hotstar.com/in/home")
# time.sleep(5)


# x = 34
#
# z = [ "odd", "even"]
# print(z[(x+1)%2])


# """Find the next greatest element and print output in list formate"""
# a =[5,1,4,9,7,2]
# #output[9,4,9,-1,-1,-1]
#
# output=[]
# for i in range (len(a)):
#     x = -1
#     for j in range(i+1, len(a)):
#         if a[j] > a[i]:
#             x = a[j]
#             break
#     output.append(x)
#
# print(output)               #[9, 4, 9, -1, -1, -1]
#
#
# """Find next Lower number from given input and print output in list formate
#  a = [5,1,4,9,7,2]
# """
# a = [5,1,4,9,7,2]
# result =[]
# for i in range(len(a)):
#     y =-1
#     for j in range (i+1, len(a)):
#         if a[j]<a[i]:
#             y = a[j]
#             break
#     result.append(y)
# print(result)           #[1, -1, 2, 7, 2, -1]
print(bin(35))
print(bin(79))