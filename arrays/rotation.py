# left rotation of an array

# juggling method
import math as ma
def right_rotation(arr,d):
    n=len(arr)
    gcd = ma.gcd(n,d)
    d=d%n
    for i in range(gcd):
        j=i 
        temp = arr[j]
        while True:
            k=d+j 
            if k>=n:
                k-=n 
            if k == i:
                break 
            arr[j]=arr[k]
            j=k 
        arr[j]=temp 
    print(arr) 

arr=[1,2,3,4,5,6,7,8]
d=4
right_rotation(arr,d)

# left rotation
