# List=[2,4,6,8]
# # print(List)
# # print(List[0])
# # print(List[1])
# # print(List[2])
# # print(List[3])
# print(List[-3])   # negative index
# print(List[len(List)-3])  # positive index
# print(List[4-3])  #  positive index
# if 8 in List:        # to cheeck either the num is avaiable in list
#     print("yes..")
# else:
#     print("No...")
    
# marks=[3,8,2,"kamran",True,9,7,1]
# print(marks[0:]) # it automatically set end length 7
# print(marks[:]) # it automatically set start length 0
# print(marks)
# print(marks[1:5])
# print(marks[1:5:2])      # string slicing



# # list comprehension
# lst=[i for i in range(6)]
# print(lst)

# lst=[i*i for i in range(10) if(i%2==0)]
# print(lst)

info=['Python','Programming','is','easy']
print(info[0]+info[3])
info.append("Waoo!")  # append mode to add string in list
print(info)
info.insert(0,"Hey students")
print(info)
info.remove("Waoo!")
print(info)
print(info.pop(2))     # to remove at specific index
print(info)

#modify of list
info[1]="Javascript"
print(info)

info.insert(32,"Lets do it")
print(info)

multiples=[]
for i in range(1,11):
    multiples.append(i*7)
print(multiples)

multiples=[i*7 for i in range(1,11)]  # list comprehension
print(multiples)

# list comprehension
table=[x for x in range(1,30+1) if x%3==0]
print(table)

sortdata=[4,2,9,5,0,1,3,-3]
sortdata.sort()
print(sortdata)
sortdata=[4,2,9,5,0,1,3,-3]
sortdata.clear()
print(sortdata)
sortdata=[4,2,9,5,0,1,3,-3]
sortdata.reverse()
print(sortdata)
sortdata=[4,2,9,5,0,1,3,-3]
sortdata.copy()
print(sortdata)
sortdata.extend(table)  # connect the other list at the after the last index of current list
print(sortdata)



filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames=[filename.replace('hpp','h') if filename.endswith('hpp') else filename for filename in filenames ]

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]




