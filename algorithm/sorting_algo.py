# Insertion Sort

# Time Complexity: O(n^2)
def Insertion_sort(arr):
    for i in range(len(arr)):
        a=arr[i]
        
        # checking for left side and and insert the element to it's correct position
        j=i-1 
        while a<arr[j] and j>=0:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=a
    return arr

# Selection_Sort

# Time Complexity: O(n^2)
def Selection_Sort(arr):
    for i in range(len(arr)):
        mi=i

        # searching for next minimum element 
        for j in range(i+1,len(arr)):
            if arr[j]<arr[mi]:
                mi=j
        arr[i],arr[mi]=arr[mi],arr[i]
    return arr

# Bubble Sort

# Time Complexity: O(n^2)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    

# Merge Sort

# divide and conqure strategy
# Time Complexity: O(nlogn)
def merge_sort(arr):
    if len(arr)>1:
        mid=(len(arr))//2
        left=arr[:mid]
        right=arr[mid:]
        merge_sort(left)
        merge_sort(right)

        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1

        while i<len(left):
            arr[k]=left[i]
            i,k=i+1,k+1

        while j<len(right):
            arr[k]=right[j]
            j,k=j+1,k+1

# Quick Sort

# Worst Case: O(n^2) when array is already sorted
# Average Case: O(nlogn)
def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1


def quick_sort(arr,low,high):
    if low<high:
        j=partition(arr,low,high)
        quick_sort(arr,low,j-1)
        quick_sort(arr,j+1,high)

if __name__ == '__main__':
    arr=[9,8,7,6,2,4,3,5]
    
    quick_sort(arr,0,len(arr)-1)
    #bubble_sort(arr)
    #merge_sort(arr)
    #Selection_Sort(arr)
    #Insertion_sort(arr)
    print(arr)