#read check in time from student
#after 2 pm no attendence
print("enter the Age")
age=int(input("enter the Age"))
year=2025-age
if year>=2025:
     print("Gen Beta")
elif year>=2010:
    print("Gen Alpha")
elif year>=1997:
    print("Gen Z")
elif year>=1981:
    print("Gen Y")
else:
    print("Gen X or previous")
