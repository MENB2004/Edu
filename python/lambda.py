#lambda functions
#lambda params:return

test=lambda name:print("hello ",name)
sq=lambda x:x**2
add=lambda x,y:x+y
nums=[2,3,4]
for i in map(sq,nums):
    print(i)

for i in map(lambda x:x**3,nums):
    print(i)
