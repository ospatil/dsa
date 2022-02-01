+++
title = 'Asymptotic Notation'
+++

{{< toc >}}

Consider the example: Given number {{< katex >}}n{{< /katex >}}, write a function to find sum of first {{< katex >}}n{{< /katex >}} natural numbers.

Some solutions (Python):

1. ```py
    def sum1(n):
      return n * (n + 1) / 2
   ```

   Total work done: {{< katex >}}c_{1}{{< /katex >}} and it is not dependent on {{< katex >}}n{{< /katex >}}.

2. ```py
   def sum2(n):
       sum = 0
       for n in range(n + 1):
           sum += n
       return sum
   ```

   Total work done: Some constant work and a loop that executes n times: {{< katex >}}c_{2}n + c_{3}{{< /katex >}}.

3. ```py
     def sum3(n):
         sum = 0
         for i in range(1, n + 1):
             for j in range(1, i + 1):
                 sum += 1
         return sum
   ```

   The inner loop executes:

   - once for `i = 1`
   - twice for `i = 2`
   - thrice for `i = 3`

   So the total work done is:

    {{< katex >}}
    1 + 2 + 3 + ... + n \\
    = n * (n + 1)/2 \\
    = c_{4}{n^2} + c_{5}n + c_{6}
    {{< /katex >}}

## Asymptotic Analysis

{{< hint info>}}
It's a measure of the order of growth of an algorithm in terms of its input size.
{{< /hint >}}

Let's compare the growth of solutions 1 and 2.

Assuming the values of constants as per the figure below, let's find {{< katex >}}n{{< /katex >}}.

![Analysis](/analysis/images/analysis.png)

{{< katex >}}2n + 5 \geqslant 10 \therefore n \geqslant 2.5 \approx 3{{< /katex >}}

So, for any {{< katex >}}n >= 3{{< /katex >}} the constant function `sum1()` will always be faster than `sum2()`.

## Order of growth

A function {{< katex >}}f(n){{< /katex >}}is said to be growing faster than {{< katex >}}g(n){{< /katex >}} if

{{< katex display >}}
\text {for $n \geqslant 0, f(n), g(n) \geqslant 0 $} \\
\lim\limits_{n \to \infty} \frac{g(n)}{f(n)} = 0
{{< /katex >}}

Example:

{{< katex >}}
f(n) = n^2 + n + 6 \hspace{20px} g(n) = 2n + 5 \\
\lim\limits_{n \to \infty} \frac{2n + 5} {n^2 + n + 6} \\
\small \text{dividing by highest term i.e. } n^2 \hspace{10px}
\lim\limits_{n \to \infty} \frac{2/n + 5/n^2} {1 + 1/n + 6/n^2} \\
\small \text{with n tending to } \infty \hspace{10px}
\lim\limits_{n \to \infty} \frac{0 + 0}{1 + 0 + 0} = 0
{{< /katex >}}

So, if {{< katex >}}f(n){{< /katex >}} and {{< katex >}}g(n){{< /katex >}}represent time complexity of algorithms i.e. order of growth, {{< katex >}}g(n){{< /katex >}} is a better algorithm.

{{< hint info >}}

### Direct way to find out the order of growth

1. Ignore lower order terms.
2. Ignore leading constants.
{{< /hint >}}

**Faster growing function dominates a slower growing one.**

Common dominance relations:
{{< katex >}}C < \text {loglog } n < \text {log } n < n^{1/3}< n^{1/2} < n < n^2 < n^3 < 2^n < n^n{{< /katex >}}

## Asymptotic Notations and Best, Average and Worst Cases

### Best, Average and Worst Cases

Let's Consider some examples:

1. ```py
   def nsum(arr, n):
     sum = 0
     for i in range(n):
       sum += arr[i]
     return sum
   ```

   This function is _linear_.

2. ```py
    def nsum(arr, n):
      if n % 2 != 0:
        return 0
      sum = 0
      for i in range(n):
        sum += arr[n]
      return sum
   ```

   _Best Case_: When _n_ is odd, it's going to take _constant_ time. \
   _Average Case_: Often it's impractical to calculate unless you know all the inputs that will be provided to the algorithm all the time. \
   _Worst Case_: When _n_ is even it will be _linear_.

**Worst Case** is considered the most important case for algorithm analysis.

{{< hint warning >}}
**Cases are not related to notations**. You can use the any notation for any case.
{{< /hint >}}

### Asymptotic Notations

_Big O_: Represents _exact_ or _upper_ bound i.e. order of growth. \
_Big Theta (𝛳)_: Represents _exact_ bound. \
_Big Omega (Ω)_: Represents _exact_ or _lower_ bound.

**Big O** is the most common notation used.

#### Big O Notation

{{< hint info >}}
{{< katex >}}f(n) = O(g(n)){{< /katex >}} if and only if there are exact constants {{< katex >}}c{{< /katex >}}and {{< katex >}}n_0{{< /katex >}} such that {{< katex >}}f(n) \leqslant cg(n){{< /katex >}} for all {{< katex >}}n \geqslant n_0{{< /katex >}}.
{{< /hint >}}

In simple terms, _we want to find a function {{< katex >}}g(n){{< /katex >}} that is always going to be equal to or greater than {{< katex >}}f(n){{< /katex >}}when multiplied by a constant for large values of {{< katex >}}n{{< /katex >}}_.

![Big O](/analysis/images/big-o.png)

Example:

{{< katex >}}f(n) = 2n + 3{{< /katex >}}can be written as {{< katex >}}O(n){{< /katex >}} after ignoring co-efficient of highest-growing term and lower-order terms.

Since {{< katex >}}f(n) \leqslant O(g(n){{< /katex >}}, equating it to above gives us {{< katex >}}g(n) = n{{< /katex >}}.

Let's prove it mathematically:

{{< katex >}}
f(n) \leqslant cg(n) \space \forall \space n \geqslant n_0 \\
\text{i.e.}\space(2n + 3) \leqslant cg(n) \\
\text{i.e.}\space(2n + 3) \leqslant cn \space \because g(n) = n
{{< /katex >}}

Quick way to find the value of c is _take leading constant of highest growing term and add 1_.

{{< katex >}}
\therefore c = 3 \\
\small \text{Substituting} \space c \space \text{to find the value of } n_0 \\
2n + 3 \leqslant 3n \\
3 \leqslant n \therefore n_0 = 3 \\
{{< /katex >}}

So for all values of {{< katex >}}n \space \geqslant 3{{< /katex >}}, the equation {{< katex >}}2n+3 \leqslant 3n{{< /katex >}} holds true.

If we try putting some values, say {{< katex >}}n = 4{{< /katex >}}in above equation, we can observe it holds true. Hence proved.

Some more examples:

1. {{< katex >}}\{\frac{n}{4}, 2n + 3, \frac{n}{100} + \log n, 100, \log n, ...\} \in O(n){{< /katex >}}
2. {{< katex >}}\{n^2 + n, 2n^2, \frac{n^2}{100}, ...\} \in O(n^2){{< /katex >}}

Since Big O is upper bound, all functions in 1 can be said to belong to 2, but it helps to use _tight bounds_.

{{< hint info >}}
Big O gives the **upper bound**. If we say an algorithm is linear, then the algorithm in question is {{< katex >}} \leqslant O(n){{< /katex >}}. So, it's going to perform linearly in worst case scenario or better. Therefore Big O is the upper bound of the algorithm.
{{< /hint >}}

#### Big Ω Notation

{{< hint info >}}
{{< katex >}}f(n) = \Omega(g(n)){{< /katex >}} iff there are exact constants {{< katex >}}c{{< /katex >}} and {{< katex >}}n_0{{< /katex >}} such that {{< katex >}}0 \leqslant cg(n) \leqslant f(n){{< /katex >}} for all {{< katex >}}n \geqslant n_0{{< /katex >}}.
{{< /hint >}}

- Big Omega is exact opposite of Big O.
- Big Omega gives the **lower bound** of an algorithm i.e. the algorithm will perform at least or better than it.
- Example - {{< katex >}}f(n) = 2n + 3 = \Omega(n){{< /katex >}}
- {{< katex >}}\{\frac{n}{4}, \frac{n}{2}, 2n, 2n+3, n^2 ...\} \in \Omega(n){{< /katex >}} i.e. all the functions having order of growth greater than or equal to linear.
- If {{< katex >}}f(n) = \Omega(g(n)) \space \small{then} \space g(n) = O(f(n)){{< /katex >}}.

#### Big 𝛳 Notation

{{< hint info >}}
{{< katex >}}f(n) = \Theta(g(n)){{< /katex >}} iff there are exact constants {{< katex >}}c_1, c_2, n_0{{< /katex >}} such that {{< katex >}}0 \leqslant c_1g(n) \leqslant f(n) \leqslant c_2g(n) \space \small{for all} \space n \geqslant n_0{{< /katex >}}.
{{< /hint >}}

- Big Theta gives the **exact bound** on the order of growth of a function.
- Example - For {{< katex >}}f(n) = 2n + 3 = \Theta(n){{< /katex >}}
- If {{< katex >}}f(n) = \Theta(g(n)){{< /katex >}} then \
  {{< katex >}}f(n) = O(g(n)) \text { and } f(n) = \Omega(g(n)) \\
  g(n) = O(f(n)) \text { and } g(n) = \Omega(f(n)){{< /katex >}}
- {{< katex >}}\{\frac{n^2}{4}, \frac{n^2}{2}, n^2, 4n^2, ...\} \in \Theta(n^2){{< /katex >}}
- We should use big 𝛳 notation whenever possible.
