# return True global and local inversion are equal, False otherwise
# global inversion: 0<=i<j<N arr[i]>arr[j]
# local inversion: 0<=i<N arr[i]>arr[i+1]
# Given some permutaion of and arrat from 0 to n-1


def inversion(arr):
    for i in range(len(arr)):
        if abs(arr[i]-i)>1:
            return False
    return True

#arr=[0,2,1]
arr = [2,1,0]
print(inversion(arr))