<h1>BST - Essential member function snippets</h1>

<details>
<summary>Breadth First Search</summary>
<br/>
  
```py
import queue

def breadthFirstPrint(self):
  if(self.root):
    q = queue.Queue()
    
  q.put(self.root)

  while not q.empty():
    current = q.get()

    if current.left:
      q.put(current.left)
    if current.right:
      q.put(current.right)

    print(current.data, end=", ")
  print("Done")
      
```

</details>

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
    elif value > subtree.data:
      subtree.right = self.r_insert(value, subtree.right)
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
  
