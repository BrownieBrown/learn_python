# Learning Python: Algorithms and Data Structures

Welcome to my personal repository where I'm diving deep into algorithms and data structures using Python. Primarily
tailored for my coding interview preparations, I hope it can be a valuable resource for others embarking on a similar
journey.

## 📜 Contents

### 🧠 Algorithms

#### 🔄 Sorting

- **Bubble Sort**: A simple comparison-based sort that repeatedly steps through the list, compares adjacent elements,
  and swaps them if they're in the wrong order.
- **Merge Sort**: A divide-and-conquer method that divides the unsorted list into `n` sublists, each with one element,
  and then repeatedly merges these sublists to produce new sorted ones until there's just one remaining.
- **Quick Sort**: This divide-and-conquer algorithm selects a 'pivot' element from the list and then partitions the
  other elements into two sublists, based on whether they're less than or greater than the pivot.
- **Insertion Sort**: Builds the final sorted array one item at a time. It's much less efficient on large lists than
  more advanced algorithms like quicksort, heapsort, or merge sort.
- **Selection Sort**: This sorting algorithm is an in-place comparison sort. It has O(n^2) time complexity, making it
  inefficient on large lists, and generally performs worse than the similar insertion sort.

#### 🔍 Searching

##### Binary Search

- **Main Implementation**: Efficiently finds an item from a sorted list. By halving the possible locations each time,
  you narrow down the potential spots to just one.

- **Challenges**:
    - Finding Boundary in a Boolean List
    - First Not Smaller
    - Find First Occurrence
    - Finding the Peak of a Mountain Array
    - _...and more challenges related to binary search!_

#### 🔮 Depth-First Search (DFS)

- **Main Implementation**: A traversal algorithm that explores as far as possible along each branch before backtracking.
  Primarily used for tree and graph traversal.

- **Challenges**:
    - Checking if a tree is balanced
    - Counting visible nodes in a tree
    - _...and more challenges related to DFS!_

### 🛠️ Data Structures

#### 🌲 Trees

- **Binary Tree**: A tree in which each node has at most two children, referred to as the left child and the right
  child.
- **Binary Search Tree (BST)**: A binary tree where nodes are ordered. Each node's left subtree contains only nodes with
  values less than the node's value, and its right subtree only nodes with values greater than the node's value.
- **Balanced Binary Trees**: These trees ensure that the depth of the two subtrees of every node never differs by more
  than one.

#### 🌲 Binary Search Trees

- **Find**: Searches for a value in the BST. If the value is found, it returns `True`, otherwise `False`.
- **Insert**: Inserts a value into the BST.
  If the value already exists, it will simply traverse the tree without adding a duplicate.

> _Note: The binary search tree operations make certain assumptions for simplicity: no duplicates are allowed, and the
tree does not auto-balance itself._

- **Challenges**:
    - Tree traversal (In-order, Pre-order, Post-order)
    - Finding max depth of a tree
    - _...and more challenges related to trees!_

## 🚀 Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/YourGitHubUsername/learning_python.git
