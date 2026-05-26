# a = 15
# b = 20.5
# c = 12+25j
# d = 4
# e = 6
# print(a, 'is type of ', type(a))
# print(b, 'is type of ', type(b))
# print(c, 'is type of ', type(c))
# print('Quotient of a/b is ', a/b)
# print('Floored Quotient of a/b is', a//b)
# print('Reminder of b%a', b % a)
# print('Power e**d', e ** d)
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))
# print(id(e))
# print(dir(a))
# print(a.bit_count())
#print(b.bit_count())   # Result : AttributeError: 'float' object has no attribute 'bit_count'
#print(c.bit_count())   # Result : AttributeError: 'complex' object has no attribute 'bit_count'
# print(d.bit_count())
# print(e.bit_count())
# print(e.bit_length())        # Result : 3
# print(a.bit_length())        # Result : 4
# print(d.bit_length())        # Result : 3
# """print(c.bit_length())       # Result : AttributeError: 'float' object has no attribute 'bit_count'
# print(b.bit_length())       # Result : AttributeError: 'float' object has no attribute 'bit_count'
# """
# print(c.conjugate())        # Result : (12-25j)
# print(d.conjugate())        # Result : 4
# print(b.conjugate())        # Result : 20.5
# print(a.conjugate())        # Result : 15
# print(e.conjugate())        # Result : 6
# print(a.to_bytes())         # Result : b'\x0f'
# #print(b.to_bytes())         # Result : AttributeError: 'float' object has no attribute 'to_bytes'
# #print(c.to_bytes())         # Result : AttributeError: 'Complex' object has no attribute 'to_bytes'
# print(d.to_bytes())          # Result : b'\x04'
# print(e.to_bytes())          # Result : b'\x06'
#
# print(a.as_integer_ratio())     # Result : (15, 1)
# print(b.as_integer_ratio())     # Result : (41, 2)
# #print(c.as_integer_ratio())     # Result : AttributeError: 'complex' object has no attribute 'as_integer_ratio'
# print(d.as_integer_ratio())     # Result : (4, 1)
# """ So 'as_integer_ratio()' function is not applicable to only complex int data types"""
#
# print(a.imag)       # Result : 0
# print(b.imag)       # Result : 0.0  result also written in float int data type
# print(c.imag)       # Result : 25.0
# print(d.imag)       # Result : 0
#
# print(a.real)       # Result : 15  It will print real part of number
# print(b.real)       # Result : 20.5
# print(c.real)       # Result : 12.0
# print(d.real)       # Result : 4

#print(len(a))       # Result : TypeError: object of type 'int' has no len()

f=8
g=5
print(f.bit_length())
print(g.bit_length())

a= 10675.5529
b= 0.00
print(a*b)

xyz = 122
print(id(xyz))
xyz = 187
print(id(xyz))
print(id(xyz))