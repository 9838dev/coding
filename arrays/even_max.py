# find largest combination of string and that number should be even

def largest_even(s):
    arr=list(map(int,s))
    min_ev_el,min_ev_ind=float('inf'),-1
    min_odd_el,min_odd_ind=float('inf'),-1

    for i in range(len(arr)):
        if arr[i]%2 == 0:
            if min_ev_el>arr[i]:
                min_ev_el=arr[i] 
                min_ev_ind=i
        if arr[i]%2 == 1:
            if min_odd_el>arr[i]:
                min_odd_el = arr[i]
                min_odd_ind = i

    if min_ev_el!=float('inf'):
        arr[min_ev_ind]=-1*float('inf')
        arr.sort(reverse=True)
        arr[-1] = min_ev_el 
        s=''
        for i in arr:
            s+=str(i) 
        return s
    else:
        arr[min_odd_ind]=-1*float('inf')
        arr.sort(reverse=True)
        arr[-1] = min_odd_el 
        s=''
        for i in arr:
            s+=str(i) 
        return s 

s='4656469948812'
print(largest_even(s))
