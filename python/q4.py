# create a list of marks by reading 5 integer values from user

marks=[]
n=int(input("Enter the number of marks: "))
for i in range(n):
    mark=int(input("Enter the marks : "))
    marks.append(mark)
print(marks)

#increse marks by 5 for those who scored less than 20
for i in range(0,len(marks)):
    if marks[i]<20:
        marks[i] = marks[i]+5
print(marks)
