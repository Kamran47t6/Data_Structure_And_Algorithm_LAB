import random
import time
def Selection_Sort(array,start,end):
    for i in range(start,end-1):
        min_idx=i
        for j in range(i+1,end):
            if array[j]<array[min_idx]:
                temp=array[j]
                array[j]=array[min_idx]
                array[min_idx]=temp
    return array
def RandomArray(size):
    return [random.randint(0,1000) for _ in  range(size)]
def SaveIntoFile(array):
    filename="SortedBubbleSort.csv"
    with open(filename,"w") as f:
        for elementofArray in array:
            f.write(str(elementofArray)+"\n")
    f.close()

array=RandomArray(1000)
start=0
end=len(array)
start_time=time.time()
Selection_Sort(array,start,end)
end_time=time.time()
run_time=end_time-start_time
SaveIntoFile(array)
print(f"The time taken is {run_time:.3f} seconds")
print(array)