import sys

n=int(input())
arr=[int(x) for x in input().split(" ")]
num_Swaps=0

for i in range(n):
	for j in range(n-1):
		if arr[j]>arr[j+1]:
			temp=arr[j]
			arr[j]=arr[j+1]
			arr[j+1]=temp
			num_Swaps+=1

	if num_Swaps==0:
		break
print("Array is sorted in "+ str(num_Swaps)+" swaps.")
print("First Element: "+str(arr[0]))
print("Last Element: "+str(arr[len(arr)-1]))				
