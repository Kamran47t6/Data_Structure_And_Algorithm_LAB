class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
         self.front=self.rear=None
        
    def enqueue(self,data):
        newnode=Node(data)
        if self.front==None:
            self.front=self.rear=newnode
            
        else:
            self.rear.next=newnode
            self.rear=newnode
    def dequeue(self):
        if self.front==None:
            print("Queue is empty.")
        else:
            data=self.front
            self.front=self.front.next
            return data
        
    def isEmpty(self):
        return self.front==None
    def display(self):
        if self.front==None:
            print("Queue is empty.")
        else:
            temp=self.front
            while temp!=None:
                print(temp.data,end="")
                if temp.next!=None:
                    print("-->",end="")
                temp=temp.next
            print()

que=Queue()
que.enqueue(2)
que.enqueue(5)
que.enqueue(1)
que.enqueue(3)
que.enqueue(9)
que.display()
que.dequeue()
que.display()
que.isEmpty()
