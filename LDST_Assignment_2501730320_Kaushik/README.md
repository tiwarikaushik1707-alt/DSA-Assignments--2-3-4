# Linear Data Structures Toolkit (LDST)

## 📌 Overview

This project implements core **Linear Data Structures** from scratch using Python as part of the *Data Structures (ETCCDS202) Unit–2 Assignment*.

The toolkit demonstrates how fundamental data structures work internally and applies them to solve a real-world problem.

---

## 🚀 Features

* Dynamic Array (with resizing logic)
* Singly Linked List
* Doubly Linked List
* Stack (LIFO) using Linked List
* Queue (FIFO) using Linked List
* Balanced Parentheses Checker (application of Stack)

---

## 🧠 Concepts Covered

* Sequential data storage
* Dynamic memory handling
* Pointer-based structures
* Abstract Data Types (ADT)
* Time complexity and amortized analysis

---

## 🛠️ Technologies Used

* Python 3.x
* No external libraries (implemented from scratch)

---

## 📂 Project Structure

```
LDST_Assignment_RollNo_Name/
│
├── ldst_toolkit.py   # Main implementation
├── output.txt        # Program output
├── report.pdf        # Analysis and explanation
```

---

## ▶️ How to Run

### Using Python Launcher (Windows):

```
py ldst_toolkit.py
```

### OR:

```
python ldst_toolkit.py
```

To save output:

```
py ldst_toolkit.py > output.txt
```

---

## 🔍 Implemented Data Structures

### 1. Dynamic Array

* Custom implementation similar to Python list
* Automatically resizes when full (capacity doubles)
* Supports append and pop operations

### 2. Singly Linked List

* Insert at beginning and end
* Delete by value
* Traverse elements

### 3. Doubly Linked List

* Insert after a node
* Delete at a given position
* Supports bidirectional traversal

### 4. Stack (LIFO)

* push, pop, peek
* Implemented using linked list for O(1) operations

### 5. Queue (FIFO)

* enqueue, dequeue, front
* Uses head and tail pointers for efficiency

---

## ⚙️ Application: Balanced Parentheses Checker

* Validates expressions using Stack
* Supports: `()`, `{}`, `[]`
* Ensures correct order and matching

### Example:

```
([])  → Balanced
([)]  → Not Balanced
((()  → Not Balanced
""    → Balanced
```

---

## 📊 Time Complexity Summary

| Data Structure | Operation       | Complexity  |
| -------------- | --------------- | ----------- |
| Dynamic Array  | append          | O(1)*       |
|                | pop             | O(1)        |
| Linked List    | insert/delete   | O(1) / O(n) |
| Stack          | push/pop        | O(1)        |
| Queue          | enqueue/dequeue | O(1)        |

* Amortized O(1)

---

## 📖 Learning Outcomes

* Understood internal working of linear data structures
* Implemented structures without built-in shortcuts
* Learned amortized analysis
* Applied stack in solving a real problem

---

## 📚 References

* Python Documentation
* GeeksforGeeks (for conceptual understanding)

---

## 👨‍💻 Author

**Kaushik Tiwari**
B.Tech – Computer Science Engineering

---

## Note :- This project is part of an academic assignment. All implementations are written from scratch for learning purposes.
