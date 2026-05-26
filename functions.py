# #First Function :
#
# employees = {"satyam":[35, 50000],
#
#              "shivam":[45, 60000],
#
#              "Bhaskar":[55,70000]}
# vals=employees.values()
# vals = [i[1] for i in vals]
# print(vals)
# lowest = min(vals)
# for k,v in employees.items():
#     if lowest in v:
#         print(k, lowest)
#
#
# # Second Function:
#
# input = [[1, 2, [3, 4]], [5, 6], [7, [8, 9]]]
# l = []
#
#
# def fun_nested_list(l1):
#     for i in l1:
#         if isinstance(i, list):
#             fun_nested_list(i)
#         else:
#             l.append(i)
#     return l
#
#
# print(fun_nested_list(input))
# mane="AbdUL KHadar"
# print(mane.casefold())

l = [1,2,3,4,5]
k=0

# [4,5,1,2,3]

def rotate_list(l,k):
    k=k%len(l)
    rl = l[-k:]+l[:-k]
    return rl

print(rotate_list(l,k))
# l = [1,5,7,-1]
# k=6
# def get_pairs(l, k):
#     pairs = []
#     for i in range(len(l)-1):
#         if l[i]+l[i+1]==k:
#             pairs.append([l[i],l[i+1]])
#     return pairs
#
# # print(get_pairs(l,k))
#
# l=[3,2,1,5,6,4]
# k=2
#
# def sort_list(l, k):
#     for i in range(len(l)):
#         for j in range(i, len(l)-i-1):
#             if l[j]>l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
#     return l[-k]
# print(sort_list(l,k))
fullname ="Abdul Khadar"
print(fullname.lower())
a=400
b=100
c=9800
d=240
e=300
f=200
print(a+b+c+d+e+f)
