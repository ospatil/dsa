+++
title = 'Analysis of Recursion'
weight = 30
+++

{{< toc >}}

Let's go through some examples to get a hang of how to derive time taken {{< katex >}}T(n){{< /katex >}} for recursive functions.

## Examples

### Example 1

{{< columns >}}
**Python**

```py
def fun(n):
    if n <= 1:
        return
    for i in range(n):      # 𝛳(n)
        print("something")
    fun(n//2)               # T(n/2)
    fun(n//2)               # T(n/2)
```
<--->
**JavaScript**

```js
function fun(n) {
  if(n <= 1) {
    return;
  }
  for(let i = 0; i < n; i++) {
    console.log('something');
  }
  fun(Math.floor(n/2));
  fun(Math.floor(n/2));
}
```

{{< /columns >}}

Time taken: {{< katex >}}T(n) = 2T(n/2) + \Theta(n){{< /katex >}} \
Base case: {{< katex >}}T(1) = C{{< /katex >}}

### Example 2

{{< columns >}}
**Python**

```py
def fun(n):
    if n <= 1:
        return
    print("something")      # 𝛳(1)
    fun(n//2)               # T(n/2)
    fun(n//2)               # T(n/2)
```
<--->
**JavaScript**

```js
function fun(n) {
  if(n <= 1) {
    return;
  }
  console.log('something');
  fun(Math.floor(n/2));
  fun(Math.floor(n/2));
}
```

{{< /columns >}}

Time taken: {{< katex >}}T(n) = 2T(n/2) + C{{< /katex >}} \
Base case: {{< katex >}}T(1) = C{{< /katex >}}

### Example 3

{{< columns >}}
**Python**

```py
def fun(n):
    if n <= 0:
        return
    print(n)        # 𝛳(1)
    fun(n - 1)      # T(n - 1)
```
<--->
**JavaScript**

```js
function fun(n) {
  if(n <= 0) {
    return;
  }
  console.log(n);
  fun(n - 1);
}
```

{{< /columns >}}

Time taken: {{< katex >}}T(n) = T(n - 1) + C{{< /katex >}} \
Base case: {{< katex >}}T(1) = C{{< /katex >}}

## Recursion Tree Method

Once the value of {{< katex >}}T(n){{< /katex >}} is written recursively, we can use **Recursion Tree Method** to find the actual value of {{< katex >}}T(n){{< /katex >}}. Here are the steps for it:

  1. Write non-recursive part as root of tree and recursive parts as children.
  2. Keep expanding children until a pattern emerges.

### Example 1

{{< katex >}}T(n) = 2T(n/2) +Cn \\
T(1) = C
{{< /katex >}}

![Recursion1](/analysis/images/recursion-recursion1.png)

{{< katex >}}cn{{< /katex >}} work is being done at every level.\
The work is getting reduced by half in each recursion. Therefore the height of tree is {{< katex >}}\log_2 n{{< /katex >}}.\
Total work done: {{< katex >}}cn + cn + cn + \dots \space \log n \space \text{times i.e.} \space cn \log n{{< /katex >}}.\
Therefore, the time complexity is {{< katex >}}\Theta(n \log n){{< /katex >}}.

### Example 2

{{< katex >}}
T(n) = 2T(n-1) + C \\
T(1) = C
{{< /katex >}}

![Recursion2](/analysis/images/recursion-recursion2.png)

We are reducing by 1 in each recursion, therefore the height of tree will be {{< katex >}}n{{< /katex >}}.\
Total work done: {{< katex >}}C + 2C + 4C + \dots \text{for} \space n{{< /katex >}} times.\
It's a geometric progression: {{< katex >}}C(1 + 2 + 4 + ... + n){{< /katex >}}.\
Therefore, the time complexity is {{< katex >}}\Theta(2^n){{< /katex >}}.

{{< hint info >}}
Formula for geometric progression:
{{< katex display >}}
\frac{a *(r^n-1)}{r-1} \\
\text {\footnotesize where r = common ratio, a = first term}
{{< /katex >}}
{{< /hint >}}

### Example 3

{{< katex >}}
T(n) = T(n/2) + C \\
T(1) = C
{{< /katex >}}

![Recursion3](/analysis/images/recursion-recursion3.png)

Total work done: {{< katex >}}C + C + \dots \space \log n{{< /katex >}} times.\
Therefore, the time complexity is {{< katex >}}\Theta(\log n){{< /katex >}}.

### Example 4

{{< katex >}}
T(n) = 2T(n/2) + C \\
T(1) = C
{{< /katex >}}

![Recursion4](/analysis/images/recursion-recursion4.png)

Total work done: {{< katex >}}C + 2C + 4c + \dots \space \log n{{< /katex >}} times.\
{{< katex >}}
C(1 + 2 + 4 + \dots \space \log n) \\
a = 1, r = 2 \\
\text {\footnotesize applying geometric progression formula} \\
\frac {2^{\log n} - 1}{2-1} \\
2^{\log n } = n
{{< /katex >}}

Therefore, the time complexity is {{< katex >}}\Theta(n){{< /katex >}}.

## Incomplete trees

We can still use _Recursion Tree_ method for incomplete trees, but instead of exact bound we'll get upper bound.

### Example 1

{{< katex >}}
T(n) = T(n/4) + T(n/2) + Cn \\
T(1) = C
{{< /katex >}}

![Incomplete1](/analysis/images/recursion-incomplete1.png)

In this example, the left subtree will reduce faster than the right one.\
We'll assume this is a full tree and therefore will get upper bound {{< katex >}}O{{< /katex >}} instead of the exact bound {{< katex >}}\Theta{{< /katex >}}.

Total work done: {{< katex >}}Cn + 3Cn/4 + 9Cn/16{{< /katex >}} and height of tree is {{< katex >}}\log n{{< /katex >}}.

It's a geometric progression with ratio less than 1.

{{< hint info >}}
Formula for geometric progression with ratio < 1:
{{< katex display >}}
\frac{a}{1-r} \\
\text {\footnotesize where r = common ratio} \\
\text {\footnotesize a = first term}
{{< /katex >}}
{{< /hint >}}

{{< katex >}}a = Cn, r = 3/4{{< /katex >}}\
applying geometric progression formula
{{< katex >}}\frac {Cn}{1-3/4}{{< /katex >}}\
ignoring constants, the complexity is
{{< katex >}}n{{< /katex >}}

The time complexity is {{< katex >}}O(n){{< /katex >}}.

### Example 2

{{< katex >}}
T(n) = T(n-1) + T(n-2) + C \\
T(1) = C
{{< /katex >}}

![Incomplete2](/analysis/images/recursion-incomplete2.png)

It's not a full tree with height {{< katex >}}n{{< /katex >}}.
Total work done: {{< katex >}}C + 2C + 4C + \dots \space \text{for} \space n \space \text{times}{{< /katex >}}.\
It's a geometric progression: {{< katex >}}C(1 + 2 + 4 + ... + n){{< /katex >}}.
Therefore, the time complexity is {{< katex >}}O(2^n){{< /katex >}}.
