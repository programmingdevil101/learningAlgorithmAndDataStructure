import time
import random


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 13, 15, 14, 17, 11, 45, 333, 43, 35, 35, 65,7, 6, 4]
def binary_search(arr, value):
	arr = sorted(arr)
	start = 0
	mid = 0
	end = len(arr) - 1
	while start <= end:
		mid = (start + end)//2

		if value == arr[mid]:
			return mid
		if value < arr[mid]:
			end = mid - 1
		else:
			start = mid + 1

	return -1
	
a = []
for i in range(10000000):
	a.append(random.randint(0, 10000))
value = 27741
start = time.time()
v = binary_search(a, value)
timetaken = time.time()-start
print(v, timetaken)
f = open('Speed.txt', 'a')
f.write(f"Time taken by binary_search to search {value}(is_in: {value in a}) in array of {len(a)} items is {timetaken}s.\n")

