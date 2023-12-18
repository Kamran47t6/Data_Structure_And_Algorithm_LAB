num=int(input("ENter the number of table :"))
i=1
while(i<=10):
    print(num,"*",i,"=",num*i)
    i=i+1
count=5
while(count>0):
    print(count)
    count=count-1
# do while emulate
name="Kamran"
na1=input("Enter name:")
count=1
while(count>0):
    print("Count",count)
    na1=input("Enter name:")
    if(name==na1):
     print("Correct")
     count=count+1
    else:
        break
    