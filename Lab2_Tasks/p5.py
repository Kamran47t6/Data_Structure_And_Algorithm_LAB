import time
import random
def BubbleSort(array,start,end):
    for i in range(start,end):
        for j in range(start,end-i-1):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp

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
BubbleSort(array,start,end)
end_time=time.time()
run_time=end_time-start_time
SaveIntoFile(array)
print(f"The time taken is {run_time:.3f} seconds")
print(array)
