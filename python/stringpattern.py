#read a string from user and display the following pattern
#input = abc
#output:
#aaa
#bb
#c

string=input("Enter the string")
n=len(string)
for i in range(n):
    print(string[i]*(n-i))
