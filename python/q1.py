#read check in time from student
#after 2 pm no attendence
print("enter the time of check in")
checkin=input("enter the time HH:MM")
hrs,mins=map(int,checkin.split(":"))

if hrs>=1 and hrs<7:
    hrs+=12
if hrs>=14:
    print("marked absent at ",hrs,":",mins)
else:
    print("marked present at ",hrs,":",mins)
