# given a two string, we have to minimize the number of step require to make both string equal

# problem link: https://leetcode.com/problems/delete-operation-for-two-strings/

def minDistance(word1, word2):
    dp = [0]*len(word2)
    for i in range(len(word1)):
        temp = [0]*len(word2)
        for j in range(len(word2)):
            if j == 0:
                if word1[i] == word2[j]:
                    temp[j]+=1
                elif i!=0:
                    temp[j] = dp[j]
                    
            else:
                if word1[i] != word2[j]:
                    temp[j] = max(temp[j-1],dp[j])
                else:
                    temp[j] = dp[j-1]+1 
        dp = temp 
    return len(word1) + len(word2) - 2*(dp[-1])

word1 = 'aabc'
word2 = 'abcdb'

print(minDistance(word1,word2))