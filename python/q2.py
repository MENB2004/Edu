#read 2 strings and convert them to a single by appenfing alternative characters. Do only if both string are of equal size.
#input1-abcde
#input2-pqrs
#output-apdqcrds

# sourcery skip: use-join
str1=input("Enter string 1: ")
str2=input("Enter string 2: ")
m=len(str1)
n=len(str2)
if(m==n):
    str3=""
    for i in range(m):
        str3 += str1[i] + str2[i]    
    print("Output = ", str3)
else:
    print("Strings are not of same length")
