# create a python function that will accept any number of integer value and return the square of the smallest value
# smallsq(2,3,4) - 4
#smallsq(7,8)- 49
#smallsq(45,5,90,10)- 25

def smallsq(ar):
    j=min(ar)
    sq=j*j
    print(sq)
n= int(input("Enter the total numbers : "))
ar=[]
for i in range (n):
    k = int(input("Enter the number: "))
    ar.append(k)
smallsq(ar)
