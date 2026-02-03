#read n from user diaplay all odd numbers between n to 1 in reverse order
n=int(input("Enter the number : "))
for i in range(n,0,-1):
    if(i%2!=0):
            print(i)
