+++
title = 'Analysis of Common Loops'
weight = 20
+++

{{< toc >}}

## Increasing counter

{{< columns >}} <!-- begin columns block -->
**Python**

```py
for i in range(0, n, c):
    # some constant work
```
<---> <!-- magic separator, between columns -->
**JavaScript**

```js
for (let i = 0; i < n; i += c) {
  // some constant work
}
```

{{< /columns >}}

- Example: for `n = 10` and `c = 2`, it will run `5` times `(0, 2, 4, 6, 8)`.
- Time complexity for this loop is {{< katex >}}\Theta(\lfloor \frac{n}{c} \rfloor){{< /katex >}}. Ignoring constants, it's {{< katex >}}\Theta(n){{< /katex >}}.

## Decreasing counter

{{< columns >}}
**Python**

```py
for i in range(n, 0, c) # where c is negative value
    # some constant work
```
<--->
**JavaScript**

```js
for (let i = n; i > 0; i -= c) {
  // some constant work
}
```

{{< /columns >}}

- Example: for `n = 10` and `c = 2`, it will run `5` times `(10, 8, 6, 4, 2)`.
- Time complexity for this loop is {{< katex >}}\Theta(\lceil \frac{n}{c} \rceil){{< /katex >}}.
  Ignoring constants, it's {{< katex >}}\Theta(n){{< /katex >}}.

## Counter getting multiplied in each iteration

{{< columns >}}
**Python**

```py
i = 1
    while i < n:
        # some constant work
        i *= c
```
<--->
**JavaScript**

```js
for (let i = 1; i < n; i *= c) {
  // some constant work
}
```

{{< /columns >}}

- Example:
  For `n = 32` and `c = 2`, it will be executed `5` times `1, 2, 4, 8, 16`.
  For `n = 33` and `c = 2`, it will be executed `6` times `1, 2, 4, 8, 16, 32`.
  Generalizing, it runs for {{< katex >}}1, c, c^2, c^3, ..., c^{k-1}{{< /katex >}} i.e. it runs {{< katex >}}k{{< /katex >}}times from {{< katex >}}1{{< /katex >}} to {{< katex >}}k-1{{< /katex >}}.

  {{< katex display >}}
  c^{k-1} < n \\
  k-1 < \log_c n \\
  k < \log_c n + 1
  {{< /katex >}}

  So, the loop is going to run {{< katex >}}\log_c n + 1{{< /katex >}} times.
- Time complexity for this loop is {{< katex >}}\Theta(\log n){{< /katex >}}.
- Note that base of the log doesn't matter, since bases can be  converted by simple multiplication or division operations and in asymptotic analysis constants are ignored.

## Counter getting divided in each iteration

{{< columns >}}
**Python**

```py
i = n
    while i > 1:
        # some constant work
        i //= c # // is integer division
```
<--->
**JavaScript**

```js
for (let i = n; i > 1; i /= c) {
  // some constant work
}
```

{{< /columns >}}

- Example: \
  For `n = 32` and `c = 2`, it will be executed `5` times `32, 16, 8, 4, 2`.
  For `n = 33` and `c = 2`, it will be executed `6` times 33, 16, 8, 4, 2`.
- Time complexity for this loop is {{< katex >}}\Theta(\log n){{< /katex >}}.

## Counter raised to some power in each iteration

{{< columns >}}
**Python**

```py
i = 2
    while i < n:
        # some constant work
        i = pow(i, c)
```
<--->
**JavaScript**

```js
for (let i = 2; i < n; i = Math.pow(i, c)) {
  // some constant work
}
```

{{< /columns >}}

- Example: For `c = 2` and `n = 32` it's going to run for {{< katex >}}2, 2^2, {(2^2)}^2{{< /katex >}} i.e. `2, 4, 16`.

  Let's find out the number of times the loop runs:

  {{< katex display >}}
  2, 2^c, {(2^c)}^c \\
  2, 2^c, 2^{c^2}, ...2^{c^{k-1}} \text{\footnotesize k is the number of times it runs} \\
  2^{c^{k-1}} < n \\
  c^{k-1} < \log_2 n \\
  k - 1 < \log_2 \log_2 n \\
  k < \log_2 \log_2 n + 1
  {{< /katex >}}
- Time complexity of this loop is {{< katex >}}\Theta(\log\log n){{< /katex >}}.

## Sequential loops

{{< columns >}}
**Python**

```py
def fun(n):
    for i in range(n):          # 𝛳(n)
        # some constant work
    i = 0
    while i < n:                # 𝛳(log n)
        # some constant work
        i *= 2
    for i in range(1, 100):     # 𝛳(1)
        # some constant work
```
<--->
**JavaScript**

```js
function fun(n) {
  for (let i = 0; i < n; i++) {
    // some constant work
  }
  i = 0;
  while(i < n) {
    i *= n;
  }
  for (i = 0; i < 100; i++) {
    // some constant work
  }

}
```

{{< /columns >}}

- Since the work is sequential, we add the values {{< katex >}}\Theta(n) + \Theta(\log n) + \Theta(1){{< /katex >}}.\
  Ignoring lower order terms, the complexity of this function is {{< katex >}}\Theta(n){{< /katex >}}.

## Nested loops

{{< columns >}}
**Python**

```py
def fun(n):
    for i in range(n):            # 𝛳(n)
        j = 0
        while j < n:              # 𝛳(log n)
            # some constant work
            j *= 2
```
<--->
**JavaScript**

```js
function fun(n) {
  for(let i = 0; i < n; i++) {
    let j = 0;
    while(j < n) {
      j *= 2;
    }
  }
}
```

{{< /columns >}}

- Since it's a nested loop,we multiply the values {{< katex >}}\Theta(n) * \Theta(\log n){{< /katex >}}.\
  Therefore the complexity is {{< katex >}}\Theta(n \log n){{< /katex >}}.

## Nested loops 2

{{< columns >}}
**Python**

```py
def fun(n):
    for i in range(n):          # 𝛳(n)
        for j in range(n):      # 𝛳(n)
            # some constant work
```
<--->
**JavaScript**

```js
function fun(n) {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      // some constant work
    }
  }
}
```

{{< /columns >}}

- The time complexity is {{< katex >}}\Theta(n^2){{< /katex >}}.
