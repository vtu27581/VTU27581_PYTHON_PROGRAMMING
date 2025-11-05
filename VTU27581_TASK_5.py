#product price sorting

#Bubble sort (Ascending)

def bubble-sort (arr):

n = len(arr)

for i in range(n):

max_idx= i

for j in range (iti,n):

If arr[i]>arr (max-idx):

max-idx=j

arr (i), arr (max-idx]=

arr (max-idx), arr[i]

return arr

#insertion sort (Ascending)

def insertion sort (arr)

for i in range (1,len(arr)):

key= arr[i]
j=i-1
while j>=0 ond arr(j)= key:

arr[i+1] = arr[i]
j==1
arr[j+1]=key

return arr

#Main program

prices=[250,120,300, 90, 150]

print("original prices:", prices)

Print ("Bubble sort (Ascending)", bubble_sort (prices.copy())

print ("selection sort(Descending):", selection_sort(prices.copy())

print("insertion sort(Ascending): ", insertion_sort (prices.copy())
