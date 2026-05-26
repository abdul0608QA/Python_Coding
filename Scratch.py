"""
1) What is a python and characteristics?
2) Naming spaces ?
3) What is a python path?
4) what are the inbuilt functions with examples?
4) What are the datatypes with examples?
5) What is mutable and immutable?
6) What are the int methods with examples?
8) What are the string methods with examples?
9) What are the tuple methods with examples?
10) What are the list methods with examples?
11) What is the diff b/w list and tuple?
12) What is the diff b/w insert, append and extend?
13) What is the diff b/w pop, remove and clear?
14) What is the diff b/w count adn index?
15) what are the comments types?
16) What is dict with examples?
17) What is the diff b/w pop and popitem?
18) What are the ways to update the dict values?
19) How to get the keys, values and key values pairs?
20) What is set with examples?
21) What are the available methods?
22) What is diff b/w list & tuple?
23) What is diff b/w dict & set?
24) What is  a slicing with examples?
25) What is  indexing? positive nad negative?
26) What are the constants in python?
27) What are the operators in python with examples?
28) Type casting with examples?
29) What are the conditions we have in python? with examples
"""
"""
1. What is Programming Language?
    A programming language is a set of instructions that tells a computer what to do.
    It's a way for humans to communicate with computers and create programs, applications, and other software. 
"""
"""
1.Where we can use python?
    We use python in various programming platforms like
    1.Server-Client communication Programming
    2.Web application developments---ex: Django, flask ..etc..
    3.AI(Artificial Intelligence)/ML(Machine Learning) and Data science
     (for Data science required packages are pandas, numpy,matlab, scipy )
    4.Networking applications, Gaming applications.
    5.Software applications like Automation Testing
    6.Web Scrapy(it is like gathering data from web)
"""
"""
2.What is Python?
    Python is a high-level, interpreted programming language and it is Object oriented programme. Everything will be 
    stored in to objects.In python we don't need to declare the type of variables, bcz it is
    dynamically typed language.
"""
"""
#Q) What are the python Features?
    * Easy to learn and use:
				Python's Syntax is clean and readable syntax, it uses indentation to define code blocks instead of braces or keywords 
				making it beginner friendly.
    * High-level language:
                When we write programme in python we don't need to remember to system architecture and nor we do need the memory management.
                It handles low-level details like memory-management.
    * Free and opensource:
                It is freely available at its official website and its source code is also open for public view and modification. 
    * It is object-oriented programme:
                Python fully supports object-oriented programming(OOPs) principles like class, object, inheritance, and polymorphism 
                which helps in reusable and modular code.
    * It is Interpreted language:
                Python code is executed line by line by an interpreter, which simplifies debugging and tests.
    * It has Large standard library:
                Python comes with vast collection of pre-built modules and packages that provides functionalities for various tasks,
                from web development to data manipulation.
    * It is Dynamically typed Language:
                It means you don't need to declare data type of variable explicitly, python determines data types of variable
                during run-time and speeding up development.
    * It is platform Independent:
                Python code can run on various platforms or operating systems(windows, MAC os, LINUX) without requiring significant 
                changes.

"""
"""
3.What is Name spaces or Indentation in Python?
    Indentation is a fundamental part of Python's syntax and is used to define blocks of code,
    group them, and identify which block is being executed. Indentation is refers to the spaces at the beginning
    of code line. Its tells the python Interpreter that group of statements belongs to specific block.  
"""
"""
4. What is Python path?

"""
"""
5.What are the Inbuilt Functions in Python with examples?
    abs()           :	Returns the absolute value of a number
    all()           :	Returns True if all items in an iterable object are true
    any()           :	Returns True if any item in an iterable object is true
    ascii()         :	Returns a readable version of an object. Replaces none-ascii characters with escape character
    bin()           :	Returns the binary version of a number
    bool()          : 	Returns the boolean value of the specified object
    bytearray()     :	Returns an array of bytes
    bytes()         :	Returns a bytes object
    callable()      :	Returns True if the specified object is callable, otherwise False
    chr()           :	Returns a character from the specified Unicode code.
    class method()	:   Converts a method into a class method
    compile()       :	Returns the specified source as an object, ready to be executed
    complex()       :	Returns a complex number
    delattr()       :	Deletes the specified attribute (property or method) from the specified object
    dict()          :	Returns a dictionary (Array)
    dir()           :	Returns a list of the specified object's properties and methods
    divmod()        :	Returns the quotient and the remainder when argument1 is divided by argument2
    enumerate()     :	Takes a collection (e.g. a tuple) and returns it as an enumerate object
    eval()          :	Evaluates and executes an expression
    exec()          :	Executes the specified code (or object)
    filter()        :	Use a filter function to exclude items in an iterable object
    float()         :	Returns a floating point number
    format()        :	Formats a specified value
    frozenset()     :	Returns a frozenset object
    getattr()       :	Returns the value of the specified attribute (property or method)
    globals()       :	Returns the current global symbol table as a dictionary
    hasattr()       :	Returns True if the specified object has the specified attribute (property/method)
    hash()          :	Returns the hash value of a specified object
    help()          :	Executes the built-in help system
    hex()           :	Converts a number into a hexadecimal value
    id()            :	Returns the id of an object
    input()         :	Allowing user input
    int()           :	Returns an integer number
    isinstance()    :	Returns True if a specified object is an instance of a specified object
    issubclass()    :	Returns True if a specified class is a subclass of a specified object
    iter()          :	Returns an iterator object
    len()           :	Returns the length of an object
    list()          :	Returns a list
    locals()        :	Returns an updated dictionary of the current local symbol table
    map()           :	Returns the specified iterator with the specified function applied to each item
    max()           :	Returns the largest item in an iterable
    memoryview()    :	Returns a memory view object
    min()           :	Returns the smallest item in an iterable
    next()          :	Returns the next item in an iterable
    object()        :	Returns a new object
    oct()           :	Converts a number into an octal
    open()          :	Opens a file and returns a file object
    ord()           :	Convert an integer representing the Unicode of the specified character
    pow()           :	Returns the value of x to the power of y
    print()         :	Prints to the standard output device
    property()      :	Gets, sets, deletes a property
    range()         :	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
    repr()          :	Returns a readable version of an object
    reversed()      :	Returns a reversed iterator
    round()         :	Rounds a numbers
    set()           :	Returns a new set object
    setattr()       :	Sets an attribute (property/method) of an object
    slice()         :	Returns a slice object
    sorted()        :	Returns a sorted list
    staticmethod()  :	Converts a method into a static method
    str()           :	Returns a string object
    sum()           :	Sums the items of an iterator
    super()         :	Returns an object that represents the parent class
    tuple()         :	Returns a tuple
    type()          :	Returns the type of an object
    vars()          :	Returns the __dict__ property of an object
    zip()           :	Returns an iterator, from two or more iterators
"""

# Naming Conventions:

# Possible or Valid Conditions:
"""TO Declare any variable we need follow some rules"""
name= "ABDUL" # it is a Valid declaration
_name = "ABDUL" # underscore is allow at any place in variable so it's valid declaration
__name="ABDUL" # valid declaration
NAME = "ABDUL"# Capital letters is allowed so it's valid
FullName= "ABDUL KHADAR" #it is valid
name1 = "khadar" # numerical numbers  and special characters are allowed middle, last of the variables, except starting.
Full1naME= "abdul khadar"# it's valid declaration
Full_Name = "ABDUL KHADAR"# valid declaration

# Invalid Conditions :
 name = "ABDUL"# Invalid bcz at starting Space character is not allowed.
1name= "KHADAR"# Numbers and special characters are not allowed at starting of variable name.
@name= "ABDUL"# invalid bcz special character is present at starting of variable.
Full Name = "ABDUL KHADAR"# invalid bcz spaces are not allowed at any place of variables.
""" 
Note : Class Name Should be starts with Capital Letter
       Variables names should be starts with lower case letters / camel cases
"""

"""
6.What are the Data types and with examples?
    Python Data types are the classification or categorization of data items.
    It represents the kind of value that tells what operations can be performed on a particular data.
    Since everything is an object in Python programming, Python data types are classes and variables are
    instances (objects) of these classes.
    The following are the standard or built-in data types in Python:
    Numeric data types  : int, float, complex.
    String data types   : str.
    Sequence types      : list, tuple, range.
    Binary types        : bytes, bytearray, memory  view.
    Mapping data type   : dict.
    Boolean type        : bool.
    Set data types      : set, frozenset.
"""

"""
7.What is mutable and immutable?
    In Python, mutable and immutable are terms used to describe whether a variable's value
    can be changed after it's created: 
    Mutable
        A variable is mutable if its value can be changed after it's created.
        Examples of mutable data types include lists, dictionaries, and sets.
    Immutable
        A variable is immutable if its value cannot be changed after it's created.
        Examples of immutable data types are integers, strings and tuples.
        
    Error handling: 
        If you try to change an immutable variable, Python will give an error. 
    Memory location: 
        Immutable variables share the memory location with other variables. 
    Dictionary keys: 
        Only immutable elements can be used as dictionary keys. 
    Data transformation: 
        Tuples don't have methods to perform data transformations in place because they're immutable. 
"""
"""
8. What is variable in Python?
    A variable in python is like a memory location, where you store a value, may or may not be change in future.
    In python to declare a variable we just have to assign a value to it, does not need any commands unlike other 
    programming languages.
    Variables in Python are case sensitive.
"""
#Ex:
a = 10         # here I am just declare a value "10" to variable "a"
B = "KHADAR"   # here declare string "KHADAR" to variable "B"
print(a)
print(B)

"""
9. What is Integer data type in python and What are the int methods with examples?
        Integers : This value is represented by int class. It contains positive or negative 
        whole numbers (without fractions or decimals).In Python, there is no limit to how long an integer value can be.
 """
# Ex:
a = 15
b = 20.5
c = 12+25j
d = 4
e = 6
print(a, 'is type of ', type(a))            #: result : 15 is type of  <class 'int'>
print(b, 'is type of ', type(b))            #: result : 20.5 is type of  <class 'float'>
print(c, 'is type of ', type(c))            #: result : (12+25j) is type of  <class 'complex'>
print('Quotient of a/b is ', a/b)           #: result : Quotient of a/b is  0.7317073170731707
print('Floored Quotient of a/b is', a//b)   #: result : Floored Quotient of a/b is 0.0
print('Reminder of b%a', b % a)             #: result : Reminder of b%a 5.5
print('Power e**d', e ** d)                 #: result : Power e**d 1296
print(id(a))                                #: result : 140719479420136
print(id(b))                                #: result : 2302280843024
print(id(c))                                #: result : 2302280842160
print(id(d))                                #: result : 140719479419784
print(id(e))                                #: result : 140719479419848
print(dir(a))  # This dir function will return all the available methods for any data types, class, or function
"""
   ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__',
    '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__',
    '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__',
    '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__',
    '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__',
    '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__',
    '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__',
    '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length',
    'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
      Above all are available methods for int data type. If these integer methods having suffix and prefix as
      double under scores then that methods are called as MAGIC methods or DUNDER methods.
"""
print(a.bit_count())    # Result : 4
print(d.bit_count())    # Result : 1
print(e.bit_count())    # Result : 2
#print(b.bit_count())   # Result : AttributeError: 'float' object has no attribute 'bit_count'
#print(c.bit_count())   # Result : AttributeError: 'complex' object has no attribute 'bit_count'
"""
  So in integer Data type "bit_count" function is not applicable for float and Complex numbers, it applicable only 
  base 10 integers only. 
"""
print(e.bit_length())       # Result : 3
print(a.bit_length())       # Result : 4
print(d.bit_length())       # Result : 3
print(c.bit_length())       # Result : AttributeError: 'float' object has no attribute 'bit_count'
print(b.bit_length())       # Result : AttributeError: 'float' object has no attribute 'bit_count'
""" Same like bit_count , bit_length function also not applicable to float & Complex int data types."""

print(c.conjugate())         # Result : (12-25j)
print(d.conjugate())         # Result : 4
print(b.conjugate())         # Result : 20.5
print(a.conjugate())         # Result : 15
print(e.conjugate())         # Result : 6
print(a.to_bytes())          # Result : b'\x0f'
#print(b.to_bytes())         # Result : AttributeError: 'float' object has no attribute 'to_bytes'
#print(c.to_bytes())         # Result : AttributeError: 'Complex' object has no attribute 'to_bytes'
print(d.to_bytes())          # Result : b'\x04'
print(e.to_bytes())          # Result : b'\x06'
"""
So function 'to_bytes()' is not applicable to complex & float int data Types.
"""
"""
10.What is Magic Methods or Dunder Methods in Python?
    Python Magic methods are the methods starting and ending with double underscores '__'.
    They are defined by built-in classes in Python and commonly used for operator overloading.
    They are also called Dunder methods, Dunder here means “Double Under (Underscores)”
"""

"""
11.What are the string methods with examples?
    A string is a sequence of characters. Python treats anything inside quotes as a string.
    This includes letters, numbers, and symbols. Python has no character data type so single character
    is a string of length 1.
    Ex: user = "ABDUL".   Here I am assigning string 'ABDUL' to variable 'user'.
    
    string methods are:
    print(dir(str)):
      ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
       '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
       '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
       '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize',
       'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index',
       'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
       'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
       'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
       'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""
"""
encode () method : 
        String encode() method in Python is used to convert a string into bytes using a specified encoding format.
        This method is beneficial when working with data that needs to be stored or transmitted in a specific encoding
        format, such as UTF-8, ASCII, or others.

Syntax of encode() method :
      string.encode(encoding=”utf-8″, errors=”strict”)

Parameters
encoding (optional):
            The encoding format to use. The default is "utf-8".
            Examples include "ascii", "latin-1", "utf-16", etc.
errors (optional):
            Specifies the error handling scheme. Possible values are:
            "strict" (default): Raises a UnicodeEncodeError for encoding errors.
            "ignore": Ignores errors and skips invalid characters.
            "replace": Replaces invalid characters with a replacement character (? in most encodings).
            "xmlcharrefreplace": Replaces invalid characters with their XML character references.
            "backslashreplace": Replaces invalid characters with a Python backslash escape sequence.              
"""
"""
format() method:
           This method offers a flexible and versatile way to construct textual output for a wide range of applications.
           Python string format() function has been introduced for handling complex string formatting more efficiently.
           Sometimes we want to make generalized print statements in that case instead of writing print statements 
           every time we use the concept of formatting.
           
Syntax: { }.format(value)
Parameters: 
      value : Can be an integer, floating point numeric constant, string, characters or even variables.
      Return type: Returns a formatted string with the value passed as parameter in the placeholder position.            
"""
name = "ABDUL"
age = 30
place = 'Bangalore'
print(" HI! My name is {0}, I am {1} years old guy and I am living in {2}.".format(name, age, place))
"""
Syntax : { } { } .format(value1, value2)
Parameters :  (value1, value2) : Can be integers, floating point numeric constants, strings, characters and even variables. 
                                 Only difference is, the number of values passed as parameters in format() method must be equal
                                 to the number of placeholders created in the string.
Errors and Exceptions : 
     IndexError : Occurs when string has an extra placeholder, and we didn’t pass any value for it in the format() method.
     Python usually assigns the placeholders with default index in order like 0, 1, 2, 3…. to access the values passed 
     as parameters. So when it encounters a placeholder whose index doesn’t have any value passed inside as parameter, 
     it throws IndexError.
"""
"""
isalnum() method:
       The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and 
       numbers (0-9).
isalpha() method      : It Returns True if all characters in the string are in the alphabet.
isascii() method      : It Returns True if all characters in the string are ascii characters.
isdecimal() method    : It Returns True if all characters in the string are decimals.
isdigit() method      : It Returns True if all characters in the string are digits
isidentifier() method : It Returns True if the string is an identifier
islower() method      : It Returns True if all characters in the string are lower case
isnumeric()	method    : It Returns True if all characters in the string are numeric
isprintable() method  : It Returns True if all characters in the string are printable
isspace() method      : It Returns True if all characters in the string are whitespaces
istitle() method      : It Returns True if the string follows the rules of a title
isupper() method      : It Returns True if all characters in the string are upper case       
"""
"""
print(txt.isalnum())            #result : False.    Bcz in 'txt' variable other than alphanumeric characters are present.

stat1 = "Mynameisabdul1234"
print(stat1.isalnum())                  #result : True.
print(stat1.isalpha())                  #result : False.
print(stat1.isascii())                  #result : True.
print(stat1.isdecimal())                #result : False.
print(stat1.isdigit())                  #result : False.
"""


"""
What is Tuple ?
    Definition : In python tuple is a built-in data structure that stores a collection of items in a single variable.
                Tuple is ordered and unchangeable. Tuples are immutable just like Strings.We can't make changes in
                the tuple, but we can have duplicate values in tuple as well.
                Tuples are defined by enclosing elements in parentheses(), separated by a comma(,).
                Tuple object can include elements separated by comma without parentheses().
                ex : name = 'ABDUL', 'KHADAR', 'Bangalore', 'August'
"""
# Tuple can not be declared with a single element unless followed by a comma(,).
names = ('STEVE')   # it is not tuple ...bcz there is no comma after one object, it is a string.
name = ('steve',)   # it is tuple with single element.
print(type (name))      #Result : <class 'tuple'>