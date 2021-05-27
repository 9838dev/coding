# given an integer count no. of 1's in bit representation of that number upto 0 to n

# problem link: https://leetcode.com/problems/counting-bits/

def countBits(num):
    count = [0]
    for i in range(1,num+1):
        count.append(count[i//2] + i%2)
    return count

n = 5
print(countBits(n))

n = 8
print(countBits(n))