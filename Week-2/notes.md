# 📊 Algorithm Analysis & Asymptotic Notation

---

## 🧠 What is Algorithm Analysis?

* **Analysis** of an algorithm means measuring its **resource consumption** (like time and space).
* It is **theoretical** and helps us **predict performance** without running the code.
* Always done **relative to input size (n)**.

---

## 📈 Growth Rates — How Resource Consumption Changes with Input Size

Understanding how the algorithm scales:

| Growth Type     | Notation     | Description                                                               |
| --------------- | ------------ | ------------------------------------------------------------------------- |
| **Constant**    | `O(1)`       | Resource usage stays the same regardless of input size.                   |
| **Logarithmic** | `O(log n)`   | Doubling the data only adds a small amount of extra work.                 |
| **Linear**      | `O(n)`       | Resource usage increases proportionally to input size.                    |
| **Log-Linear**  | `O(n log n)` | A combination of linear and logarithmic growth (e.g., efficient sorting). |
| **Quadratic**   | `O(n²)`      | Resource usage grows rapidly with input (e.g., nested loops).             |
| **Exponential** | `O(2ⁿ)`      | Each new data point **doubles** the resource usage — very inefficient.    |

---

## ⚖️ Asymptotic Notation — Formal Language of Algorithm Efficiency

Used to express **how resource usage grows** for large input sizes:

| Notation      | Meaning                                                |
| ------------- | ------------------------------------------------------ |
| **Big O**     | `O(f(n))` — Upper Bound — maximum resource usage.      |
| **Omega (Ω)** | `Ω(f(n))` — Lower Bound — minimum resource usage.      |
| **Theta (Θ)** | `Θ(f(n))` — Tight Bound — both upper and lower bounds. |
| **Little o**  | `o(f(n))` — Strict Upper Bound — not equal to `f(n)`.  |

📝 Big-O is **most commonly used** to describe **runtime complexity**.

---

## 🛠 How to Analyze Code

1. **Understand the logic** of the algorithm.
2. **Identify loops, recursive calls, and function calls.**
3. Describe how the number of operations **grows with input size (n)**.
4. Express the growth using appropriate **asymptotic notation**.

---

## 🔁 Real-World Analogy

Imagine your algorithm is a car engine:

* Analysis tells you **how much fuel (resources)** the engine will need **as the road (input size)** gets longer.
* Asymptotic notation gives you a **mathematical fuel efficiency rating.**

---