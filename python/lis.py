L=['a','b','c','d','e','f']
#delete- del list[index]
del L[0]
print("L after delete ",L)
#pop-list.pop(index)
L.pop()#removes the last ele
print("L after pop()",L)
L.pop(0)
print("L after pop(0)",L)
#remove- lsit.remove(value)
L.remove('d')
print("L after remove",L)
L.clear()
#del L- the list is deleted
