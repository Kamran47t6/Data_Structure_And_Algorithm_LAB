import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp=time.strftime('%H')
print(timestamp)
timestamp=time.strftime('%M')
print(timestamp)
timestamp=time.strftime('%S')
print(timestamp)
# hour=int(input("Enter hour:"))
# min=int(input("Enter min:"))
# sec=int(input("ENter Second :"))
# mood=input("Enter am/pm:")
# if(mood=="am"):
#     if(hour==12):
#         print("Good Night")
#     elif(hour==1):
#         print("Good Night")
#     elif(hour==2):
#         print("Good Night")
#     elif(hour==3):
#         print("Good Night")
#     elif(hour==4):
#         print("Good Morning")
#     elif(hour==5):
#         print("Good Morning")
#     elif(hour==6):
#         print("Good Morning")
#     elif(hour==7):
#         print("Good Morning")
#     elif(hour==8):
#         print("Good Morning")
#     elif(hour==9):
#         print("Good Morning") 
#     elif(hour==10):
#         print("Good Morning")
#     elif(hour==11):
#         print("Good Morning") 
# elif(mood=="pm"):
#      if(hour==12):
#         print("Good Afternoon")
#      elif(hour==1):
#         print("Good Afternoon")
#      elif(hour==2):
#         print("Good Afternoon")
#      elif(hour==3):
#         print("Good Afternoon")
#      elif(hour==4):
#         print("Good Evening")
#      elif(hour==5):
#        print("Good Evening")
#      elif(hour==6):
#         print("Good Evening")
#      elif(hour==7):
#         print("Good Night")
#      elif(hour==8):
#         print("Good Night")
#      elif(hour==9):
#         print("Good Night") 
#      elif(hour==10):
#         print("Good Night")
#      elif(hour==11):
#         print("Good Night") 
# else:
#     print("Invalid time")

arrr=[[2,4,1,3],[1,3,2,5]]
print(arrr)
array = 0 * 10 #array of length 10 having all zeros
#2D array having all zeros
array1 = [[0 for x in range(4)] for y in range(3)]
print(array1)

import random
array3 = []
min = 0
max = 20
n = 5
for i in range (0, n):

  num = random. randint (min, max)
  array3. append (num)
print(array3)

#Traverse in forward direction using for loop
str4 = ['U','E', 'T']
for x in range(len(str4)):
  print(str4[x])
array4 = [32, 1, 9, 31, 12, 22]
# Reverse by using a slice
# slice (start, end, step)
print(array4[-1])

# given_file = open (file = 'test.txt', mode = 'r')
# lines = given_file. read ()
# numbers = []
# arr = lines.split()
# for s in arr:
#   num = int(s)
#   numbers.append(num)
# print(numbers)

arr5=['UET','Lahore']
given_file=open(file="test.txt",mode="w" )
for i in arr5:
  given_file.write(i + "\n")

