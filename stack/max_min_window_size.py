# maximum of minimum for every window size in a given array

arr = [10,20,30,50,10,70,30]
n=len(arr)
left=[-1]*(n)
right=[n]*(n)

# previous minimum of a element
st=[]
for i in range(len(arr)):
    while len(st)!=0 and arr[st[-1]]>=arr[i]:
        st.pop()
        
    if len(st)!=0:
        left[i] = st[-1]
    st.append(i)
    
#next minimum of a element
st=[]
for i in range(n-1,-1,-1):
    while len(st)!=0 and arr[st[-1]]>=arr[i]:
        st.pop()
    if len(st)!=0:
        right[i] = st[-1]
    st.append(i)
    
# arr[i] is a minimum of a window of length
# i.e ans[i] = right[i]-left[i]-1
# first value indicate minimum of window of size arr[i]
# second value indicate minimum of window of size arr[i+1]
# and so on

ans=[0]*(n+1)
for i in range(n):
    
    # if two value points same index position, then we store the maximum value index
    le = right[i]-left[i]-1
    ans[le] = max(ans[le],arr[i])
    
# filling remaining values
for i in range(n-1,0,-1):
    ans[i] = max(ans[i],ans[i+1])
    
print(ans[1:])
