# longest valid parenthesis

def longest_valid(s):
    st=[-1]
    res=0
    for i in range(len(s)):
        if s[i] == '(':
            st.append(i)
        else:
            if len(st)>0:
                st.pop()
            if len(st)>0:
                res = max(res,i-st[-1])
            else:
                st.append(i)
    print(res)
    
s = input("Enter any string")
longest_valid(s)
