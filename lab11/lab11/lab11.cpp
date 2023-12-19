#include <iostream>
#include <fstream>
#include <sstream>
#include <list>

using namespace std;

class KeyNode {
public:
    string Key;
    int Value;

    KeyNode(string key, int value) : Key(key), Value(value) {}
};

class MyHashTable {
private:
    list<KeyNode>* table;
    int size;
    int keysOccupied;

public:
    MyHashTable(int hsize) : size(hsize), keysOccupied(0) {
        table = new list<KeyNode>[size];
    }

    ~MyHashTable() {
        delete[] table;
    }

    int GetHashTableSize() {
        return size;
    }

    int GetNumberOfKeys() {
        return keysOccupied;
    }

    int HashFunction(const string& key) {
        int sum = 0;
        for (char ch : key) {
            sum += static_cast<int>(ch);
        }
        return sum % size;
    }

    void UpdateKey(const string& key, int value) {
        int index = HashFunction(key);

        for (auto& node : table[index]) {
            if (node.Key == key) {
                node.Value += value;
                return;
            }
        }

        // Key not found, add a new KeyNode
        table[index].emplace_back(key, value);
        keysOccupied++;

        // Check for rehashing
        if (keysOccupied > size * 0.7) {
            Rehash();
        }
    }

    int SearchKey(const string& key) {
        int index = HashFunction(key);

        for (const auto& node : table[index]) {
            if (node.Key == key) {
                return node.Value;
            }
        }

        return 0; // Key not found
    }

    void Rehash() {
        int newSize = size * 2;
        list<KeyNode>* newTable = new list<KeyNode>[newSize];

        for (int i = 0; i < size; ++i) {
            for (const auto& node : table[i]) {
                int newIndex = HashFunction(node.Key);
                newTable[newIndex].push_back(node);
            }
        }

        delete[] table;
        table = newTable;
        size = newSize;
    }
};

int main() {
    MyHashTable hashTable(128);
    ifstream inputFile("input.txt");
    string line;
    while (getline(inputFile, line)) {
        hashTable.UpdateKey(line, 1);
    }

    cout << "Word Occurrences:" << endl;

    // Iterate over the hash table
    for (int i = 0; i < hashTable.GetHashTableSize(); ++i) {
        for (const auto& node : hashTable[i]) {
            cout << node.Key << " " << node.Value << endl;
        }
    }

    return 0;
}


