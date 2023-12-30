def Average(a,b):
    return (a+b)/2

c=Average(2,4)
print(c)


def newAverage(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)

c=newAverage(2,4,6)
print(c)