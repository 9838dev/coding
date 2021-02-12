def issafe(board,i,j,n):
    # returning False if we won't able to place the queen at particular column
    # otherwise True
    # checking for the row of same column
    for row in range(i,-1,-1):
        if board[row][j] == 1:
            return False
    
    #checking for the left diagonal
    x,y=i,j 
    while x>=0 and y>=0:
        if board[x][y] == 1:
            return False 
        x,y=x-1,y-1

    # checking for right diagonal
    while i>=0 and j<n:
        if board[i][j] == 1:
            return False 
        i-=1
        j+=1
    return True

def nqueen(board,i,n):

    # base case... if in last row queen placed successfully
    if i == n:
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    print('Q',end=' ')
                else:
                    print('.',end=' ')
            print()
        print()
        return False 

    # checking for every column in the given row
    for j in range(n):

        # can we place the queen on that place, if yes we place the queen there
        if issafe(board,i,j,n): 
            board[i][j]=1

            # recursively calling for each row
            a = nqueen(board,i+1,n)

            # return true if we place the queen successfully.. otherwise we can't place the queen 
            if a:
                return True 
            board[i][j]=0
    return False

if __name__ == '__main__':
    n=5

    # creating board of size n*n
    # 1 for placing the queen and 0 for not placing
    board=[[0 for j in range(n)] for i in range(n)] 
    nqueen(board,0,n)
