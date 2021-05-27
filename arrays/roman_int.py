# given a roman number to integer

# problem link: https://leetcode.com/problems/roman-to-integer/

def roman_int(s):
    d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    carry = 0
    total_sum = 0

    for i in range(len(s)-1):
        if d[s[i]] < d[s[i+1]]:
            carry = d[s[i]]
        else:
            total_sum += d[s[i]] - carry 

    return total_sum + d[s[-1]] - carry 

s = "MCMXCIV"
print(roman_int(s))