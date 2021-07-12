#to print all +ve numbers within range
n=int(input("Enter number of numbers "))
list=[]
for i in range(0,n):
	list.append(int(input("Enter number ")))
print(list)
for j in list:
 	if j<0:
 		continue;
 	print(j)