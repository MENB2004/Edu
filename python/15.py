#read a list of n elements from user. Remove duplicate values from the list
values=[]
n=int(input("Enter the total number : "))
for i in range(n):
    value=int(input("Enter the values : "))
    values.append(value)
value_up=[]
for i in values:
    if i in value_up:
        continue
    else:
        value_up.append(i)
print(values)
print(value_up)

            
            
