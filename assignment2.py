import os
print(os.walk(top='python'))
for g,s,f in os.walk(top='python'):
    print(g)
    print(s)
    print(f)
