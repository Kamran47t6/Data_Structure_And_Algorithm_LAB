
#include <iostream>
#include<conio.h>
#include<stack>
using namespace std;
class Node{
public:
	int data;
	Node* link;
	Node(int n) {
		this->data = n;
		this->link = NULL;

	}
};
class Stack {
	Node* top;
public:
	Stack() {
		top = NULL;
	}
	// to add data into stack
	void push(int data) {
		Node* temp = new Node(data);
		if (!temp) {
			cout << "Stack Overflow.";
		}
		temp->data = data;
		temp->link = top;
		top = temp;
	}
	// check whether the stack is empty or not
	bool isEmpty() {
		return top == NULL;
	}
	// return the top element of the stack
	int peek() {
		if (!isEmpty()) {
			return top->data;
		}
	}
	void pop() {
		Node* temp;
		if (top == NULL) {
			cout << "Stack Underflow.";
		}
		else {
			temp = top;
			top = top->link;
			delete temp;
		}
	}
	// to display all elements of stack 
	void display() {
		Node* temp;
		if (top == NULL) {
			cout << "Stack Underflow here.";
			exit(1);
		}
		else {
			temp = top;
			while (temp != NULL) {
				cout << temp->data;
				temp = temp->link;
				if (temp != NULL) {
					cout << "   ";   
				}
			}
		}
	}
};
int main()
{
	Stack s1;
	stack<int> mystack;
	s1.push(1);
	s1.push(2);
	s1.push(3);
	s1.push(4);
	s1.push(5);
	s1.display();
	s1.pop();
	s1.display();

	return 0;
}
