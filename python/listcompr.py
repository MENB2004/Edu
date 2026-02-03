#List Comprehension
'''It is a shortend way of creating list'''
#list with value 1-50
lst=[x for x in range(1,51)]
print(lst)
nums=[1,2,3,4,5,6,7]
nums2=[v for v in nums[::2]]
print(nums2)
#[value for value in swquence cond]
even=[n for n in nums if n%2==0]
print(even)
