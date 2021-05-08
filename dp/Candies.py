# we have to minimize the number of Candies given to children
# we have to give more candies to student having better rank to its adjacent

# problem link: https://www.hackerrank.com/challenges/candies/problem

def candies(n, arr):
    # Write your code here
    dp = [1]*n
    
    # left to right
    for i in range(1,n):
        if arr[i]>arr[i-1]:
            dp[i]+=dp[i-1]
    
    # right to left
    for i in range(n-2,-1,-1):
        if arr[i] > arr[i+1] and dp[i] <= dp[i+1]:
            dp[i]=dp[i+1]+1
    return sum(dp)

arr = [2,4,2,6,1,7,8,9,2,1]
print(candies(len(arr),arr))