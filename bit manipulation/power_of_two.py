# given a number find wheather a number is power of two or not

# problem link: https://leetcode.com/problems/power-of-two/

def isPowerOfTwo(n):
    if n == 0: return False
    if (n) & (n-1) == 0:
        return True
    else:
        return False

print(isPowerOfTwo(5))
print(isPowerOfTwo(8))