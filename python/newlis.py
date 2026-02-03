#adding values to a list
fruits=[]
#Method 1 -list.append(value)
fruits.append("apple")
fruits.append("grapes")
fruits.append(100)
print(fruits)
#Method 2 -list.extend(list)
fruits.extend(['banana','kiwi'])
print(fruits)
#Method 3- list.insert(ind,value)
fruits.insert(0,"mango")
print(fruits)
