'''Read a string from user and convert index as key, items as value
input- "abc"
output-{0:'a',1:'b',2:'c'}
'''
d=dict()
s=input("Enter any string")
for i in range(0,len(s)):
    d[i]=s[i]
print(d)
