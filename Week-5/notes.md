# Lists & Linked Lists — Summary Notes

## 🔹 What is a List?

* **ADT (Abstract Data Type)**: Ordered collection of elements.
* **Order matters**, but not necessarily sorted.
* Supports **duplicates** or **unique** elements.

### 📌 Common List Operations

* `add_front(x)`
* `add_back(x)`
* `get_front()`, `get_back()`
* `get_at(i)`
* `remove_front()`, `remove_back()`
* `traverse()`

---

## 🔹 List Implementations

### 1. **Array-based**

* Stored in contiguous memory.
* Fast access: O(1) indexing.
* Insertion/removal at front: O(n).
* Resize: Doubling capacity → **Amortized O(1)** insert at end.

### 2. **Linked List-based**

* Elements in **nodes**, linked via pointers.
* No direct access: O(n) lookup.
* O(1) insertion/removal (known position).

| Operation        | Array (no grow) | Singly Linked List | Doubly Linked List |
| ---------------- | --------------- | ------------------ | ------------------ |
| `add_front(x)`   | O(n)            | O(1)               | O(1)               |
| `add_back(x)`    | O(1)            | O(n)               | O(1)               |
| `remove_front()` | O(n)            | O(1)               | O(1)               |
| `remove_back()`  | O(1)            | O(n)               | O(1)               |

---

## 🔹 Linked Lists Overview

### Types:

* **Singly Linked List**: `next` pointer only.
* **Doubly Linked List**: `next` and `prev` pointers.

### Key Components:

* **Node**:

  * Stores `data`, `next` (and `prev` in doubly list).
* **List Object**:

  * Points to `front` (and `back` for optimization).

### Python Class Structure:

```python
class LinkedList:
    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev
    def __init__(self):
        self.front = None
        self.back = None
```

---

## 🔹 push\_front(data)

### Without Sentinel:

```python
def push_front(self, data):
    nn = self.Node(data, self.front)
    if self.front is None:
        self.back = nn
    else:
        self.front.prev = nn
    self.front = nn
```

---

## 🔹 pop\_front()

### Without Sentinel:

```python
def pop_front(self):
    if self.front is not None:
        rm = self.front
        self.front = self.front.next
        if self.front is None:
            self.back = None
        else:
            self.front.prev = None
        del rm
```

---

## 🔹 Sentinel Nodes

### Why?

* Eliminate special case checks for empty lists or single-node lists.

### With Sentinel – Initialization:

```python
def __init__(self):
    self.front = self.Node(None)
    self.back = self.Node(None, None, self.front)
    self.front.next = self.back
```

### push\_front (With Sentinel):

```python
def push_front(self, data):
    nn = self.Node(data, self.front.next, self.front)
    self.front.next.prev = nn
    self.front.next = nn
```

### pop\_front (With Sentinel):

```python
def pop_front(self):
    if self.front.next is not self.back:
        rm = self.front.next
        rm.next.prev = rm.prev
        rm.prev.next = rm.next
        del rm
```

---

## 🔹 Advantages & Disadvantages

### ✅ Array

* Fast indexing
* Good memory locality
* Easy to binary search

### ❌ Array

* Costly insertions/removals (except at end)
* Resizing overhead

### ✅ Linked List

* Fast insert/delete anywhere (if position known)
* No preallocation needed

### ❌ Linked List

* Slow lookup
* More memory (pointers)
* Poor cache performance

---

## 🔹 Memory

* **Array**: extra space due to unused capacity.
* **Linked List**: extra pointers → higher per-node overhead.

---

## 🔹 Iterators (Conceptual)

Used to **traverse** container structures:

* `first` → start of container
* `next()` → move to next element
* `isDone()` → check end
* `currentItem()` → get current element

---

✅ **Recap**:

* List is an abstract idea (sequence, order matters).
* Implement using arrays or linked nodes.
* Linked list operations require careful handling.
* Sentinel nodes simplify logic by eliminating edge cases.

---
