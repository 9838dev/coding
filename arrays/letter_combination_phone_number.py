# Given string contains [2,9] return all letter combinations that number could represent
'''
Sample Input:
digits = '23'

Sample Output:
["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''

def find_combinations(digits):
    d={
        '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
        '7':'pqrs','8':'tuv','9':'wxyz'
    }
    if len(digits) == 0:
        return []
    ans = []

    def dfs(pos,st):
        if pos == len(digits):
            ans.append(st)
        else:
            letters = d[digits[pos]]
            for letter in letters:
                dfs(pos+1,st+letter)
    dfs(0,'')
    return ans 

digits = '452'

print(find_combinations(digits))