#
# a="hello world"
# l=[]
# for i in a:
#      if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#          l.append(i)
# print(l)



# string1= "Hai Abdul! How are You?"
# list1=[]
# for i in string1:
#     if i in 'AEIOUaeiou':
#         list1.append(i)
# print(list1)
#
#
# first="Hello World"
# second="python program learning"
# result =[]
# #output = ["o", "o", "r", " "]
# for i in first:
#     if i in second:
#         if second.count(i) > 1:
#            print(i)
#            result.append(i)
# print(result)
#
# '''
# d={"a": 1, "b": 2, "c":3, "d": 4}
# print(d["b"], d["d"])
# '''

# n = 10
# for i in range(0, n, 2):
#     print(i)
#
#
# list1=["Abdul","Khadar","Bangalore","Spice Garden"]
# for i in list1:
#     print(i)                #result : Abdul
#                                     # Khadar
#                                     # Bangalore
#                                     # Spice Garden
#
# tuple1=('train','bus','truck','car','aeroplane',)
# for i in tuple1:
#     print(i)            #result: train\nbus\ntruck\ncar\naeroplane
#
# str1= "HAI Abdul!"
# for i in str1:
#     print(i)            #result :H\nA\nI\n \nA\nb\nd\nu\nl\n!
#
# dict1={'name':"Abdul",'Age':30,"Place":"Anantapur"}
# # for i in dict1:
# #     print(i)            #result:name\nAge\nPlace
# for key, value in dict1.items():
#     print(key,":",value)        #result: name : Abdul\nAge : 30\nPlace : Anantapur
#
#
# set1={"Khadar",500,533,"Electrical"}
# for i in set1:
#     print(i)            #result:Khadar\nElectrical\n500\n533




# string1= "Hai Abdul! How are You?"
# list1=[i for i in string1 if i in "AEIOUaeiou"]
# print(list1)            #result : ['a', 'i', 'A', 'u', 'o', 'a', 'e', 'o', 'u']



# a="helloworld"
# l=[i for i in a if i in "aeiou"]
# print(l)




# set1={"Khadar",500,533,"Electrical"}
# l2=[i for i in set1 ]
# print(l2)           #result : [500, 'Electrical', 'Khadar', 533]



# list2= ['a','s','t','u','e','f','g','h','k','i']
# for i in list2:
#     if i in "AEIOUaeiou":
#         print("{} is a Vowel".format(i))



# str1= "You are Learning Python!"
# for i in str1:
#     if i in "AEIOUaeiou":
#         print("{} is a Vowel".format(i))




# str2 = "Hi! Good Morning Abdul"
# list3=[i for i in str2 if i in "AEIOUaeiou" ]
# # print("{} is a Vowel".format(list3))
# print(list3)



# x="hello world!"
# l=[]
# for i in x:
#     if i in 'aeiou':
#         l.append(i)
# print(l)

#Q)print common letters in both strings which is repeated more than once?
# a1='hello world'
# b1='Python Program learning'
# l1=[]
# for i  in a1:
#     if i in b1:
#         if b1.count(i)>1:
#             l1.append(i)
# print(l1)                       #result : ['o', ' ', 'o', 'r']
# for i in a1:
#     if i in b1:
#         if a1.count(i)>1 and b1.count(i)>1:
#             l1.append(i)
# print(l1)             #result : ['o', 'o']
# for i in a1:
#     if i in b1:
#         if b1.count(i)>1:
#             l1.append(i)
# for i in l1:
#     if l1.count(i)>1:
#         l1.remove(i)
# print(l1)


# x = "hello world"
# y = "python programing learning"
# L = []
# for i in x:
#     if i in y and y.count(i)>1:
#         L.append(i)
# print(L)


# dict1= {'a':20,'b':26,'c':33,'d':47,'e':42,'f':59}
# for k,v in dict1.items():
#     if v%2==0:
#         print(k,v)
# for k, v in dict1.items():
#     if v%2!=0:
#         print(v)


# Finding Factorial using For and While loops

# n = int(input("Enter the Number:"))
# result=1
# for i in range(1,n+1):
#     result *=i
# print("Factorial of ",n, "is :",result)


# n = int(input("Enter the Number:"))
# temp = n
# result = 1
# while temp > 0:
#     result*=temp
#     temp -=1
# print("Factorial of ", n, "is:",result)

#Check any number is divisible by 2 or3 or4?
given_number=int(input("Enter any Number: "))
divisors = [2, 3, 4]
temp = 0
for i in divisors:
    if given_number%i == 0:
        if temp == 0:
            print("given_number is divisible by:",end = " ")

        print(i,end=" ")
        temp = 1
if temp == 0:
    print("Not divisible with any number ")
