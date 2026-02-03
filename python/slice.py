#slicing
fruit="pineapple"
print(fruit[0])
#string[start:stop]
#string[start:stop:step]
print("slice1", fruit[:3])
#start 0, stop3, step1-> 0,1,2
print("slice1",fruit[3:6])
#start 3, stop6, step-> 3,4,5
print("slice1",fruit[3:])
#start 3, stop=len, step->3,4,5,6,7,8
print("slice1",fruit[2:7:2])
#start 2, stop 7 step->2,4,6
print("slice1",fruit[:3])
#start 0, stop 3, step->0,1,2
print("slice1",fruit[7:2])
#start 7, stop2, step 1
print("slice1",fruit[::2])
#start 0, stop 7 step-> 0,2,4,6
print("slice1",fruit[7:2:-1])
#start 7, stop 2 , step -> 7,6,5,4,3
print("slice1",fruit[0::-1])
