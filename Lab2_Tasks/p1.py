def RandomArray(size):
    arr=[]
    for i in range(0,size):
        j=int(input())
        arr.append(j)
    return arr
print("Enter the size of array:")
size=int(input())
result=RandomArray(size)
print(result)
