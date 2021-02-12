# largest continous subarray
from sys import maxsize
def largest(arr):
    max_curr,max_so_far=0,float('-inf')
    for i in range(len(arr)):
        max_curr+=arr[i]
        max_so_far=max(max_so_far,max_curr)
        if max_curr<0:
            max_curr=0
    print(max_so_far)

if __name__ == '__main__':
    arr=[-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    largest(arr)