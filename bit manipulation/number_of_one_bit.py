# given a integer count number of '1' bit it has

# problem link: https://leetcode.com/problems/number-of-1-bits/

def count_one(n):
    count = 0
    while n!=0:
        count+=1
        n = n & (n-1)
    return count

print(count_one(12))
print(count_one(8))