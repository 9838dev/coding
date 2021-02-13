# it is a point where sum of left side and sum of right side of an array are equal 

def equilibrium_Point(arr):
    n=len(arr)
    i,j=1,n-2
    suml,sumr=arr[0],arr[n-1]
    while i<n and j>=0:
        if suml == sumr:
            if i == j:
                return [i+1]
            else:
                suml+=arr[i]
                i+=1
        if i>=j:
            return (i,j)
        while i<len(arr) and sumr>suml:
            suml+=arr[i]
            i+=1
        while j>=0 and sumr<suml:
            sumr+=arr[j]
            j-=1 

if __name__ == '__main__':
    arr=[10,20,6,30,40,10,50,6]
    a = equilibrium_Point(arr)
    if len(a)>1:
        print(-1)
    else:
        print(arr[a[0]-1])