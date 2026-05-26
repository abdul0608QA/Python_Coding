"""
What is the Magic or dunder methods?
    Python Magic methods are the methods starting and ending with double underscores '__'.
    They are defined by built-in classes in Python and commonly used for operator overloading.
    They are also called Dunder methods, Dunder here means “Double Under (Underscores)”
"""

fullname ="Abdul khadar"
user = 'khadar'
person = 'CHITTI'
person2 = 'chitti'
print(fullname.split(' '))                  #result : ['Abdul','Khadar']
print(type(user))                           #result : <class 'str'>
print(dir(user))                            #result : it will print all available methods or functions of string
print(fullname.capitalize())                #result : Abdul Khadar it will print capital letter of the  string of starting letter only.
print(fullname)                             #result : Abdul khadar
print(fullname.index('a'))                  #result : 8    it will print  position of given letter in argument.
print(fullname.upper())                     #result : ABDUL KHADAR  it will print all uppercases of letters in a string.
print(fullname.lower())                     #result : abdul khadar  it will print all lowercases of letters in a string.
print(id(fullname))                         #result : 1900001855664 it will print memory address location of string.
print(fullname.casefold())
print(fullname.title())
print(fullname.swapcase())
print(fullname.find('d'))
print(fullname.find('r'))
print(fullname.capitalize())
print(fullname)
print(user.capitalize())            #result : Khadar                here starting letter of the string will capitalize
print(person.casefold())            #result : chitti                By using this function to convert upper case letters to lower case
                                    #                               letters only.
print(user.center(20))              #result :        khadar         it's used to print string in center.
print(user.center(12))              #result :    khadar             to given number that much length of spaces will apply at both sides
print(fullname.title())             #result : Abdul Khadar          by using title function it will print starting letter of every word as Capital
print(fullname.swapcase())          #result : aBDUL KHADAR          it will print lower case letters into uppercase and vice versa.
print(fullname.count('a'))          #result : 2                     it will print the number of occurrences of letter that you provided in argument.
print(person.count('I'))            #result : 2

print(user.encode())                #result : b'khadar'
print(user.endswith('a'))           #result : False .               It will return True or false value.. here string is endswith 'r' letter so its result is written as false.
print(user.endswith('r'))           #result : True                  here string is endswith 'r' letter so its result is written as True.

fullname2 = "A\tb\td\tu\tl\t \tk\th\ta\td\ta\tr"
print(fullname2.expandtabs(2))          #result : A b d u l   k h a d a r
print(fullname2.expandtabs(7))          #result : A      b      d      u      l             k      h      a      d      a      r
print(fullname2.expandtabs(4))          #result : A   b   d   u   l       k   h   a   d   a   r
print(fullname2.expandtabs())          #result : A       b       d       u       l               k       h       a       d       a       r
"""
 this method will provide how much tab space you want between characters it will provide.
"""
print(fullname.find('d'))              #result : 2          it will return index value of given argument.
"""
find() method :
        This method is same like index() method.
        The find() method finds the first occurrence of the specified value.
        The find() method returns -1 if the value is not found.
        The find() method is almost the same as the index() method, the only difference is that the index() method 
        raises an exception if the value is not found.
"""
#  Syntax : string.find(value, start, end).
#ex:
x = "Hi! My name is Abdul Khadar "
print(x.find('M', 3, 15))     #Result : 4        Here 3 and 15 are range in between I want to search that
                                                                    # "M" letter. if it's not in that range it will return as -1 as default.


print(x.find('r', 3, 15))     #Result : -1      character 'r' is not in range os 3-15 so it has written as -1.


"""
format() method :
                The format() method formats the specified value(s) and insert them inside the string's placeholder.
                The placeholder is defined using curly brackets: {}. This method is useful at the time of dynamic outputs.
"""
name = "ABDUL"
age = 30
place = 'Bangalore'
print(" HI! My name is {0}, I am {1} years old guy, and I am living in {2}.".format(name, age, place))
      # Result : HI! My name is ABDUL, I am 30 years old guy, and I am living in Bangalore.

x = 60.50
print(" My weight was {}kgs " .format(x))     # Result : My weight was 60.5kgs   For floating datatypes it will print one decimal point.

# Example :
txt = "I have {a: .2f}k in my pocket right now."
print(txt.format(a = 1.25))                     # Result : I have 1.25k in my pocket right now.

#Exmple :
a = 3.75
statement = "I am lending {}k money from my colleague."
print(statement.format(a))                      # result : I am lending 3.75k money from my colleague.

# parameters in format function.
my_string = "{} is currently working on {} {} network across county and to established it by the end of {} year"
#print(my_string.format("Tejas Networks ", "BSNL", "5G"))            #Result : IndexError: Replacement index 3 out of range for positional args tuple
""" Because here number of placeholders are 4 but i passed only 3 values in that string, So it shows Index erros."""

x = {'a': "ABDUL", 'b':"KHADAR"}
print("{a}'s last name is {b}.".format_map(x))           # result : ABDUL's last name is KHADAR.

statement = {"name" :["Ramu","Vijay","Surya"],"Profession" : ['student','Software Engineer','Doctor'], "AGE":[22, 30,34]}
print("{name[0]} is a {Profession[0]} and he is just {AGE[0]} years old guy.".format_map(statement))        #Result : Ramu is a student and he is just 22 years old guy.
print("{name[2]} is a {Profession[2]} and he is {AGE[2]} years old guy.".format_map(statement))             #Result : Surya is a Doctor and he is 34 years old guy.
print("{name[1]} is a {Profession[1]} and he is {AGE[1]} years old guy.".format_map(statement))             #Result : Vijay is a Software Engineer and he is 30 years old guy.

print(txt.isalnum())            #result : False.    Bcz in 'txt' variable other than alphanumeric characters are present.

stat1 = "Mynameisabdul1234"
print(stat1.isalnum())                  #result : True.
print(stat1.isalpha())                  #result : False.
print(stat1.isascii())                  #result : True.
print(stat1.isdecimal())                #result : False.
print(stat1.isdigit())                  #result : False.
print(stat1.isidentifier())             #result : True.
print(stat1.islower())                  #result : False.
print(stat1.isupper())                  #result : False.
print(stat1.isnumeric())                #result : False.
print(stat1.istitle())                  #result : True.

"""
join() Method : 
       The join() method in Python is used to concatenate the elements of an iterable (such as a list, tuple, or set)
       into a single string with a specified delimiter placed between each element.
"""
#Example :
stat2 = ['Hi','Abdul,','How','are','you?']
print(' '.join(stat2))                  #result : Hi Abdul, How are you?
print('-'.join(stat2))                  #result : Hi-Abdul,-How-are-you?

"""
replace() method:
        This method replaces all occurrences of a specified substring in a string and returns a new string without
        modifying the original string.
"""
#Example :
stat3 = "Hello Abdul, How are you?"
print(stat3.replace("Hello","Hi!"))         #result :Hi! Abdul, How are you?

"""
Using replace() with Count Limit :
        By using the optional count parameter, we can limit the number of replacements made.
        This can be helpful when only a specific number of replacements are desired.
"""
#Example:
stat4 = "one two three five five"
print(stat4.replace("five","four",1))       #Result : one two three four five.
print(stat4.upper())

"""
zfill() Method :
        This method in Python is used to pad a string with zeros (0) on the left (i.e from beginning) until it reaches 
        a specified width.
"""
#Example :
num = "346"
print(num.zfill(7))             #result : 0000346
print(num.zfill(2))             #result : 346        here already three characters are occupied in string so no zeros are padded in this string.
print(num.zfill(3))             #result : 346        same here also 3 characters are filled with digits.So no zeros are padded.
print(num.zfill(4))             #result : 0346       here only one zero is padded bcz already 3 characters are filled.
print(num.zfill(10))            #result : 0000000346

