#multiple of 5 & 6 for +ve numbers
num = int(input("Enter the number: "))
if(num>=0):
    if(num%6==0):
        if(num%5==0):
            print("Number is multiple of 5 & 6")
    else:
        print("Number not a multiple of 5 & 6")
else:
    print("Number is negative")
