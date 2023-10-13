# Nth Fibonacci Number

## 💡 First approach 
Calculate all the Fibonacci series numbers, storing them in RAM memory.

```python
def fib(n):
    if n <= 1:
        return n

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % 1000000007

    return fib[n]
```

This approach is easily readable and adds flexibility to access other elements of the list. However, it is inefficient in terms of memory usage.

## 🏆  Proposed solution 
Iterative approach not storing all Fibonacci numbers in a list.
Instead, it only keeps track of two variables for the current numbers. This is more memory-efficient as it doesn't store past numbers. 😃

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a
```

## 📊 Complexity 
Both functions have a time complexity of O(n), so they are equally efficient in that regard. 
The choice between them will depend on your personal preferences, the memory requirements of your application,
and the need to access additional Fibonacci numbers.

- Time Complexity: O(n)
- Auxiliary Space: O(1)

## 💬 Conclusion
If memory efficiency is a priority, the `fib(n)` function provided may be the better choice. 
If readability and flexibility are more important, the first approach of `fib(n)` function could be preferable.