#include<iostream>
#include<conio.h>
using namespace std;
class Node {
public:
	int data;
	Node* next=NULL;
};
class LinkList {
public:
	LinkList() {
		head = nullptr;
	}
	~LinkList() {
		while (head != nullptr) {
			Node* temp = head;
			head = head->next;
			delete temp;		
		}
	}
	Node* insertNode(int index, int x) {
		if (index < 0) {
		
			return nullptr;
		}
		Node* current = head;
		Node* new_node = new Node();
		
		new_node->data = x;
		int curent_index = 0;
		while (current != nullptr && curent_index < index - 1) {
			current = current->next;
			curent_index++;
		}
		if (current == nullptr) {
			return nullptr;
		}
		new_node->next = current->next;
		current->next = new_node;
		return new_node;
	
    }

	Node* insertAtHead(int x) {
		Node* new_node = new Node();
		new_node->data = x;
		new_node->next = head;
		head = new_node;
	}
	Node* insertAtEnd(int x) {
		Node* new_node = new Node();
		new_node->data = x;
		new_node->next = NULL;
		Node* temp = head;
		while (temp->next!= NULL) {
			temp = temp->next;
		}
		temp->next = new_node;
	}
	bool findNode(int x) {
		Node* temp = head;
		int node_count = 0;
		while (temp->data != x) {
			node_count++;
		}
		cout << "Node found at index:" << node_count;
		return true;
	}
	bool deleteNode(int x) {
		Node* current = head;
		bool deletd = false;
		int n=sizeof(head);
		int count = 0;
		while (count<n && current!=NULL) {
			if (current->next->data == x) {
				delete current->next;
				deletd = true;
			}
			else 
			{
				current = current->next;
			}
			count++;
		}
		
		return deletd;
	}


	
	bool deleteFromStart() {
		if (head == nullptr) {
			return false;
		}
		Node* todelete = head;
		head = head->next;
		delete todelete;
		
		return true;
	}
	bool deleteFromEnd(int x) {
		Node* temp = head;
		while (temp->next != NULL) {
			temp = temp->next;
		}
		delete temp;
	}
	void displayList(Node* node) {
		while (node != NULL) {
			cout << "  " << node->data;
			node = node->next;

		}
	}
	Node* reverseList(Node* head) {
		if (head == NULL || head->next == NULL) {
			return head;
		}
		Node* newhead = reverseList(head->next);
		head->next->next = head;
		head->next = NULL;
		return newhead;
	}
	
	Node* sortList(Node* list) {
		if (list == nullptr) {
			return nullptr;
		}
		Node* current;
		Node* temp = nullptr;
		bool swapped;
		do {
			swapped = false;
			current = list;
			while (current->next != temp) {
				if (current->data > current->next->data) {
					int tempdata = current->data;
					current->data = current->next->data;
					current->next->data = tempdata;
					swapped = true;
				}
				current = current->next;
			}
			temp = current;
		} while (swapped);
		return list;
		
	}
	Node* removeDuplicates(Node* list) {
		Node* current = list;
		Node* nextPointer;
		if (current ==NULL) {
			return nullptr;
		}
		while (current->next != NULL) {
			if (current->data == current->next->data) {
				nextPointer = current->next->next;
				delete current->next;
				current->next = nextPointer;

			}
			else {
				current = current->next;
			}
		}
		return list;

	}
	
	
private:
	Node* head;
};

void push(Node** head, int new_data) {
	Node* new_node = new Node();
	new_node->data = new_data;
	new_node->next = (*head);
	(*head) = new_node;
}

int main() {
	Node* head = nullptr;
	LinkList mylist;
	
	push(&head, 13);
	push(&head, 24);
	push(&head, 9);
	push(&head, 7);
	push(&head, 2);
	push(&head, 24);
	push(&head, 4);
	push(&head, -2);
	push(&head, 2);
	push(&head, 11);
	cout << "Before :";
	mylist.displayList(head);
	head = mylist.sortList(head);
	head=mylist.removeDuplicates(head);
	cout << "After :";
	mylist.displayList(head);

	
	return 0;
}