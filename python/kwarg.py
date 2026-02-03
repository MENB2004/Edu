#keyword arguments
def studdetails(**args):
    print(args)

studdetails(name="arun",score=67)

def disp(n1,n2,*others):
    print("n1=",n1)
    print("n2=",n2)
    print("*others",others)

disp(10,20,40,50,60)

