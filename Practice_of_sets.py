

"""
Q) What is a Set?
    In Python Set is type of Data Structure to store the collection of data.
    Set is unordered, with collection of unique elements.That means Set won't allow Duplicates.
    Duplicates are automatically removed.Set is unordered means, elements in a set do not have a defined order,
    their indexes can vary, So items/elements can not be accessed by indexes.
    We can create set by using curly brackets {}.
    Set is a Mutable, we can add or remove the elements after creation, the individual elements in a set
    can not be changed by directly.
    A set can have any number of items and that may be of different datatypes(like string, int, tuple).
    But a set can not have Mutable datatypes like List, Dictionary and set as its elements.
  Creating a set:
  set1={1,2,3,'Abdul',"khadar","true"}

Q) What is Frozenset in Python?
    In python frozenset is an immutable version of set. Regular set is mutable collection of unordered elements.
    A frozenset is cannot be modified after its creation. This immutability makes frozenset objects hashable,
    which means they can be used in context.

Example :
        my_list =[1,2,3,4,52,3,42,4,2,1,3]
        my_frozenset=frozenset(my_list)
        print(my_frozenset)                 #result : frozenset({1, 2, 3, 4, 42, 52})
"""
set1={1,2,3,'Abdul',"khadar","true"}
set1.add(4)
print(set1)             # result : {1, 2, 3, 4, 'khadar', 'Abdul', 'true'}
set2=set1.add("Bengaluru")
print(set2)             # result : None, bcz add function in set, it modifies the value in set, but not return the
                                  # modified set. when set2 is assigned the result of set1.add("Bengaluru),
                                  # it receives None.
prime_numbers = {2,3,5,7,11}
prime_numbers.add(13)
print(prime_numbers)                # result : {2, 3, 5, 7, 11, 13}
"""
add() Method :
        This method add a given element to set. If given element is already exists it won't add.
        Also you won't get back a set if you use "add()" when creating a set object.
        "nonValue = setObject.add()"
        The above statement doesn't return a reference to the set but 'None', 
        because the statement returns the return type of add which is None.
        add() method does not return any value, it return as 'none'.
        
"""
print(dir(set1))                #result : ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__',
                                        # '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
                                        # '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__',
                                        # '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__',
                                        # '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__',
                                        # '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__',
                                        # '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference',
                                        # 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint',
                                        # 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update',
                                        # 'union', 'update']


empty_set = set()
empty_object = {}
print(type(empty_set))                  # result : <class 'set'>
print(type(empty_object))               # result : <class 'dict'>

"""
Note : Creating a empty set in a python is little bit tricky. To make set without elements, then use "set()" function.
       If you use curly brackets {} then it will treated as "Empty Dictionary" in python.
"empty_set" - an empty set created by using "set()" function
"empty_dictionary" - an empty dictionary created using "{}" curly brackets.
"""

"""
update() Method :  This method is update the current set by adding the iterable elements from another sets (or
                   any other iterable).
                   If an item present in both sets, only one appearance will be present in updated set.
                   you can use "|=" ("pipe equals" or "BitwiseOR equals" operator)
                
"""
set10 = {'a','b','c'}
set11 = {13,'bengaluru',24.7590,(12,'b',496) }
#set10.update(set11)
set10 |= set11
print(set10)                #result : {'bengaluru', 'a', (12, 'b', 496), 24.759, 'c', 'b', 13}

word_set = {"computer","Laptop", "Mobiles","Tablets"}
OS_sets = {"Windows","Linux","MAC Os", "Simbion", 'Android', "FunTouch Os", "Oxygen Os"}
mobiles = {"Samsung", "Vivo", "Apple","Oneplus","Sony", "Xiaomi", "IQoo"}
OS_sets.update(word_set,mobiles)
print(OS_sets)          #result : {'Linux', 'Simbion', 'IQoo', 'Vivo', 'Android', 'Apple', 'Laptop', 'computer',
                                    # 'Windows', 'Mobiles', 'Xiaomi', 'Samsung', 'Tablets', 'MAC Os', 'FunTouch Os',
                                    # 'Sony', 'Oneplus', 'Oxygen Os'}
mobiles |= OS_sets | word_set
print(mobiles)           #result : {'Vivo', 'Mobiles', 'computer', 'IQoo', 'Sony', 'Xiaomi', 'Simbion', 'Samsung',
                                    # 'Linux', 'Oneplus', 'Tablets', 'FunTouch Os', 'Apple', 'Laptop', 'Oxygen Os',
                                    # 'MAC Os', 'Windows', 'Android'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"cherry", "micra", "bluebird"}
x.update(y,z)
print(x)                    #result : {'micra', 'bluebird', 'microsoft', 'banana', 'apple', 'cherry', 'google'}
                            # Here duplicates are removed and considered as single element
y|=x|z
print(y)                    #result : {'bluebird', 'cherry', 'banana', 'microsoft', 'google', 'micra', 'apple'}


"""
Use  '|=' pipe equals to or Bitwise OR equals to operator instead of update() function. Using this we can join,
or insert more than one set.
"""

a = {1,2,3,4,5}
a.update(['Hello', 'Doctor'])           # result : {1, 2, 3, 4, 5, 'Hello', 'Doctor'}
print(a)
a.update("Abdul", "Khadar")
print(a)                                # result : {1, 2, 3, 4, 5, 'Hello', 'd', 'r', 'u', 'l', 'h', 'a', 'Doctor', 'A', 'b', 'K'}


"""Copy() Method :
                Copying sets in Python refers to creating a new set that contains the same elements as an existing set.
                copying ensures that changes made to the copied set do not affect the original set, and vice versa.
                There are different methods for copying a set in python, including using the copy() method, or the 
                set() function or set comprehension. 

Copy sets using the copy() Method :
                This method is used to create a shallow copy of a set object.
                A shallow copy means that the method creates a new collection object, but does not create copies 
                of the objects contained within the original collection. Instead, it copies the references 
                to these objects.

"""

OG_set = {"Abdul",1,2,"Khadar"}
copied_set = OG_set.copy()
print("Copied_set =", copied_set)           #result : Copied_set = {1, 2, 'Khadar', 'Abdul'}
copied_set.add(3)
print("OG_set =",OG_set)                    #return : OG_set = {1, 2, 'Khadar', 'Abdul'}
print("copied_set =",copied_set)            #return : copied_set = {1, 2, 3, 'Abdul', 'Khadar'}

"""
copy sets using set() function : 
"""

set1 = {88,46,"Flight", "AirIndia","Boing714",515411}
set2 = set(set1)
print("SET2 :",set2)
set1.add("Airbase")             #result : SET2 : {515411, 'Boing714', 88, 'AirIndia', 'Flight', 46}
print("SET1 :",set1)            #result : SET1 : {515411, 'Boing714', 88, 'AirIndia', 'Airbase', 'Flight', 46}
print("SET2 :",set2)            #result : SET2 : {515411, 'Boing714', 88, 'AirIndia', 'Flight', 46}


"""
set comprehension method:
                set comprehension method provides a concise way to create a new sets in python. While it's commonly
                used for transforming or filtering elements, it can also used to be creating a copy of an existing set.
syntax : 
        "new_set = {element for element in original_set}"
"""
"copying set by using comprehension method"
setA = {23, 25, 27, 29}
setB = {x for x in setA}
print("SET B :",setB)             # result : SET B : {25, 27, 29, 23}

"Transforming above set by using comprehension Method"
# squiring the elements of setA
squaring_setA = {x**2 for x in setA}
print(squaring_setA)            # result : {841, 625, 729, 529}


"""Filtering set by using comprehension method"""

numbers = {234,24,6,4,456,563,5,34,356,3,667,756,758,585,3235,35,363,457,4564,35}
mod3 = {x for x in numbers if x % 3 == 0 }
print("Division of 3 numbers are :",mod3)       #result : Division of 3 numbers are : {3, 6, 456, 585, 234, 363, 756, 24}
mod5 = {x for x in numbers if x%5==0}
print("Division of 5 numbers are :",mod5)       #result : Division of 5 numbers are : {585, 3235, 5, 35}
mod2 = {x for x in numbers if x%2==0}
print("Numbers with divisible 2 =",mod2)        #result : Numbers with divisible 2 = {34, 4, 356, 6, 456, 234, 4564, 756, 758, 24}

"""
NOTE : 
    When simply copying a set without any transforming or filtering then use 'set.copy()' or 'set(original_set)'
    is more explicit and often preferred for clarity. Set comprehension is particularly useful when you need to 
    perform operations on elements while creating the new set.
"""

"""
Discard() method :
        This method is used to remove the element from a set if it id present in a specified set.
        If element is not present in set it won't rise a error and set will remain unchanged.
        When you unsure whether the element is exist or not this method is safer alternative of "remove()"
        method. 
"""
my_set = {"Adlafn","dleghw", 2,5,46,5}
my_set.discard(46)
print(my_set)                   #result: {'Adlafn', 2, 5, 'dleghw'}
my_set.discard(4457)
print(my_set)                   #result : {2, 'dleghw', 5, 'Adlafn'} here it won't rise an error.

"Alternative method to remove safer of an element, if it is present or not"
if 33 in my_set:
    my_set.discard(33)
print(my_set)                   #result : {2, 'dleghw', 5, 'Adlafn'}
if "Adlafn" in my_set:
    my_set.discard('Adlafn')
print(my_set)                   #result : {2, 'dleghw', 5}
"""
Remove() Method :
         This method is used to remove element form the set. If element is present it will removes it.
         If element is not found then it will rise KeyError exception.

In Discard() method no error will raised if element is not found in set. this is the main difference b/w
remove() method and discard() method.
"""
my_set.remove(5)
print(my_set)               #result : {2, 'dleghw'}
try:
    my_set.remove(66)
except KeyError as e:
    print(f"Error : {e}")       #result : Error : 66

"Remove multiple elements from set :"

removeble_numbers = {5,34,356,3,667,756,758}
for elem in removeble_numbers:
    numbers.remove(elem)

print(numbers)           #result : {4, 6, 456, 585, 457, 4564, 24, 3235, 35, 234, 363, 563}

"Remove the element by using comprehension method"

numbers = {x for x in numbers if x>=100}
print(numbers)      #result : {3235, 456, 585, 457, 234, 363, 563, 4564} here removing below 100 numbers
numbers = {x for x in numbers if (x<400)^(x<600)}
print(numbers)      #result :  {456, 585, 563, 457}   here output was in between 400 and 600

"""
Pop() method:
        pop() method is used to remove and return an arbitrary element from a set. 
        If the set is empty it raises a 'KeyError'.
"""

set_obj = {"Abdul","set",25,636,(1,3,4325,'ACF'),54.87}
print(set_obj.pop())           #result : (1, 3, 4325, 'ACF')    its return the popped item


while set_obj:
    popped_item = set_obj.pop()
    print(popped_item)
    print("Updated_set :", set_obj)
                                        #result :54.87
                                        #Updated_set : {25, 'set', 636, 'Abdul'}
                                        #25
                                        #Updated_set : {'set', 636, 'Abdul'}
                                        #set
                                        #Updated_set : {636, 'Abdul'}
                                        #636
                                        #Updated_set : {'Abdul'}
                                        #Abdul
                                        #Updated_set : set()

                                        #Process finished with exit code


empty_set = set()
try :
    empty_set.pop()
except KeyError as A:
    print("Error:", A)          #result : Error: 'pop from an empty set'

"""
clear() method:
            This method is used to remove all elements from a set effectively making it an empty set.
"""

set101 = {"as;fms;dvm;m", 'dfbkb',234,2463}
set101.clear()
print(set101)                   #result: set()

list_of_sets = [{1,34,25},{23,574,24},{232,753,354,456},{"Abdul","khadar","python"}]
for s in list_of_sets:
    s.clear()

print(list_of_sets)             #result : [set(), set(), set(), set()]

"""
difference() Method:
            This method is used with sets to find the elements that are present in the first set but not in any
            other sets provided as arguments.Its returns a new set containing these unique elements.
How it works:
            When set1.difference(set2) is called, the method iterates through set1 and includes only 
            those elements that are not found in set2 in the resulting new set. This is analogous to the 
            mathematical set difference operation (A - B).
            
Syntax:
        "setA.difference(setB,setC,setD,.....)"
"""
pra_set1 = {23,325,643,34,645,678,33}
pra_set2 = {643,645,647,325,33,23}
pra_set3 = set()
result = pra_set1.difference(pra_set2)
print(result)                   #result : {34, 678}
result1 = pra_set1-pra_set2
print(result1)                  #result : {34, 678}
result2 = pra_set2.difference(pra_set3)
print(result2)                  #result : {33, 643, 23, 325, 645, 647}
setA1 = {1,2,3,45,6,7,5,58}
setA2 = {2,3,4,5,6,7,8,9}
setA3 = {3,4,5,6,23,12,45}
result3 = setA1.difference(setA2,setA3)
print(result3)                   #result: {1, 58}
result4 = pra_set1.difference(setA1)
print(result4)                  #result : {33, 34, 643, 325, 645, 678, 23}


"""
Difference_update() method:
            The set difference_update() method is used to to remove elements from the set that are also present 
            in one or more specified sets by altering the original sets.
            
        * difference() method will return a new set , where as difference_update() method is directly update the 
          original set. It efficiently updates the set by iterating through the elements of specified set and 
          removing any matching elements from the original set.
"""
"Examples"

pra_set1 = {23,325,643,34,645,678,33}
pra_set2 = {643,645,647,325,33,23}
pra_set1.difference_update(pra_set2)
print(pra_set1)             #result :{34, 678}

my_set1={1,2,3,4,5}
my_set2={5,6,7,8,9}
my_set3={10,11,12,13,14,3,5,8}
my_set1.difference_update(my_set2,my_set3)
print(my_set1)          #result: {1, 2, 4}
my_set4=set()
my_set2.difference_update(my_set4)
print(my_set2)          #result : {5, 6, 7, 8, 9}

"""
set intersection():
        This method is used to find all common elements, compare between two or more sets. It will return 
        a new set containing only the elements that are present in all the sets that are being compared.
                                            or 
        Alternatively we can use '&'(and) operator to achieve the same result.                                  

Syntax :
        "set1.intersection(set2, set3,set4,....)"
"""
a={"Abdul","Khadar",6,8,94}
b={12,24,6,94,25,"Khadar",8}
c={"Abdul", 'python',25,12,6,8}
result5=a.intersection(b,c)
print(result5)          #result: {8,6}

d={"Abdul","Khadar",6,8,94}
e={12,24,6,94,25,"Khadar",}
f={"Abdul", 'python',25,12}
result6=d.intersection(e,f)
print(result6)          #result : set()   here no common element present in 3 sets
result7=d&e
print(result7)          #result : {94, 6, 'Khadar'}
print(e&f)              #result : {25, 12}


"""
Set intersection_update() method :
            This method is use to update a set with intersection of itself and one or more other sets.
            This means it modifies original set to contain only elements that are present in all the sets involved.
            This method is useful for filtering a set based on the common elements it shares with other elements.

Syntax :
        "set1.intersection_update(set2,set3,set4,.....)"            
"""
x={1,2,3,4,5,6,7,8}
y={34,46,6,72,2,5,14,5,67,4,8,9}
z={24,14,5,6,7,89,32,234,21,2,7,4,3,8,9,34}
print(x.intersection_update(y,z))     #result : None
x.intersection_update(y,z)
print(x)                                  #result : {2, 4, 5, 6, 8}

# If you are apply intersection_update() b/w list and set result will be return as set
x2a={1,3,4,5,6,"ABDUL","KHADAR",23,24,25}
x2b=['ABDUL',"KHADAR",13,4,5,6,7,8,9]
x2a.intersection_update(x2b)
print(x2a)                      #result :{4, 5, 'KHADAR', 6, 'ABDUL'}
x2c={"khadar",1,3,5,7,9,0}
#x2b.intersection_update(x2c)
#print(x2b)                      #result : AttributeError: 'list' object has no attribute 'intersection_update'

"Example"
def commonEle(arr):
    resultent =set(arr[0])

    for curr in arr[1:]: # slicing
        resultent.intersection_update(curr)
    return list(resultent)

if __name__ == "__main__":
    nested_list=[['a','b','d','u','l'],['k','h','a','d','a','r'],['a','d','d','r','e','s','s']]
    out = commonEle(nested_list)
if len(out) > 0:
    print(out)
else :
    print("NO COMMON ELEMENTS ARE FOUND")
# above program output is : ['d','a']


"""
set isdisjoint() method:
            This method is used to check if two sets have no common elements. It returns true if two sets are 
            disjoint, that means there is no intersection (or intersection is empty) b/w two two sets,
            otherwise it returns False.
            This method can be used with any other iterable not just with set. If any element in the 
            other set or any iterable is found in hte original set then isdisjoint() method returns false,
            otherwise it will returns true.

Syntax:
        "set1.isdisjoint(set2,...)"
"""
a={"Abdul","Khadar",6,8,94}
b={12,24,6,94,25,"Khadar",8}
print(a.isdisjoint(b))                  #result : False
pra_set1 = {23,325,643,34,645,678,33}
pra_set2 = {643,645,647,325,33,23}
print(pra_set2.isdisjoint(b))           #result : True
my_list1=['ABDUL',"KHADAR",13,4,5,6,7,8,9]
print(b.isdisjoint(my_list1))           #result : False
print(pra_set1.isdisjoint(my_list1))    #result : True

if a.isdisjoint(my_list1):
    print("There is NO common Elements in Both sets. So they are Disjoint Sets")
else:
    print("There is an Intersection between Both sets.")
                                        #result : There is an Intersection between Both sets.

"""
Set issubset() method :
        This method is used to check whether all elements of one set i.e the subset are contained with in the 
        another set i.e superset. It returns true if every element of the subset is in the superset otherwise
        it will returns false.
        This method can be used with other iterables like lists, tuples or strings as well.
        It is useful for verifying if one collection is completely contained within another,
        which is a common operation in various algorithms and data analysis tasks.

Syntax:
    "set.issubset(iterable)"
"""
exam1={1,2,3,4,5}
exam2={1,2,3,4,5,6,7,8}
print(exam1.issubset(exam2))            #result : True
print(exam2.issubset(exam1))            #result : False
my_frozenset=frozenset({4,5,6})
print(exam2.issubset(my_frozenset))     #result : False
print(my_frozenset.issubset(exam2))     #result : True

"""
Symmetric_difference() method :
                This method is used to obtain elements present in either of two sets but not in both.

Syntax : 
    'set.symmetric_difference(other_set)'
"""
obj1={1,3,5,6,7,9,2}
obj2={1,2,3,4,5}
result8=obj1.symmetric_difference(obj2)
print(result8)              #result :{4, 6, 7, 9}
obj3={"apple","Orange","papaya","banana","Mangoes","Guava"}
obj4={1,2,3,"Guava","pineapple","Orange","papaya","Grapes"}
obj5={"Orange","apple","papaya","Guava",1,2}
result9=obj3.symmetric_difference(obj4).symmetric_difference(obj5)
print(result9)                      #result: {3, 'pineapple', 'Grapes', 'Orange', 'Mangoes', 'banana', 'papaya', 'Guava'}
obj6={1,2,3,4}
obj7={4,5,6,7}
obj8={6,7,8,9}
result10=obj6.symmetric_difference(obj7).symmetric_difference(obj8)
print(result10)                     #result : {1, 2, 3, 5, 8, 9}

"""
symmetric_difference_update()  method:
                This method is used to modifies the set by removing the common elements of both sets and 
                inserting the elements that are exclusive to either set. 
                It does not return any new set, but modifies the original set itself. This operation is 
                similar to XOR operation in mathematical boolean logic.
                
Syntax:
    "set1.symmetric_difference_update()"                 
"""
obj3={"apple","Orange","papaya","banana","Mangoes","Guava"}
obj4={1,2,3,"Guava","pineapple","Orange","papaya","Grapes"}
obj3.symmetric_difference_update(obj4)
print(obj3)             #rersult : {1, 2, 3, 'Grapes', 'apple', 'banana', 'Mangoes', 'pineapple'}

exam1={1,2,3,4,5}
exam2={1,2,3,4,5,6,7,8}
exam1.symmetric_difference_update(exam2)
print(exam1)            #result : {6, 7, 8}


"""
set union() method :
        Set union() method is used with sets to return a new set containing all the unique elements from the 
        original set and all specified sets. It combines the elements from multiple sets without including 
        duplicates.
        We can use the '|' operator as an alternative to this method.The original sets remain unchanged as 
        union() produces a new set. It is commonly used to merge sets and find the overall collection of 
        unique items from multiple sources.

Syntax:
        "set1.union(set2)"
"""
exam3={1,2,3,4}
exam4={3,4,56,6,2,3,7}
exam5={"Khadar",12,3,4,2,4,5,6,7}
result11=exam3.union(exam4)
print(result11)                 #result : {1, 2, 3, 4, 6, 7, 56}
result12=exam5.union(exam3,exam4)
print(result12)                 #result : {1, 2, 3, 4, 5, 6, 7, 'Khadar', 12, 56}
union_set1= exam1 | exam2
print(union_set1)               #result : {1, 2, 3, 4, 5, 6, 7, 8}
union_set2 = exam1 | exam2 | exam3
print(union_set2)               #result : {1, 2, 3, 4, 5, 6, 7, 8}