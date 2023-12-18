import random
import time

def MergeSort(array,start,end):
   if start<end:
      mid=(start+end)//2
      MergeSort(array,start,mid)
      MergeSort(array,mid+1,end)
      Merge(array,start,mid,end)
      return array
def Merge(array,p,q,r):
    left_half=array[p:q+1]
    right_half=array[q+1:r+1]
    i=j=0
    k=p
    while(i<len(left_half) and j<len(right_half)):
        if left_half[i]<right_half[j]:
            array[k]=left_half[i]
            i+=1
        else:
            array[k]=right_half[j]
            j+=1
        k+=1
    while (i<len(left_half)):
        array[k]=left_half[i]
        i+=1
        k+=1
    while(j<len(right_half)):
        array[k]=right_half[j]
        j+=1
        k+=1
        
def SaveIntoFile(array):
    filename="SortedMergeSort.csv"
    with open(filename,'w') as f:
        for elementArray in array:
            f.write(str(elementArray)+ "\n")
    f.close()

def RandomArray(size):
    return [random.randint(1,1000) for _ in range(size)]

array=RandomArray(1000)
start_time=time.time()
MergeSort(array,0,len(array)-1)
end_time=time.time()
run_time=end_time-start_time
SaveIntoFile(array)
print(array)
print(f"The time taken {run_time:.4f} seconds")
