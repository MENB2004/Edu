'''Exception-Runtime Errors
exception handling
'''

'''
try:
    l=[]
    #print(L[10]
    print(1/0)
except IndexError:
    print("I', handling IndexError")
except Exception as e:
    print("I'm handling the exception")
    print("Exception: ",e)
'''

'''
try:
    print(1/1)
except Exception as e:
    print("I'm handling the exception")
    print("Exception: ",e)
finally:
    print("I work always")
    #closing resouces,cleaning
'''

'''
try:
    d={'a':1}
    print(d['a'])
except Exception as e:
    print("There is an exception")
    print("Exception: ",e)
else:
    print("All good no exception")
finally:
    print("I work always")
    #closing resouces,cleaning

'''

'''
try:
    #for raising exceptions by the user
    raise KeyError("Key not found")
except Exception as e:
    print("There is an exception")
    print("Exception: ",e)
'''

try:
    #for raising exceptions by the user
    raise ValueError("Value not found")
except Exception as e:
    print("There is an exception")
    print("Exception: ",e)
