# given n pair of parentheses, generate all combination of well-formed parentheses

# problem link: https://leetcode.com/problems/generate-parentheses/

ans = []
def generate(s=[],left=0,right=0,n=0):
    if 2*n == len(s):
        ans.append(''.join(s))
        return
    if left<n:
        s.append('(')
        generate(s,left+1,right,n)
        s.pop()
    if right<left:
        s.append(')')
        generate(s,left,right+1,n)
        s.pop()

n = 4
generate(n=n)
print(ans)
