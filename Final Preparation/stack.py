class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Stack:
    def __init__(self):
        self.head=None

    def push(self,data):
        if self.head==None:
            self.head=Node(data)
           
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode

    def pop(self):
        if self.isEmpty():
            print("Stack is Underflow")
        else:
            popednode=self.head
            self.head=self.head.next
            popednode.next=None
            return popednode.data
        
    def peek(self):
        if self.isEmpty():
            print("Stack is Underflow.")
        else:
            return self.head.data
    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False
    
    def display(self):
        if self.isEmpty():
            print("Stack is Underflow.")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end="")
               
                if temp.next!=None:  # same as           if temp is not None:
                    print("-->",end="")
                temp=temp.next
            print()
    
stack=Stack()
stack.push(2)

stack.push(3)

stack.push(4)

stack.push(5)

stack.push(1)
stack.display()


print("Peek Element:",stack.peek())

print("Pop Element:",stack.pop())
stack.display()

