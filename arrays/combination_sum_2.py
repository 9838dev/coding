# given an array and a target
# find all unique combination in an array where array number sum to target

# solution must not contain duplicate combination
'''
Given input
array = [10,1,2,7,6,1,5]
target = 8

Output:
[
   [1,1,6],
   [1,2,5],
   [1,7],
   [2,6
]
'''



arr = [10,1,2,7,6,1,5]
target =  8
ans=[]
find_combination(0,arr,target,ans,[])
