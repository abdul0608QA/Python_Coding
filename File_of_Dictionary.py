"""
Q) What Is Dictionary?
        Python Dictionary is a datatype, and it can be used to stores the data as a "key:value" pairs.
        Dictionary is a mutable datatype, and it can be defined by curly brackets "{}". When we want map
        the data with key values that time we can use this datatype.
        Key should be unique,case-sensitive, and it is immutable, whereas values contains any datatype and its mutable
        and duplicate also.

   Example : D={key1:value1, key2:value2, key3:value3,....}
"""

# Examples :
"""
we can create dictionary by using dict() method
"""
personalInfo = dict(Name="ABDUL",age=30,Profession="Software Engineer",Location ="Bangalore")
print(personalInfo)         #result : {'Name': 'ABDUL', 'age': 30, 'Profession': 'Software Engineer', 'Location': 'Bangalore'}
"""
another method for creating dictionary is by using curly{} brackets
"""
dict1 = {'name':'Abdul', 'age':30, 'place':'Bangalore', 'Area': 'SpiceGarden'}
print(dir(dict1))           #Result : '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
                            #'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
                            #'__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__',
                            #'__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__',
                            #'__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
                            #'__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
                            #'setdefault', 'update', 'values']

# we can update or adding a key value pairs by two ways

dict1.update({'mail':'chittia06@gmail.com'})
print(dict1)       #result : {'name': 'Abdul', 'age': 30, 'place': 'Bangalore', 'Area': 'SpiceGarden', 'mail': 'chittia06@gmail.com'}
dict1['Number'] = 9398190322
print(dict1)       #result : {'name': 'Abdul', 'age': 30, 'place': 'Bangalore', 'Area': 'SpiceGarden', 'mail': 'chittia06@gmail.com', 'Number': 9398190322}
# these are the two methods to updates the items in a dictionary.

"""
Q)How to remove the values inside dictionary?
    By using pop() method can remove items in side a dictionary.
    It will take one argument as key and will remove that particular key value pair, and return the value.
"""
print(dict1.pop('Area'))       #result : SpiceGarden
print(dict1)                   #result :{'name': 'Abdul', 'age': 30, 'place': 'Bangalore', 'mail': 'chittia06@gmail.com', 'Number': 9398190322}
"""
Q) What is popitem() method ?
    popitem() method is , it will remove last item in the dictionary, and return key values as tuple.
"""
print(dict1.popitem())   #result : ('Number', 9398190322)  here last item key value pair is return as tuple.
print(dict1)             # result : {'name': 'Abdul', 'age': 30, 'place': 'Bangalore', 'mail': 'chittia06@gmail.com'}
"""
Q) Whats the difference b/w pop and popitem methods in Dictionary?
     Both pop() and popitem() methods are used to remove the items in dictionary. But the difference is pop() method
     you will give pkey as argument and will remove corresponding value of that key and return as value.
     But in popitem() method it will remove by default last item of the dictionary and return key value pair
     as tuple.
"""
"""
get() method:
        This method return the value of a specified key in argument, if it present in dictionary.
"""
print(dict1.get('age'))         #Result : 30
print(dict1.keys())             #result : dict_keys(['name', 'age', 'place', 'mail'])
                                # it will return all keys in form of List.
print(dict1.values())           #result : dict_values(['Abdul', 30, 'Bangalore', 'chittia06@gmail.com'])
                                # it will return all the values in the form of list.
"""
items() Method :
            It will return key value pair as tuples from iterable items. 
"""
print(dict1.items())        #result: dict_items([('name', 'Abdul'), ('age', 30), ('place', 'Bangalore'), ('mail', 'chittia06@gmail.com')])
# it will use in loop conditions example:

for k,v in dict1.items():
    if v == 'chittia06@gmail.com':
        print("Email is Verified")          # result : Email is Verified

"""
Q) What are the ways to update the Dictionary Values?
        There are Several Ways to update the Dict values.
        1.Direct Assignment Method(By using Square Brackets)
        2.By using Update() Method
        3.By using Merge (|=) operator
        
"""
"""
update () method:
        
"""
d1 = {1:'one',2:'Two',3:'Three'}
d2 = {'place':'Bangalore','area':'marathahalli'}
d1.update(d2)
print(d1)     # result :{1: 'one', 2: 'Two', 3: 'Three', 'place': 'Bangalore', 'area': 'marathahalli'}
d1[3]='three'
print(d1)       #result :{1: 'one', 2: 'Two', 3: 'three', 'place': 'Bangalore', 'area': 'marathahalli'}
e1 = {'A':"ABDUL",'B':"KHADAR"}
e2 = {'A':"ARAVAPPA GARI",'B':'ABDUL','C':"KHADAR"}
e1.update(e2)
print(e1)       #result : {'A': 'ARAVAPPA GARI', 'B': 'ABDUL', 'C': 'KHADAR'}
e1.update(A="A.")
print(e1)        #result : {'A': 'A.', 'B': 'ABDUL', 'C': 'KHADAR'}
e1.update(c="ARAVAPPA GARI")
print(e1)		 # result : {'A': 'A.', 'B': 'ABDUL', 'C': 'KHADAR', 'c': 'ARAVAPPA GARI'}
"""
Q) Is given dictionary is Valid or not valid?
"""
p1 = {1:'one', 2:'Two', 3: 'Three', 4:'Four', 1:'One'}  #result : Valid dictionary.
print(p1)           # result : {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
#This 'p1' dict is a valid dict but Key is won't allow duplicate, So here key "1" value is over write as 'One'.
#p2 = {['Animals', 'Humans']:"Predators", 'pets': "Dogs", "things":'Pens'} # result : Invalid Dict and gives
                                                                        #error as"TypeError: unhashable type: 'list'."
#Bcz here Hashable items are not allowed to use as keys. Hashable items means any iterable sequences and Immutable
# Sequences.
p3 = {(1,2):'one', 2:'two',3:'three',4:'Four'}      #result: It is valid Dict
                                                    #bcz here first key is a tuple, so tuple is immutable.Mutable datatypes
                                                    #are not allowed as keys
p4 = {1:['one','Two','three'],2:'two',3:'Three'}        #result: It's a Valid Dict
                                                        #Bcz mutable datatypes are allowed as values
