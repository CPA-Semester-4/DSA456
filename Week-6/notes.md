Here’s a formalized, simplified, and clear version of your notes in **Markdown (MD)** format:

---

# 📊 Tables (Abstract Data Type - ADT)

A **Table** is an abstract data type used to store **key-value pairs** (also called **records**).

* Each **key is unique**
* The **order** of records **does not matter**

---

## 🔧 Common Operations & Their Complexities

| Operation          | Description                             | Time (Sorted Array) | Time (Unsorted Array) |
| ------------------ | --------------------------------------- | ------------------- | --------------------- |
| `Insert(key, val)` | Add a new key-value pair                | `O(n)`              | `O(1)`                |
| `Modify(key, val)` | Update value of an existing key         | `O(log n)`          | `O(n)`                |
| `Remove(key)`      | Delete record by key                    | `O(n)`              | `O(n)`                |
| `Search(key)`      | Find value by key (most used operation) | `O(log n)`          | `O(n)`                |

> 🔍 **Search** is usually the most frequent operation in table-based structures.

---

## 🧱 Implementations

### ✅ Using **Sorted Array**

* Data is kept sorted by key.
* Enables **Binary Search** (`O(log n)`) due to sorting and random access.
* Can be implemented using:

  * An array of records (each having a key and value)
  * Two parallel arrays (e.g., one for keys, one for values)

### ❌ Using **Unsorted Array**

* No guarantee of order
* Simpler insertions (`O(1)`) — append at end
* Search, modify, and remove take longer due to linear scanning

---

## 💡 Key Insight

The **choice of underlying data structure** depends on:

* Which operations are most important
* How frequently each operation is performed

If **searching** is the top priority → use **sorted arrays**.
If **fast insertion** is more important → use **unsorted arrays**.

---

# 🗂️ Hash Tables – Table (ADT) Implementation

A **Hash Table** is a fast and efficient way to implement the **Table Abstract Data Type (ADT)**, where each record is a unique **key-value pair**.

---

## ⚙️ How Hash Tables Speed Up Table Operations

### 📌 Hash Function

* Converts a **key** into a numerical **hash value**.
* Must return the **same value** for the same key (consistency).
* Runtime is constant: **O(1)** (independent of the number of records).

```js
hashValue = hashFunction(key)
hashIndex = hashValue % capacity
```

> Result: a valid array index from `0` to `capacity - 1`

### 📦 Example: Inserting a Key-Value Pair

```js
insert(key, value) {
    hashValue = hashFunction(key);
    hashIndex = hashValue % capacity;
    array[hashIndex] = record(key, value);
}
```

---

## ⚠️ Collisions in Hash Tables

* **Collision**: When two different keys produce the same `hashIndex`.
* This happens because:

  ```
  Total number of possible keys > Total hash values > Total hash indices
  ```
* ➡️ **Collisions are unavoidable** and must be handled.

---

## 🔄 Collision Resolution Strategies

### 1️⃣ Closed Addressing (a.k.a. Chaining)

* The `hashIndex` **always** maps to the correct index.
* **Multiple records** can be stored at the **same index** (usually as a linked list or dynamic array).
* When accessing:

  * Hash to the index
  * **Search through all records** at that index

> Example: `array[hashIndex] = [record1, record2, ...]`

### 2️⃣ Open Addressing

* The `hashIndex` gives the **ideal spot**, but if it's taken, it searches for the **next available spot** (using probing techniques).
* Common probing methods:

  * **Linear Probing**: check next index `i+1, i+2,...`
  * **Quadratic Probing**: jump by squares `i+1², i+2²,...`
  * **Double Hashing**: use a second hash function to determine jump size

---

## ✅ Summary

| Feature            | Hash Tables                                      |
| ------------------ | ------------------------------------------------ |
| Access/Search      | `O(1)` average (with good hash + low collisions) |
| Insert             | `O(1)` average                                   |
| Remove             | `O(1)` average                                   |
| Handles Collisions | Yes – via **Open** or **Closed Addressing**      |
| Key Uniqueness     | Required                                         |
| Order of Records   | Not maintained                                   |

---

Certainly! Here's the **pseudocode** version, written in a clean and structured format:

---

# 📌 Linear Probing — Pseudocode Only

---

## 🔍 Search(key)

* Compute hash value of key
* Compute index = hash value mod capacity
* Loop starting at index:

  * If slot is empty → key not found → return failure
  * If slot matches key → return value
  * Else → move to next index (circular)

---

## ➕ Insert(key, value)

* Compute hash value of key
* Compute index = hash value mod capacity
* Loop starting at index:

  * If slot is empty or marked as tombstone → insert (key, value) here → stop
  * Else → move to next index (circular)

---

## ✏️ Modify(key, newValue)

* Compute hash value of key
* Compute index = hash value mod capacity
* Loop starting at index:

  * If slot is empty → key not found → stop
  * If slot matches key → update value → stop
  * Else → move to next index (circular)

---

## ❌ Remove(key)

* Compute hash value of key
* Compute index = hash value mod capacity
* Loop starting at index:

  * If slot is empty → key not found → stop
  * If slot matches key:

    * Mark slot as empty
    * Set emptyIndex = current index
    * Set current = next index (circular)
    * While current slot is not empty:

      * Get key at current
      * Compute original index for current key
      * If original index is between emptyIndex and current (circularly):

        * Move current record to emptyIndex
        * Mark current as empty
        * Update emptyIndex = current
      * Move to next index (circular)
    * Stop

---

## 🔁 Cluster of Records

* A cluster is a sequence of consecutive filled slots due to collisions.
* Larger clusters increase the number of probes required for operations.

---

## ⚰️ Tombstoning 


Here's a clean and formalized **pseudocode version** of **Linear Probing with Tombstoning**, covering **Insertion, Search, and Removal**, along with key rules:

---

## ⚰️ Linear Probing with Tombstoning — Pseudocode

### 🟩 Status States for Each Slot

Each array slot stores:

* A key-value pair
* A **status**:

  * `EMPTY`: Slot has never been used
  * `OCCUPIED`: Slot currently holds a valid record
  * `DELETED`: Slot once held a record but has been deleted

---

### ➕ Insertion(key, value)

```
Compute hashValue = hash(key)
Set index = hashValue mod capacity

Loop starting at index (circularly):
    If slot status is OCCUPIED and slot.key == key:
        Update slot.value with new value
        Stop

    If slot status is EMPTY or DELETED:
        Insert (key, value) at this slot
        Set status = OCCUPIED
        Stop
```

---

### 🔍 Search(key)

```
Compute hashValue = hash(key)
Set index = hashValue mod capacity

Loop starting at index (circularly):
    If slot status is EMPTY:
        // Key does not exist in table
        Return NOT FOUND

    If slot status is OCCUPIED and slot.key == key:
        Return slot.value

    // If DELETED or non-matching OCCUPIED
    Move to next index (circularly)
```

> ⚠️ **Important**: Only `EMPTY` stops the search. `DELETED` does **not**.

---

### ❌ Remove(key)

```
Compute hashValue = hash(key)
Set index = hashValue mod capacity

Loop starting at index (circularly):
    If slot status is EMPTY:
        // Key not found
        Stop

    If slot status is OCCUPIED and slot.key == key:
        Set status = DELETED
        Stop

    // If DELETED or non-matching OCCUPIED
    Move to next index (circularly)
```

---

### 📌 Summary Rules

* **Insert** at first slot marked `EMPTY` or `DELETED`
* **Search** stops only at `EMPTY`
* **Remove** marks the slot as `DELETED`, not `EMPTY`

Let me know if you’d like a flowchart or visual diagram of this too.
