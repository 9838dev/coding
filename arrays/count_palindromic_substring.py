# Count number of palindromic substring
# Time Complexity: O(n^2)
# space complexity: O(1)

def count_sub(s,low,high):
    count = 0
    while low>=0 and high<len(s):
        if s[low] != s[high]:
            break
        low-=1
        high+=1
        count+=1
    return count

def count_all_substring(s):
    ans = 0
    for i in range(len(s)):
        # for odd length palindromes
        ans+=count_sub(s,i,i)
        
        # for even length palindromes
        ans+=count_sub(s,i,i+1)
        
    return ans

s='abssba'
print(count_all_substring(s))