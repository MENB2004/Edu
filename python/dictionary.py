#dictionary
'''{key: value,ley:value},unordered key must be unique, immutable type value can be repeated'''

d1={}
d2=dict()
fruits={'a':"apple,avacado",'b':'banana'}
print(fruits)
#access
print("first ele",fruits['a'])
#adding pairs
fruits['k']="kiwi"
#updating
fruits['b']="berry"
print(fruits)
#deletion
del fruits['b']
#dict.pop(key),dict.clear()
fruits2={'m':'mango','p':'papaya'}
fruits.update(fruits2)
print(fruits)
