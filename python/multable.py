#create a python fn named multable which takes 2 arguments m and n display table of m upto n times

#multable(2,5)
#1x2=2
#2x2=4
#3x2=6
#4x2=8
#5x2=10

m=int(input("Enter a number : "))
n=int(input("Enter another number : "))
print("Multable")
def multable(m,n):
    for i in range(1,n+1):
        print(f"{i}x{m}={i*m}")
multable(m,n)
