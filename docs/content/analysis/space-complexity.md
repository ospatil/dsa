+++
title = 'Space Complexity'
weight = 40
+++

{{< toc >}}

It can be defined as:
{{< hint info >}}
Order of growth of memory space in terms of input size.
{{< /hint >}}

Let's consider some examples:

## Example 1

```py
    def sum(n):
        return n * (n + 1)//2
```

The space complexity is {{< katex >}}\Theta(1){{< /katex >}} since only 1 variable is needed.

## Exmaple 2

```py
def sum2(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
```

The space complexity is still {{< katex >}}\Theta(1){{< /katex >}} since only 3 variables are needed.

## Example 3

```py
def arrSum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
```

The space complexity is {{< katex >}}\Theta(n){{< /katex >}} since we need array of size {{< katex >}}n{{< /katex >}}.

{{< hint info >}}
**Auxiliary Space**

Order of growth of extra space (any space other than needed for input and output) in terms of input size.
{{< /hint >}}

For the earlier `arrSum` example, aux space is {{< katex >}}\Theta(1){{< /katex >}} and space complexity is {{< katex >}}\Theta(n){{< /katex >}}.

For arrays and lists, the space complexity is anyways going to be {{< katex >}}\Theta(n){{< /katex >}}.

Therefore, _auxiliary space_ is an important criteria in analysis.

## Space Requirements for Recursive Programs

### Example 1

Consider the following function:

```py
def recSum(n):
    if n <= 0:
        return 0
    return n + recSum(n - 1)
```

The function call stack for the invocation `recSum(5)` can be visualized as follows:

![Recursion Call Stack](/analysis/images/space-complexity-recursive-sum.png)

The number of stack frames is {{< katex >}}n + 1{{< /katex >}}.

The space complexity: {{< katex >}}\Theta(n){{< /katex >}}.

Aux space: {{< katex >}}\Theta(n){{< /katex >}}.

### Example 2

Consider the following fibonacci implementation:

```py
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

Expected results for values of {{< katex >}}n{{< /katex >}}:
n = 0 | n = 1 | n = 2 | n = 3 | n = 4 | n = 5 | n = 6
:---:|:---:|:---:|:---:|:---:|:---:|:---:
0|1|1|2|3|5|8

Here is how the recursion tree will look like for `fib(4)` execution:

![Fibonacci Recursion Tree](/analysis/images/space-complexity-fib.png)

Let's see how the call stack looks like for `fib(4)` execution:

![Fibonacci Recursion Call Stack](/analysis/images/space-complexity-call-stack.png)

As we can see, the maximum number of active stack frames is {{< katex >}}4{{< /katex >}} i.e. height of tree.

Therefore aux space = {{< katex >}}\Theta(n){{< /katex >}}.

{{< hint info >}}
The simple rule to find out the aux space for recursion: **it's always equal to the height of the recursion tree**.
{{< /hint >}}

### Example 3

Consider the following non-recursive implementation for fibonacci:

```py
def fib2(n):
    f = [None for _ in range(n)]
    f[0], f[1] = 0, 1
    for i in range(2, n):
        f[i] = f[i-1] + f[i-2]
    return f[n-1]
```

Space complexity: {{< katex >}}\Theta(n){{< /katex >}}.

Aux space: {{< katex >}}\Theta(n){{< /katex >}}.

Can we reduce the aux space needed?

### Example 4

Conside the following implementation:

```py
def fib3(n):
    if n == 0 or n == 1:
        return n
    a, b, c = 0, 1, 0
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
        print(f"i={i}; c={c}, a={a}, b={b}")
    return c
```

Here is variable tracing looks like for above implementation for {{< katex >}}n = 4{{< /katex >}}:

> a=0, b=1, c=0\
  i=2; c=1, a=1, b=1\
  i=3; c=2, a=1, b=2\
  i=4; c=3, a=2, b=3

Space complexity: {{< katex >}}\Theta(1){{< /katex >}}.

Aux space : {{< katex >}}\Theta(1){{< /katex >}}.
