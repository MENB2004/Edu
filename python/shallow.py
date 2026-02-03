import copy
lst1=[1,[2,2],3,4]
lst2=lst1.copy()
lst2[0]=10
print(lst1)
#lst1 2nd value is affected
'''copy() is not affected for nested values'''
#deep copy
lst3=copy.deepcopy(lst1)
print(lst3)
lst3[1][0]=20
print(lst1)
