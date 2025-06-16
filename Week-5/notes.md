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
| `add_back(x)`    | O(1)            | O(1)               | O(1)               |
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

Sure! Here's a modified and expanded Q\&A list that includes **both singly linked list and array implementations** for stacks and queues. It also covers the idea of circular arrays with two pointers for constant-time queue operations.

---

# 📚 Q\&A: Stacks and Queues with Singly Linked Lists & Arrays

---

### ❓ Q1: How should a **stack** be implemented using a singly linked list?

**✅ A:** Use the **front of the list** for both `push()` and `pop()` operations.
This gives **O(1)** time complexity since no traversal is needed.

---

### ❓ Q2: How should a **stack** be implemented using an array?

**✅ A:** Use the **end of the array** as the top of the stack.

* Track the index of the last element (top pointer).
* `push()` adds an element at the end (increment top pointer).
* `pop()` removes the element from the end (decrement top pointer).
  Both are **O(1)** operations.

---

### ❓ Q3: Why not use the back of a singly linked list for implementing a stack?

**⚠️ A:**

* Without a tail pointer, `push_back()` is **O(n)** due to traversal.
* Even with a tail pointer, `pop_back()` is **O(n)** because singly linked lists lack a `prev` pointer, requiring full traversal to find the second-last node.

---

### ❓ Q4: How should a **queue** be implemented using a singly linked list?

**✅ A:**

* Use a **tail pointer** to efficiently `enqueue()` at the back (`push_back()`) in **O(1)**.
* Use `dequeue()` by removing from the front (`pop_front()`) in **O(1)**.

---

### ❓ Q5: How should a **queue** be implemented using an array for efficient operations?

**✅ A:**

* Use **two pointers (indices)**: one for the front and one for the back of the queue.
* Treat the array as **circular (ring buffer)**: when the back reaches the end of the array, wrap it around to the front if there is space.
* `enqueue()` adds at the back index and increments it (mod array size).
* `dequeue()` removes from the front index and increments it (mod array size).
  Both operations are **O(1)** if the array is not full.

---

### ❓ Q6: What happens if you implement a queue using `pop_back()` in a singly linked list?

**⛔ A:** Bad idea — `pop_back()` is **O(n)** due to traversal to find the second-last node, making dequeue slow.

---

### ❓ Q7: Why is `pop_back()` O(n) in singly linked lists?

**🧠 A:** Because singly linked lists do not store a pointer to the previous node, so you must traverse from the head to find the node just before the last node.

---

### ❓ Q8: Why can't you efficiently `enqueue` or `dequeue` at the front or back of an array without extra pointers?

**🧠 A:**

* Adding/removing at the front requires shifting all elements, which is **O(n)**.
* Using two pointers and treating the array as circular avoids this shifting by wrapping indices.

---

### ❓ Q9: What is the "circular array" or "ring buffer" technique for queues?

**💡 A:**

* The array is treated as circular, meaning the element after the last index is the first index.
* Two indices track the front and back of the queue.
* This allows **constant-time enqueue and dequeue** without shifting elements.

---

### ❓ Q10: Summary — Where should operations happen and their complexity?

| Structure | Implementation   | Operation | Location in Data Structure | Time Complexity | Notes                    |
| --------- | ---------------- | --------- | -------------------------- | --------------- | ------------------------ |
| Stack     | Linked List      | push      | Front                      | O(1)            | Efficient                |
| Stack     | Linked List      | pop       | Front                      | O(1)            | Efficient                |
| Stack     | Array            | push      | End (top)                  | O(1)            | Efficient                |
| Stack     | Array            | pop       | End (top)                  | O(1)            | Efficient                |
| Queue     | Linked List      | enqueue   | Back (with tail pointer)   | O(1)            | Efficient                |
| Queue     | Linked List      | dequeue   | Front                      | O(1)            | Efficient                |
| Queue     | Array (Circular) | enqueue   | Back (circular index)      | O(1)            | Efficient, requires wrap |
| Queue     | Array (Circular) | dequeue   | Front (circular index)     | O(1)            | Efficient, requires wrap |

---

### 💡 Bonus Tip:

If using a **doubly linked list**, both `pop_back()` and `pop_front()` can be done in **O(1)**, since each node has a `prev` pointer.

---