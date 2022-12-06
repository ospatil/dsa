# Time complexity of build heap operation

Consider the following min heap.

![Min heap](../../misc/min-heap.png?display=inline-block)

Maximum nodes at height $h$ can be computed using the following formula:
$h = \bigg\lceil \frac {n}{2^{h+1}} \bigg\rceil$

The time required by `heapify` when called on a node with height $h$ is $O(h)$.
Letting $c$ be the constant implicit in asymptotic notation, the total cost can be expressed in the following:
$$= \sum_{h=0}^{\log{n}} \bigg\lceil \frac {n}{2^{h+1}} \bigg\rceil ch$$
Moving $h$ into the fraction and $n$ out, ignoring ceiling and the $+1$ exponent in the denominator being same as multiplying by two, the above can be rewritten as follows:
$$= cn \sum_{h=0}^{\log{n}} \frac {h}{2*2^{h}}$$
The multiplication by $2$ in the denominator, being a constant, can be ignored.
$$= cn \sum_{h=0}^{\log{n}} \frac {h}{2^{h}}$$
Upperbounding to `∞`, the above can be rewritten as:
$$\leqslant cn \sum_{h=0}^{\infty} \frac {h}{2^{h}}$$
Now it's clear it's a geometric series with $x = 1/2$, $\sum_{k=0}^{\infty} kx^k = \frac {x}{(1 - x)^2}$
Using the above formula:
$$\leqslant cn * \frac {1/2}{(1 - 1/2)^2} \\ = O(n)$$

>
> *Sources*
> Introduction to algorithms 4ed (Cormen et all) - section 6.3
> <https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity/62177336#62177336>
