#include <iostream>
#include <cstdlib>
using namespace std;
class Node {
public:
    int data;
    Node* parent;
    Node* left;
    Node* right;

    Node(int value) : data(value), parent(nullptr), left(nullptr), right(nullptr) {}
};

class BST {
public:
    BST() : root(nullptr) {}
    BST(int arr[], int size) : root(nullptr) {
        for (int i = 0; i < size; i++) {
            insertNode(arr[i]);
        }
    }
    ~BST() {
        clearTree(root);
    }

    bool isEmpty() { return root == nullptr; }
    Node* getTree() { return root; }

    Node* insertNode(int x) {
        root = insertNodeRec(root, x);
        return root;
    }

    Node* findNode(int x) {
        return findNodeRec(root, x);
    }

    bool deleteNode(int x) {
        return deleteNodeRec(root, x);
    }

    void inOrderTraversal(Node* T) {
        if (T != nullptr) {
            inOrderTraversal(T->left);
            cout << T->data << " ";
            inOrderTraversal(T->right);
        }
    }

    void preOrderTraversal(Node* T) {
        if (T) {
            cout << T->data << " ";
            preOrderTraversal(T->left);
            preOrderTraversal(T->right);
        }
    }

    void postOrderTraversal(Node* T) {
        if (T) {
            postOrderTraversal(T->left);
            postOrderTraversal(T->right);
            cout << T->data << " ";
        }
    }

    int NumberOfNodes(Node* T) {
        if (T == nullptr) {
            return 0;
        }
        return 1 + NumberOfNodes(T->left) + NumberOfNodes(T->right);
    }

    int Height(Node* T) {
        if (T == nullptr) {
            return -1;
        }
        int leftHeight = Height(T->left);
        int rightHeight = Height(T->right);
        return max(leftHeight, rightHeight) + 1;
    }

    bool isBST(Node* T) {
        return isBSTUtil(T, INT_MIN, INT_MAX);
    }

    void LeafNodes(Node* T) {
        if (T) {
            if (T->left == nullptr && T->right == nullptr) {
                cout << T->data << " ";
            }
            LeafNodes(T->left);
            LeafNodes(T->right);
        }
    }

    bool isSparseTree(Node* T) {
        int totalNodes = NumberOfNodes(T);
        int leafNodes = countLeafNodes(T);
        return (static_cast<double>(leafNodes) / totalNodes) < 0.5;
    }

    void visualizeTree(Node* T) {
        visualizeTreeUtil(T, 0);
    }

private:
    Node* root;

    Node* insertNodeRec(Node* T, int x) {
        if (T == nullptr) {
            return new Node(x);
        }

        if (x < T->data) {
            T->left = insertNodeRec(T->left, x);
            T->left->parent = T;
        }
        else if (x > T->data) {
            T->right = insertNodeRec(T->right, x);
            T->right->parent = T;
        }

        return T;
    }

    Node* findNodeRec(Node* T, int x) {
        if (T == nullptr || T->data == x) {
            return T;
        }

        if (x < T->data) {
            return findNodeRec(T->left, x);
        }

        return findNodeRec(T->right, x);
    }

    bool deleteNodeRec(Node* T, int x) {
        if (T == nullptr) {
            return false;
        }

        if (x < T->data) {
            return deleteNodeRec(T->left, x);
        }
        else if (x > T->data) {
            return deleteNodeRec(T->right, x);
        }
        else {
            if (T->left == nullptr) {
                Node* temp = T->right;
                delete T;
                T = temp;
            }
            else if (T->right == nullptr) {
                Node* temp = T->left;
                delete T;
                T = temp;
            }
            else {
                Node* minRight = findMin(T->right);
                T->data = minRight->data;
                deleteNodeRec(T->right, minRight->data);
            }
            return true;
        }
    }

    Node* findMin(Node* T) {
        while (T->left != nullptr) {
            T = T->left;
        }
        return T;
    }

    void clearTree(Node* T) {
        if (T) {
            clearTree(T->left);
            clearTree(T->right);
            delete T;
        }
    }

    bool isBSTUtil(Node* T, int min, int max) {
        if (T == nullptr) {
            return true;
        }

        if (T->data < min || T->data > max) {
            return false;
        }

        return isBSTUtil(T->left, min, T->data - 1) && isBSTUtil(T->right, T->data + 1, max);
    }

    int countLeafNodes(Node* T) {
        if (T == nullptr) {
            return 0;
        }
        if (T->left == nullptr && T->right == nullptr) {
            return 1;
        }
        return countLeafNodes(T->left) + countLeafNodes(T->right);
    }

    void visualizeTreeUtil(Node* T, int level) {
        if (T == nullptr) {
            return;
        }
        visualizeTreeUtil(T->right, level + 1);
        for (int i = 0; i < level; i++) {
            cout << "  ";
        }
        cout << T->data << "\n";
        visualizeTreeUtil(T->left, level + 1);
    }
};

int main() {
    BST tree;
    int arr[] = { 50, 30, 70, 20, 40, 60, 80 };
    int size = sizeof(arr) / sizeof(arr[0]);
    tree = BST(arr, size);

    cout << "In-order traversal: ";
    tree.inOrderTraversal(tree.getTree());
    cout << endl;

    cout << "Pre-order traversal: ";
    tree.preOrderTraversal(tree.getTree());
    cout << endl;

    cout << "Post-order traversal: ";
    tree.postOrderTraversal(tree.getTree());
    cout << endl;

    cout << "Number of nodes in the tree: " << tree.NumberOfNodes(tree.getTree()) << endl;
    cout << "Height of the tree: " << tree.Height(tree.getTree()) << endl;

    if (tree.isBST(tree.getTree())) {
        cout << "The tree is a Binary Search Tree." << endl;
    }
    else {
        cout << "The tree is not a Binary Search Tree." << endl;
    }

    cout << "Leaf nodes of the tree: ";
    tree.LeafNodes(tree.getTree());
    cout << endl;

    if (tree.isSparseTree(tree.getTree())) {
        cout << "The tree is sparse (filled less than 50%)." << endl;
    }
    else {
        cout << "The tree is not sparse (filled at least 50%)." << endl;
    }

    cout << "Visualizing the tree:\n";
    tree.visualizeTree(tree.getTree());

    return 0;
}
