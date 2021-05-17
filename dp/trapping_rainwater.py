# trapping rain water
# link: https://practice.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1#

def trappingWater(arr,n):
    #Code here
    if n<=0:
        return 0
    left_max = [0]*n
    right_max = [0]*n
    ans = 0
    
    # finding left maximum element
    left_max[0] = arr[0]
    for i in range(1,n):
        left_max[i] = max(left_max[i-1],arr[i])
    
    # finding right maximum element
    right_max[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        right_max[i] = max(right_max[i+1],arr[i])
        
    for i in range(n):
        ans = ans + min(left_max[i],right_max[i]) - arr[i]
    return ans

arr = [7,4,0,9]
print(trappingWater(arr,len(arr)))