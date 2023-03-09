"""
Hashmap essentially is an array of fixed size.

Hashing is best suited when we have requirements of search, insert and delete.
    It does it in average O(1)
    It's not useful for:
        - Finding closest value - Use AVL or reb-black trees
        - Sorted data           - Use AVL or reb-black trees
        - Prefix searching      - Use Trie

Applications of hashing:
    - dictionaries
    - Database indexing
    - Cryptography
    - Caches
    - Symbol tables in compilers/interpreters
    - Routers

Requirements of hash functions:
1. should always map a large key to same small key
2. should generate values from 0 to (m - 1) where m is the size of the hashtable
3. should be fast: O(1) for integers and O(len) for strings
4. should uniformly distribute keys into hashtable slots

Examples of hash functions:
1. h(large_key) = large_key % m
    m is usually a prime near to the map size. Why? - because there will be less
    common factors in division and therefore better distribution of large keys
    power of 2 or 10 is bad since it won't distribute properly since x % 2^3 means we
    are considering only last 3 bits of the number ignoring rest
2. For strings, weighted sum (x can be any number, for example x = 33)
    (str[0] * x^0 + str[1] * x^1 + str[2] * x^2 ...) % m
3. Universal hashing - you have a set of hash functions and you pick a function randomly
    and you use that function to hash all data in the hashtable.


Collision handling:

If we know keys in advance, we can design a perfect hashing function but that's not
the case and therefore there will always be collisions.
Birthday paradox - If there are 23 people in a room, probability that 2 people having
    same birthday is 50%, with 70 people it goes up to 99.9%.

Resolution strategies
1. Chaining
2. Open addressing
    1. linear probing
    2. quadratic probing
    3. double hashing

Chaining
Maintain array of linked lists. In case of collision, insert the item at end of linked list
Performance of chaining -
n = no of keys to be inserted
m = number of slots in hashtable
load factor ⍺ = n / m
load factor denotes how big you want your hash table to be. It's a trade-off between space and
time. For small hash tables i.e. high load factor, collisions are more.
With the assumption that the hash function distributes the keys uniformly, the expected
chain length will be ⍺ i.e. equal to load factor.
Time to search/insert/delete = O(1 + ⍺) (1 for hash computation and ⍺ for chain length)

Data structures to store chains:
- linked list (not cache-friendly, search insert and delete is O(l), l is chain length)
- dynamic arrays (cache-friendly, search insert and delete is O(l), l is length)
    (list in python, ArrayList in Java)
- self-balancing BST (Avl tree, red-black tree)
    search/insert/delete O(log l), not cache-friendly
    Java 8 onwards uses these to implement hashmaps

Open addressing
Basic requirement: no of slots >= no of keys
Idea is we use single array only without any list or any other data structure.
cache-friendly

How can we implement open addressing?

1. Linear probing
We generate hash using hash function and linearly search next empty slot
if case of collision.
hash(key, i) = (h(key) + i) % m where h(key) = key % m
For example: with m = 7, hash(key, i) = (h(key) + i) % 7
When we want to insert into a slot and that slot is occupied, we start with i = 1,
if that is occupied too, be go to next to next slot i.e. i = 2.

If last slot is occupied, we wrap-around the search, i.e. start from beginning
of the array.
For searching a value,
    we calculate the hash of the key, compare the value in the index,
    if it doesn't match, we continue with next slot.
    We stop when one of the following three conditions occurs
    1. till we encounter an empty slot.
    2. key found
    3. Traverse through the whole table. What if the table is full?
    in such case we search in circular fashion and stop at the index
    we started with and still don't find the key, we can conclude
    it's not present in the hash table.
Delete:
    We calculate the hash, go to the index, but we can't simply make the slot
    empty, since the search (as described above) will fail. So, we mark the
    slot with special value "DELETED" and during search we don't stop when we
    see a "DELETED" slot.

Problems - formation of "primary" clusters near occupied slots and all the operations
become costly since we have to search through the size of the cluster.

Solved by

2. Quadratic probing
h(key, i) = (h(key) + i^2) % m

so, first time collision happens, go to next slot (1^2)
2nd collision to to 2^2 i.e. 4th slot
3rd collision go to 3^2 i.e. 9th slot

Problems:
- "secondary" cluster
- may not find a slot even when available. It's proven to work only when:
    1. ⍺ < 0.5 (so basically no of slots is at least double the no of keys)
    2. m is prime

Solved by

3. Double hashing
Use two hash functions - original one and other in case of collision
h(key, i) = (h1(key) + i*h2(key)) % m

if h2(key) is relatively prime to m, it will always find a free slot.
What is relatively prime? when two numbers have no common factors other than 1.

The second hash function must not evaluate to 0 since we'll always be reaching
the same location again and again. (replace 0 in the equation above to see)

A popular second hash function is h2(key) = PRIME - (key % PRIME)
Example:
Consider m = 7
Original hash function: h1(key) = key % 7
Second hash function: h2(key) = 6 - (key % 6)
For h2, we can use 6 since it's relative prime to 7
h2(key) tells us the shift we need to make from current location identified by h1(key).
Assume h2(key) = 6
Let's calculate all the shifts:
First collision:(1 * 6) % 7 = 6
Second:         (2 * 6) % 7 = 5
Third:          (3 * 6) % 7 = 4
Fourth:         (4 * 6) % 7 = 3
Fifth:          (5 * 6) % 7 = 2
Sixth:          (6 * 6) % 7 = 1

As we can see, this gives us a different slot for every progressive collision.

Double hashing insert algorithm:

    def doubleHashingInsert(key):
        if table is full:
            return error
        probe = h1(key), offset = h2(key)
        while table[probe] is occupied:
            probe = (probe + offset) %m
        table[probe] = key

Performance analysis of search (unsuccessful):
    The search is unsuccessful if we have either traversed through the whole table or we encounter an empty slot
    ⍺ = n/m (should be <= 1)
    Assumption: every probe sequence looks at a random location where the key should be placed, i.e. every free slot
    is equally likely to be picked.
    (1 - ⍺) fraction of the table is empty
    Consider ⍺ = 0.8 i.e. 80% of the table is occupied, 20% free i.e. 1/5 of slots are empty
    then it will take 5 iterations to find an empty slot (we'll find 4 occupied slots and then an empty slot).
    With ⍺ = 0.9, 1/10 of slots are empty and will take 10 iterations
    Expected number of probes = 1/(1 - ⍺) (1 - ⍺ is the fraction of the table that is empty)
    As ⍺ -> 1, the number of probes tends to be infinite. For example, if ⍺ = 0.99, the number of probes will be 100.

Chaining vs open addressing (OA)
1. With chaining, hashtable never fills since the chains will grow. You might want to resize it to
avoid performance hit but it's not mandatory. With OA, since it's the main array that stores everything,
it will get full and resizing will be mandatory.
2. Chaining is less sensitive to hash functions while OA has problem of clustering depending on the hash
function.
3. Chaining is not cache-friendly while OA is.
4. For chaining, extra space needed for chaining. For OA, extra space might be required to achieve same
performance as chaining. It's interesting to compare the performance in case of unsuccessful search:
for chaining, it's (1 + ⍺) and for OA, it's 1/(1 - ⍺).
If ⍺ is 0.9, i.e. the table is 90% full, then
for chaining it's 1.9 comparisons
and for OA, it's 1/(1 - 0.9) = 1/0.1 = 10 comparisons
So to achieve same performance in OA, we'll have to reduce ⍺, i.e. increase the table size.

Rehashing - The process of increasing the array size and moving the elements to their new position
"""


import unittest


class ChainHash:
    def __init__(self, size=7):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def get_val(self, key):
        bucket_id = hash(key) % self.size  # get hash and get bucket
        bucket = self.buckets[bucket_id]
        for _, rec in enumerate(bucket):
            rec_key, rec_val = rec
            if rec_key == key:  # record found, return val
                return rec_val
        else:
            return None

    def put_val(self, key, val):
        bucket_id = hash(key) % self.size  # get hash and get bucket
        bucket = self.buckets[bucket_id]
        for i, rec in enumerate(bucket):
            rec_key, _ = rec
            if rec_key == key:  # record found, replace val
                bucket[i] = (key, val)
                return
        bucket.append((key, val))

    def delete_val(self, key):
        bucket_id = hash(key) % self.size
        bucket = self.buckets[bucket_id]
        for i, rec in enumerate(bucket):
            rec_key, _ = rec
            if rec_key == key:
                bucket.pop(i)
                break


class OpenAddressHash:
    def __init__(self, cap):
        self.cap = cap
        self.buckets = [-1] * cap  # all slots initialized to -1
        self.size = 0 . # to keep track of number of elements in the array

    def hash(self, x):
        return x % self.cap  # simple hash function

    def insert(self, x):
        # this can be made dynamic by doubling the size and copying the elements
        if self.size == self.cap:  # table full, can't insert
            return False
        if self.search(x) is True:  # key already present, won't insert
            return False
        i = self.hash(x)
        t = self.buckets
        while t[i] not in (-1, -2):  # -1 is empty slot, -2 deleted
            i = (i + 1) % self.cap  # increment the index in circular way

        t[i] = x
        self.size += 1
        return True

    def search(self, x):
        h = self.hash(x)
        t = self.buckets
        i = h  # start with the index corresponding to hash
        while (t[i] != -1):  # -1 is empty slot, continue search till we encounter an empty slot
            if t[i] == x:  # found it
                return True
            i = (i + 1) % self.cap # increment the index in circular way
            if (i == h):  # search wrapped around as we are back at the original index, table full and x not present
                return False
        return False  # encountered an empty slot, x not present

    def remove(self, x):
        # the implementation is almost same as search
        h = self.hash(x)
        t = self.buckets
        i = h # start with the index corresponding to hash
        while t[i] != -1:
            if t[i] == x:
                t[i] = -2  # this is the only change, -2 denotes deletion
                return True
            i = (i + 1) % self.cap
            if i == h:
                return False
        return False


class HashTests(unittest.TestCase):
    def test_chainhash(self):
        chain_hash = ChainHash()
        self.assertIsNone(chain_hash.get_val(2))

        chain_hash.put_val("name", "frodo")
        self.assertEqual(chain_hash.get_val("name"), "frodo")

        chain_hash.put_val("name", "gandalf")
        self.assertEqual(chain_hash.get_val("name"), "gandalf")

        chain_hash.delete_val("name")
        self.assertIsNone(chain_hash.get_val("name"))


if __name__ == "__main__":
    unittest.main()
