"""
What is Tuple ?
    Definition : In python tuple is a built-in data structure that stores a collection of items in a single variable.
                Tuple is ordered and unchangeable. Tuples are immutable just like Strings.We can't make changes in
                the tuple, but we can have duplicate values in tuple as well.
                Tuples are defined by enclosing elements in parentheses(), separated by a comma(,).
                Tuple object can include elements separated by comma without parentheses().
                ex : name = 'ABDUL', 'KHADAR', 'Bangalore', 'August'
                when the data is not going to be changed throughout the programme execution that time we are using tuples.
"""
# Tuple can not be declared with a single element unless followed by a comma(,).
names = ('STEVE')   # it is not tuple ...bcz there is no comma after one object, it is a string.
name = ('steve',)   # it is tuple with single element.
print(type (name))      #Result : <class 'tuple'>
names2 = 'ABDUL', 'KHADAR', 'RAVI', 'UPENDRA',
print(type(names2))     #Result : <class 'tuple'>
print(dir(names2))      #Result : '__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__',
                        # '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
                        # '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
                        # '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__',
                        # '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']



"""
By using import keyword class we can check what are the keywords present in python
"""
import keyword

print(keyword.kwlist)   #'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
                        # 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
                        # 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
                        # 'try', 'while', 'with', 'yield'


count = 1

while count<= 3:
    print(count)
    count +=1