
'''Read a lsit of users and create a frequency directory for the lsit{listvalue:count}
input L=[1,2,3,2,2,2,1,1,3,4]
output -{1:3,2:4,3:2,4:1}
'''
n=int(input("Enter the number of strings: "))
li = [ int(input()) for a in range(n)]
fre={}
for i in li:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1
print(fre)
