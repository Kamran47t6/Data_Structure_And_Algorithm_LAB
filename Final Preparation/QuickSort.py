def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            (array[i],array[j])=(array[j],array[i])
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1

def QuickSort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        QuickSort(array,low,pi-1)
        QuickSort(array,pi+1,high)

data=[8,2,1,6,5,9]
QuickSort(data,0,len(data)-1)
print(data)





