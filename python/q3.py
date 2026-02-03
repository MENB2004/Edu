#achieve the following using slicing
#input = abcdef
#output = cbadef

str1=input("Enter the input string")
n=len(str1)
m=round(n/2)-1
print("Output: ",str1[m::-1]+str1[n:m:-1])
