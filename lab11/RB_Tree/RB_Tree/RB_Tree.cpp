#include <iostream>
//insertion
using namespace std;
struct Node {
    int data;
    Node* parent;
    Node* left;
    Node* right;
    int color;
};
typedef Node* NodePtr;
class RedBlackTree {
private:
    NodePtr root;
    NodePtr TNull;
    void initializeNull(NodePtr node, NodePtr parent) {
        node->data = 0;
        node->parent = parent;
        node->left = nullptr;
        node->right = nullptr;
        node->color = 0;
    }
    //preorder
    void PreOrderHelper(NodePtr node) {
        if (node != TNull) {
            cout << node->data << "  ";
            PreOrderHelper(node->left);
            PreOrderHelper(node->right);
        }
    }
    //postorder
    void PostOrderHelper(NodePtr node) {
        if (node != TNull) {
           
            PostOrderHelper(node->left);
            PostOrderHelper(node->right);
            cout << node->data << "  ";
        }
    }
    //inorder
    void InOrderHelper(NodePtr node) {
        if (node != TNull) {

            InOrderHelper(node->left);
            cout << node->data << "  ";
            InOrderHelper(node->right);
            
        }
    }
    NodePtr searchTreeHelper(NodePtr node, int key) {
        if (node == TNull || key == node->data) {
            return node;
        }
        if (key < node->data) {
           return searchTreeHelper(node->left, key);
        }
        return searchTreeHelper(node->right, key);
    }
    void insert(int key) {
        NodePtr node = new Node;
        node->parent = nullptr;
        node->data = key;
        node->left = TNull;
        node->right = TNull;
        node->color = 1;


    }
    
};
int main()
{
    cout << "Hello World!\n";
}
