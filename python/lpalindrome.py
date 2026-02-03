#read a list from user and check if its palindrome or not

lst=eval(input("Enter the list: "))
print(lst)
print(type(lst))
if lst==lst[::-1]:
    print("Palindrome")
else:
    print("not palindrome") 
