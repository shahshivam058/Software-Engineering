"""In Python, a **comparator** is a function that determines how two elements should be compared, typically used in sorting. Unlike key functions (like `key=lambda x: x.age`), a comparator directly compares two elements and returns:

* `-1` if the first element is less than the second
* `0` if they are equal
* `1` if the first is greater

---

### 🔧 Using a Comparator in Python

Python’s built-in `sorted()` and `list.sort()` accept a `key` argument, **not** a comparator directly. To use a **comparator**, we need to convert it using `functools.cmp_to_key`.

---

### ✅ Example: Comparator Function for Sorting

Suppose we want to sort a list of tuples by the second element in descending order:

```python
from functools import cmp_to_key

def custom_comparator(a, b):
    # Sort by second element descending
    if a[1] > b[1]:
        return -1
    elif a[1] < b[1]:
        return 1
    else:
        return 0

data = [(1, 3), (2, 2), (3, 1)]

# Use cmp_to_key to convert comparator to key function
sorted_data = sorted(data, key=cmp_to_key(custom_comparator))
print(sorted_data)  # Output: [(1, 3), (2, 2), (3, 1)]
```

---

### 🔁 Difference between `key` and `comparator`

| Feature        | `key` Function                | Comparator Function        |
| -------------- | ----------------------------- | -------------------------- |
| Simpler to use | ✅ Yes                         | ❌ Needs `cmp_to_key`       |
| Performance    | 🔼 Faster (1 comparison/item) | 🔽 Slower (pairwise comp.) |
| Control        | ❌ Limited                     | ✅ Full control over order  |

---

### 🧠 When to Use Comparator?

Use comparator when:

* Sorting is **complex**, and can't be represented as a simple key.
* You need **multi-level custom comparison** (e.g., custom tie-breaker logic).

If you're still unsure when to use `key` vs `comparator`, feel free to give your specific use case and I can suggest the best one.


To **sort a list of tuples by the second element**, use the `key` parameter with a lambda function:

---

### ✅ Example: Ascending Order by 2nd Element

```python
data = [(1, 3), (2, 2), (3, 1)]

# Sort by second element (index 1)
sorted_data = sorted(data, key=lambda x: x[1])

print(sorted_data)
# Output: [(3, 1), (2, 2), (1, 3)]
```

---

### 🔄 Descending Order by 2nd Element

```python
sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

print(sorted_data)
# Output: [(1, 3), (2, 2), (3, 1)]
```

---

### 💡 Want to sort by 2nd element, then by 1st element (tie-breaker)?

```python
data = [(1, 3), (2, 2), (3, 1), (4, 2)]

sorted_data = sorted(data, key=lambda x: (x[1], x[0]))
print(sorted_data)
# Output: [(3, 1), (2, 2), (4, 2), (1, 3)]
```

Let me know if you want to sort using a custom rule (e.g. based on absolute value, or descending first then ascending).

"""