#s=input("Enter the letter")
#if(s=='a' or s=='A'):
#    print("Its is Vowel")
#elif(s=='e' or s=='E'):
#    print("Its is Vowel")
#elif(s=='i' or s=='I'):
#    print("Its is Vowel")
#elif(s=='o' or s=='O'):
#    print("Its is Vowel")
#elif(s=='u' or s== 'U'):
#    print("Its is Vowel")
#else:
#    print("Its is not Vowel")


ch=input("Enter a character: ")
ch=ch.lower()
if ch in "aeiou":
    print("Vowel")
else:
    print("Not Vowel")
