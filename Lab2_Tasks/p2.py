import time
import random
def InsertionSort(array,start,end): 
    for i in range(start,end):
        key=array[i]
        j=i-1
        while j>=0 and array[j]>key :  
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
    return array
def RandomArray(size):
    return [random.randint(1,1000) for _ in range(size)]
def SaveIntoFile(array):
    filename="SortedInsertionSort.csv"

    with open(filename,'w') as f:
        for elementofarray in array:
            f.write(str(elementofarray)+"\n")
    f.close()

array=RandomArray(100)
start=1
end=len(array)
start_time=time.time()
InsertionSort(array,start,end)
end_time=time.time()
run_time=end_time-start_time
SaveIntoFile(array)
print(array)
print("The time taken ",run_time," seconds")
