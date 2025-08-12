<h1>BST - Essential member function snippets</h1>

<details>
  <summary>Resursive Code Implementations</summary>
  <br/>
  
  <details>
    <summary>Inserting a node - Recursive</summary>

```py
  def recursive_insert(self, data):
    self.r_insert(data, self.root)

  def r_insert(data, subtree):
    if subtree is None:
      return Node(value)
    elif value < subtree.data:
      subtree.left = self.r_insert(value, subtree.left)
      return subtree
    elif value > subtree.data:
      subtree.right = self.r_insert(value, subtree.right)
      return subtree
```
</details>

<details>
<summary>Searching a node - Recursive</summary>

```py
def recursive_search(self, data):
    return self._r_search(self.root, data)  # Helper function starts from root

def _r_search(self, subtree, data):
    if subtree is None:  # Base case: value not found
        return None
    if data < subtree.data:
        return self._r_search(subtree.left, data)  # Search left subtree
    elif data > subtree.data:
        return self._r_search(subtree.right, data)  # Search right subtree
    else:
        return subtree  # Found the node
      
```
</details>

<details>
<summary>Count number of nodes in BST</summary>

```py
  def count_nodes(self):
    return self.r_count_nodes(self.root)

  def r_count_nodes(self, subtree):
    if subtree is None:
      return 0

    return 1 + self.r_count_nodes(subtree.left) + self.r_count_nodes(subree.right)
```
</details>

<details>
<summary>Height of a BST</summary>

```py
def height_bst(self):
    return self._r_height(self.root)  # Start from root

def _r_height(self, subtree):
    if subtree is None:
        return 0  # Base case: empty subtree has height 0
    return max(self._r_height(subtree.left), self._r_height(subtree.right)) + 1
```
</details>

<details>
<summary>Deleting a node from BST</summary>

```py
def delete_node(self, data):
    self.root = self._r_delete_node(self.root, data)

def _r_delete_node(self, subtree, data):
    if subtree is None:
        return None

    if data < subtree.data:
        subtree.left = self._r_delete_node(subtree.left, data)
    elif data > subtree.data:
        subtree.right = self._r_delete_node(subtree.right, data)
    else:
        # Case 1: No children
        if subtree.left is None and subtree.right is None:
            return None
        # Case 2: One child
        elif subtree.left is None:
            return subtree.right
        elif subtree.right is None:
            return subtree.left
        # Case 3: Two children
        else:
            # Find inorder successor (leftmost in right subtree)
            curr = subtree.right
            while curr.left is not None:
                curr = curr.left
            # Replace data with successor's data
            subtree.data = curr.data
            # Delete the successor
            subtree.right = self._r_delete_node(subtree.right, curr.data)
    
    return subtree
```
</details>


</details>

<details>
  <summary>Iterative Code Implementations</summary>
  <br/>

<details>
  <summary>Breadth First Search</summary>

```py
import queue

def print_bst(self)
  nodes = queue.Queue()

  if self.root is not None
    nodes.put(self.root)

  while not nodes.empty():
    curr = nodes.get()

    if curr.left:
      nodes.put(curr.left)
    if curr.right:
      nodes.put(curr.right)

    print(curr.data, end = "  ")
```

</details>

<details>
<summary>Searching a node</summary>

```py
  def search(self, data):
    if self.root is None:
      return None
  
    curr = self.root
    while curr is not None:
      if data < curr.data:
        curr = curr.left
      elif data > curr.data:
        curr = curr.right
      else:
        return curr
```
</details>

<details>
<summary>Maximum element in BST</summary>

```py
def maximum_element(self):
    if self.root is None:
        return None  # Empty tree
    
    current = self.root
    while current.right is not None:  # Traverse to the rightmost node
        current = current.right
    return current.data  # Return the rightmost node's data
```
</details>

<details>
<summary>Minimum element in BST</summary>

```py
  def minimum_element(self):
    if self.root is None:
      return None
    
    curr = self.root
    while curr.left is not None:
      curr = curr.left
    return curr.data 
```
</details>

<details>
<summary>Inorder Successor</summary>

```py
def inorder_successor(self, data):
    curr = self.root
    successor = None  # Initialize to handle case where we never go left
    
    while curr is not None:
        if data < curr.data:
            successor = curr  # Potential successor
            curr = curr.left
        elif data > curr.data:
            curr = curr.right
        else:  # Node found
            if curr.right:  # Case 1: Has right subtree
                temp = curr.right
                while temp.left:
                    temp = temp.left
                return temp
            return successor
    
    return successor  # Returns None if no successor exists
```

<details>
<summary>Print between</summary>

```py
  def print(self, min_val , max_val):
    self.print_between(self.root, min_val, max_val)

  def print_between(self, subtree, min_val, max_val):
    if subtree is None:
      return

    if min_val < subtree.data:
      self.print_between(subtree.left, min_val, max_val)

    if min_val <= subtree.data  <= max_val:
      print(subtree.data)

    if subtree.data < max_val:
      self.print_between(node.right, min_val, max_val)
```
</details>
</details>
