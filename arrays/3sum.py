# find all triplets with zero sum
# 3 sum
# problem link: https://leetcode.com/problems/3sum/

def triplets(arr,n):
    arr.sort()
    li=[]
    for i in range(n):
        l=i+1
        h=n-1
        a=arr[i]
        while l<=h:
            b=a+arr[l]+arr[h]
            if b == 0:
                li.append([a,arr[l],arr[h]])
                l+=1
                h-=1
            elif b>0:
                h-=1
            else:
                l+=1
    print(li)

arr=[1,-2,1,0,5,3,-1]
triplets(arr,len(arr))