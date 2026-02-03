'''
Using list comprehension create a list of multiple of 5 between 200 and 50 in reverse order
'''
lst=[x for x in range(200,49,-5) if x%5==0]
print(lst)
