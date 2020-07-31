import random

def euclidGCD(num1, num2):	
	while num1 != num2:
		if num1 > num2:
			num1 -= num2
		else:
			num2 -= num1
	return num1
def majority(arr):
 	m = None
 	i = 0

 	for j in range(len(arr)-1):
 		if i == 0:
 			m = arr[j]
 			i = 1
 		elif m == arr[j]:
 			i += 1
 		else:
 			i -= 1

 	return m	
#arr = [1, 3, 2, 2, 2, 4, 2, 2, 2, 5, 2, 7, 2, 2, 4, 4, 4, 4, 4]
#print(majority(arr)
arr = []
for i in range(10000):
	arr.append(random.randint(0, 10000))

print(23245 in arr)
