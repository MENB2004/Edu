'''

#Nested List
NL=[['arun','sem1',80],
    ['amal','sem2',70],
    ['anu','sem1',88]]
print(NL)
#display marks of amal?
print(NL[1][2])
#3rd index of 2nd list
NL[1][2]=77
print(NL)
print(NL[0][0][0])#a
print(NL[0][1][1])#e

'''


'''
lst1 & lst2 are refering to same memory
'''



lst1=[5,6,7]
lst2=lst1
lst3=lst1.copy()#shallow copy
lst1[0]=50
print(lst2)#[50,6,7]
print("lst2:",lst2)#[50,6,7]
print("lst3:",lst3)#[5,6,7]

