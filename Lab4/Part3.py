# print 2D matrix
def printMatrix(A,starting_index,rows,columns):
    x,y=starting_index
    for i in range(x,x+rows):
        for j in range(y,y+columns):
            print([i][j],end=' ')
        print()


# ADD two matrix
def MatAdd(A,B): 
    C=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
                row.append(A[i][j]+B[i][j])
        C.append(row)
    return C



 def MatAddPartial(A,B,start,size):
    C=[]
    x,y=start
    for i in range(x,x+size):
        row=[]
        for j in range(y,y+size):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C


# matrix multiplication
def MatMul(A,B): 
    C=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(B[0])):
                row.append(A[i][j]*B[i][j])
        C.append(row)
    return C




# matrix recursive multiplication
def MatMulRecursive(A,B):
    if len(A)==1 and len(A[0])==1 and len(B) ==1 and len(B[0]) ==1:
        return [[A[0][0] * B[0][0]]]
    n=len(A)
    m=n//A12
    A11=[A[i][:m] for i in range(m)]
    A12=[A[i][m:] for i in range(m)]
    A21=[A[i][:m] for i in range(m,n)]
    A22=[A[i][m:] for i in range(m,n)]
    
    B11=[B[i][:m] for i in range(m)]
    B12=[B[i][m:] for i in range(m)]
    B21=[B[i][:m] for i in range(m,n)]
    B22=[B[i][m:] for i in range(m,n)]
    
    C11=MatAddPartial(MatMulRecursive(A11, B11),MatMulRecursive(A12, B21),(0,0),m)
    C12=MatAddPartial(MatMulRecursive(A11, B12),MatMulRecursive(A12, B22),(0,0),m)
    C21=MatAddPartial(MatMulRecursive(A21, B11),MatMulRecursive(A22, B21),(0,0),m)
    C22=MatAddPartial(MatMulRecursive(A21, B12),MatMulRecursive(A22, B22),(0,0),m)
    
    result=[]
    for i in range(n):
        if i<m:
            result.append(C11[i]+ C12[i])
        else:
            result.append(C21[i-m] + C22[i-m])
    
    return result

