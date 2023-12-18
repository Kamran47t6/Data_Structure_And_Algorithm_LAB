import random
def HybridMergeSort(array,start,end):
    if len(array)<=5:
        Insertion_Sort(array)
    else:
         if len(array)<=1:
           return array
         mid=len(array)//2             # divide the array into two halves
         left_half=array[:mid]         # first half
         right_half=array[mid:]        # second half
         HybridMergeSort(left_half,start,end)       # recursive function call for spliting the array further if required more
         HybridMergeSort(right_half,start,end)
         i=j=k=0                     # i to work as left half index              j to work as right half index         k to work as index for final array
         while i<len(left_half) and j<len(right_half):      
           if left_half[i]<right_half[j]:
              array[k]=left_half[i]
              i+=1
           else:
              array[k]=right_half[j]
              j+=1
           k+=1
         while i< len(left_half):    # check if any element is left to be stored in final array
           array[k]=left_half[i]
           i+=1
           k+=1
         while j< len(right_half):   
           array[k]=right_half[j]
           j+=1
           k+=1
    return array

def Insertion_Sort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>=0 and array[j]>key:
            array[j+1]=array[i]
            j=j-1
        array[j+1]=key

def RandomArray(size):
   return [random.randint(0,1000) for _ in range(size)]

def SaveIntoFile(array):
   filename= "SortedHybridSort.csv"
   with open(filename,"w") as f:
      for elementOfArray in array:
         
        f.write(str(elementOfArray)+ "\n")
   f.close()

array=RandomArray(1000)
HybridMergeSort(array,0,len(array)-1)
SaveIntoFile(array)
print(array)
        