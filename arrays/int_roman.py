# integer to roman

d={
    1:'I',
    4:'IV',
    5:'V',
    9:'IX',
    10:'X',
    40:'XL',
    50:'L',
    90:'XC',
    100:'C',
    400:'CD',
    500:'D',
    900:'CM',
    1000:'M'
}

def roman(s,j):
    n = int(s)*pow(10,j)
    if n in d:
        return d[n]
    else:
        s1=''
        if n>(5*pow(10,j)):
            s1+=d[5*pow(10,j)]
            while n>(5*pow(10,j)):
                s1+=d[pow(10,j)]
                n = n-pow(10,j)
        else:
            while n>0:
                s1+=d[pow(10,j)]
                n = n-pow(10,j)
    print()
    return s1
               
def int_to_roman(num):
    a = str(num)
    final = ''
    j=len(a)-1
    for i in range(len(a)):
        final+=roman(a[i],j)
        j-=1
    return final
    
n=7
print(int_to_roman(n))
