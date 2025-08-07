

<details>
<summary>Breadth First</summary>
  
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
<summary></summary>

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
  
