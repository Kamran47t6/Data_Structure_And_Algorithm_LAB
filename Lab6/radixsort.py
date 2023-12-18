def RadixSort(arr):
     max1=max(arr)
     exp=1
     while max1/exp>=1:
         CountSort(arr,exp)
         exp *=10


        

def CountSort(arr,exp):
     n=len(arr)
     output_arr=[0]*n
     count_arr=[0]*10
     for i in range(0,n):
          index=arr[i]//exp
          count_arr[index%10]+=1
     for i in range(1,10):
          count_arr[i]+=count_arr[i-1]
     i=n-1
     while i>=0:
          index=arr[i]//exp
          output_arr[count_arr[index%10]-1]=arr[i]
          count_arr[index%10]-=1
          i=i-1
    
     for i in range(0,len(arr)):
          arr[i]=output_arr[i]
arr=[5,2,98,76,1,50]
RadixSort(arr)
print(arr)



