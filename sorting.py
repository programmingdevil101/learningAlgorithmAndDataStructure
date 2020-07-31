# This algorithm takes first two element and checks if first element is greater than second element.
# If so it swaps. then it checks the 2nd and 3rd and does the same and so on.
# To return fully sorted array it have to loop through a nested loop of n, where n is length of array.
# So the time complexity of this algorithm is O(n^2).
# We can optimize this algorithm  to have best case time complexity of O(n).
# The optimization is that we declare a variable is sorted and set it to True and re-assign it to false 
# inside the if statement inside inner loop.
# Best Case O(n)
# Worst Case O(n)
def bubble_sort(arr):
	for i in range(len(arr)-2):
		is_sorted = True
		for j in range(len(arr)-1):
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
				is_sorted = False
		if is_sorted:
			print(f"Itered {i+1} times")
			return arr 
	return arr




#
#
def merge_sort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		left = arr[:mid]
		right = arr[mid:]
		merge_sort(left)
		merge_sort(right)
		i = j = k = 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i+=1
			else:
				arr[k] = right[j]
				j+=1
			k+=1
		while i < len(left):
			arr[k]=left[i]
			i=i+1
			k=k+1

		while j < len(right):
			arr[k]=right[j]
			j=j+1
			k=k+1
	return arr
def quick_sort(arr, start , end):
	if start < end :
		PI = partition(arr, start, end)
		quick_sort(arr, start, PI-1)
		quick_sort(arr, PI+1, end)
	return arr

# helper function for quick sort
def partition(arr, start, end):
	pivot = arr[end]
	PI = start
	for i in range(start, end):
		if arr[i] <= pivot:
			arr[i], arr[PI] = arr[PI], arr[i]
			PI +=1
	arr[PI], arr[end] = arr[end], arr[PI]
	return PI
def test_sort(arr, low, high):
	pass


a = []
for i in range(10000):
	a.append(random.randint(0, 10000))



