def multiply_matrix(a,b):
    n1,m1=len(a),len(a[0])
    n2,m2=len(b),len(b[0])
    if m1!=n2:
        return []
    matrix=[[0 for i in range(m2)] for j in range(n1)]

    for i in range(n1):
        for j in range(m2):
            val=0
            for k in range(m1):
                val+=(a[i][k]*b[k][j])
            matrix[i][j]=val 
    print(matrix)

a=[
    [1,2,3],
    [3,4,5],
    [6,7,8]
]
b=[
    [1],
    [7],
    [8]
]
multiply_matrix(a,b)