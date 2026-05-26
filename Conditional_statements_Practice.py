"""
In Python
"""
# discount = 0
# given_amount = 1500
# if given_amount > 1200:
#     discount = given_amount*0.15
# print("Payable Amount :", given_amount-discount)






# age = 10
# if age >= 18:
#     print("You are a Major")
# else:
#     print("You are a minor")







# balance = 5000
#
# print("Welcome to ATM")
# pin = int(input("Enter your 4-digit PIN: "))
#
# if pin == 1234:
#     print("✅ Correct PIN")
#     choice = int(input("1. Check Balance\n2. Withdraw\n3. Deposit\nEnter choice: "))
#
#     if choice == 1:
#         print("Your balance is:", balance)
#     elif choice == 2:
#         amount = int(input("Enter amount to withdraw: "))
#         if amount <= balance:
#             balance -= amount
#             print("Withdrawal successful! Remaining balance:", balance)
#         else:
#             print("❌ Insufficient balance")
#     elif choice == 3:
#         amount = int(input("Enter amount to deposit: "))
#         balance += amount
#         print("Deposit successful! New balance:", balance)
#     else:
#         print("❌ Invalid choice")
# else:
#     print("❌ Wrong PIN! Access denied")






# username = "abdul0608"
# password = "abdul@0608"

# User input
# usr = input("Enter User name :")
# pwd = input("Enter password :")
#
# if usr == username and pwd == password:
#     print("Login in your account Successful!")
# elif usr == username and pwd != password:
#     print("wrong password! PLEASE try Again")
# elif usr != username and pwd == password:
#     print("User is Not Found!,Please Check the username!")
# else:
#     print("Please Provide the Input Fields!")






# balance = 15000
# print("HDFC Welcomes to You!")
# pin = int(input("Please! enter your PIN Number:"))
# if pin == 9876:
#     print("Successfully Verified")
#     choice = int(input("1.Balance Enquire\n2.Withdraw\n3.Deposit\nEnter Choice:"))
#     if choice ==1:
#         print("Balance in Account:", balance)
#     elif choice ==2:
#         amount = int(input("Enter Amount to Withdraw:"))
#         if amount <= balance:
#             balance -= amount
#             print("Withdraw is Successful, And Balance Amount is:", balance)
#         else:
#             print("Insufficient Balance!")
#     elif choice ==3:
#         amount =int(input("Enter Deposit Amount:"))
#         balance += amount
#         print("Deposit Successful! and Your Account Balance is:", balance)
#     else:
#         print("Invalid Choice!")
# else:
#     print("WRONG PIN Number!...Please! Enter Correct PIN Number")







# num = int(input("Enter the Number:"))
# print("Number = ", num)
# if num % 2 == 0:
#     if num % 4 == 0:
#         if num % 3 == 0:
#             print("Given Number Divisible by 2,3 &4")
#         else:
#             print("Given Number is Divisible by 2 and 4!")
#     else:
#         print("Given Number divisible by 2 only!")
# else:
#     print("Given Number is Not Divisible")


num = int(input("Enter the Number:"))
print("Number = ", num)
if num % 2 == 0 and num%4==0 and num%3==0:
    print("Given Number Divisible by 2,3 &4")
elif num%2==0 and num % 4 == 0:
    print("Given Number is Divisible by 2 and 4!")
elif num%2 ==0 and num %3 ==0:
    print("Given number is divisible by 2 & 3 only")
elif num%3 ==0 and num %4 ==0:
    print("Given number is divisible by 3 & 4 only")
elif num%3 ==0:
    print("Given number is divisible by 3 only")
else :
    print("Given Number is Not Divisible with any number")
