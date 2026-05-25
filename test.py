
"""
 Q) What is list?
        In Python List is a Collection of data. It is used to store multiple items in a single variable.
        List is Mutable, we can change the values after creation, or delete and add the duplicates in a List.
        List is Defined by using Square Brackets "[]". It has heterogeneous values.List is a one of 4 built-in Data types
        in python using for to store collection of data in a single variable, other three datatypes are Dictionary,
        Set and Tuple.
        When we say List is ordered, that means items in a list is defined ordered, that order can not be changed.
        If you want to add new items in a list that will be placed in end of the list.

Q) Why "List, Dictionary and Set" data types are Mutable and "Integer, Strings and Tuples" data types are Immutables?
        Here "List, Dictionary and Sets" are mutable Datatypes bcz if you change or add any new values in a these datatypes,
    after declare the that datatype, the Memory address location of the variable can not be changed.
        But in "Integer, Strings, Tuples" datatypes if you change or any modification is happened to the variable
    after declaration, the Memory address location of that variable is change. So that's why these are Immutable
    Datatypes.

"""
# Examples/Operations on List Data Types:

mylist1 = ["Abdul", "Khadar", 120, 180, 100, 90, ("friends", "animals", 'Tools'), "abdul533khadar@gmail.com"]
print (dir(mylist1))         # Result : '__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__',
                             # '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
                             #'__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
                             # '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
                             # '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
                             # '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append',
                             # 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse',
                             #  'sort'

print(type(mylist1))          # Result : <class 'list'>
print(id(mylist1))            # Result : 2314977906368
mylist1.insert(0, "work")       # Result : ['work', 'Abdul', 'Khadar', 120, 180, 100, 90, ('friends', 'animals', 'Tools'), 'abdul533khadar@gmail.com']
print(mylist1)
"""pop() method :
            It will remove the last element of the list and witten it.
"""
print(mylist1.pop())        #Result : abdul533khadar@gmail.com    here last value in the list item is "abdul533khadar@gmail.com",
                            #         and it's removed from list and written the removable item in console.
print(mylist1)              # Result : ['work', 'Abdul', 'Khadar', 120, 180, 100, 90, ('friends', 'animals', 'Tools')]
                            # after removing the last item in list remaining list will be printed.
"""
append() Method :
        This method is used for to add any value at the end of the list.
"""
mylist1.append('chittia06@gmail.com')
print(mylist1)              # Result : ['work', 'Abdul', 'Khadar', 120, 180, 100, 90, ('friends', 'animals', 'Tools'), 'chittia06@gmail.com']

# Sorting of List :
list1 = [34,2,5,225,252,435267,363,34,63,6]
list1.sort()
print(list1)         # Result : [2, 5, 6, 34, 34, 63, 225, 252, 363, 435267] here it printed as ascending order.

"""
Q) who to print the list in descending order?
     If given List is in unsorted or random first it will sort and then use reverse method by using flag as "True".
"""
# Example :
list2 = [43,346,453,135,2,46,3352,54,3,333,46]
list2.sort()
print(list2)                        # Result : [2, 3, 43, 46, 46, 54, 135, 333, 346, 453, 3352]
list2.sort(reverse=True)
print(list2)                        # Result : [3352, 453, 346, 333, 135, 54, 46, 46, 43, 3, 2]
"""
reverse() Method: it will just reverse the list whether the list is sorted or unsorted.
"""
list2.reverse()
print(list2)                        # Result : [2, 3, 43, 46, 46, 54, 135, 333, 346, 453, 3352]

#Index() method in List#
l= ['Apple', 'ball','cat','Doll','Elephant','Fan','Grapes']
print(type(l))      # result : <class 'list'>
print(l[1])         # result : ball
print(l[2][2])      # result : t
print(l[-3][-5])    # result : p
print(l[-1][0])     # result : G
print(l[-2][-1])    # result : n