# Week 1 - Introduction to Python

### 🧠 Core Concepts

* **Tabs vs Spaces**: Stick to one; mixing causes errors.
* **Variable Initialization**: Python requires variables to be initialized before use. Type is inferred from the assigned value.
* **No ++ or --**: Use `x += 1` or `x -= 1` instead.
* **Lists vs Arrays**: Python does not have built-in arrays like C/C++. Use `list`, which behaves like JS arrays — dynamic and indexable.
* **Python Shell**: Start by typing `python` in the terminal.
* **Pointers-Like Behavior**: Variables point to memory locations; reassigning creates a new reference.

### 🧱 Classes in Python

* Use `__init__` to initialize object attributes.
* Use `self` to access instance variables.
* Python doesn't require member variable declarations before assignment inside `__init__`.

```python
class Dog:
    def __init__(self, name):
        self.name = name
```

### 🔬 Lab Insight

* Watched and reflected on a YouTube video about algorithm analysis.

---