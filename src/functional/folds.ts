import assert from 'node:assert/strict';

// Recursive addition of elements of an array
const sum = ([h, ...t]: number[]): number => h === undefined ? 0 : h + sum(t);

assert.equal(sum([1, 2, 3]), 6); // Array with multiple elements
assert.equal(sum([5]), 5); // Array with 1 element
assert.equal(sum([]), 0); // Empty array

// Recursive multiplication of lements of an array
const product = ([h, ...t]: number[]): number => h === undefined ? 1 : h * product(t);

assert.equal(product([2, 2, 3]), 12);
assert.equal(product([5]), 5);
assert.equal(product([]), 1);

/* As we can see sum and product are almost same. The things that vary is the base case value -
 * (0 for sum and 1 for product) and the operation. Let's generalize it.
 */
const foldr = <A, B>(f: (x: A, acc: B) => B, acc: B, [h, ...t]: A[]): B => h === undefined ? acc : f(h, foldr(f, acc, t));

const sumFoldr = (xs: number[]) => foldr((x, acc) => x + acc, 0, xs);
assert.equal(sumFoldr([1, 2, 3]), 6);
assert.equal(sumFoldr([5]), 5);
assert.equal(sumFoldr([]), 0);

const productFoldr = (xs: number[]) => foldr((x, acc) => x * acc, 1, xs);
assert.equal(productFoldr([2, 2, 3]), 12);
assert.equal(productFoldr([5]), 5);
assert.equal(productFoldr([]), 1);

/* Now let's look at foldl */
const foldl = <A, B>(f: (x: A, acc: B) => B, acc: B, [h, ...t]: A[]): B => h === undefined ? acc : foldl(f, f(h, acc), t);

const sumFoldl = (xs: number[]) => foldl((x, acc) => x + acc, 0, xs);
assert.equal(sumFoldl([1, 2, 3]), 6);
assert.equal(sumFoldl([5]), 5);
assert.equal(sumFoldl([]), 0);

const productFoldl = (xs: number[]) => foldl((x, acc) => x * acc, 1, xs);
assert.equal(productFoldl([2, 2, 3]), 12);
assert.equal(productFoldl([5]), 5);
assert.equal(productFoldl([]), 1);

/* Define type and actual function for identity */
type IdType<A> = (x: A) => A;

/* Compose: Compose([f1, f2, f3]) = f1(f2((f3(x)))) */
const compose = <A>(fns: Array<IdType<A>>) => foldr((fn, acc) => x => fn(acc(x)), (x: A) => x, fns);

const add1 = (x: number) => x + 1;
// Or add type to the parameter to conform to IdType<number>
const multiplyBy5 = (x: number) => x * 5;

const composition = compose([add1, multiplyBy5]);
// This is equivalent to addOne(multiplyByFive(10)) === 51
assert.equal(composition(10), add1(multiplyBy5(10)));

/* Now let's look at pipe */
// Pipe([f1, f2, f3]) = f3(f2((f1(x))))
const pipe = <A>(fns: Array<IdType<A>>) => foldl((fn, acc) => x => acc(fn(x)), (x: A) => x, fns);

const divideBy2: IdType<number> = x => x / 2;
const divideBy3: IdType<number> = x => x / 3;
const multiplyBy10: IdType<number> = x => x * 10;

const pipeline = pipe([divideBy2, divideBy3, multiplyBy10]);
// This is equivalent to multiplyBy10(divideBy3(divideBy2(24))) === 40
assert.equal(pipeline(24), multiplyBy10(divideBy3(divideBy2(24))));

/* Let's implement a couple of JavaScript standard apis using folds: map, reduce, not exact but close enough. */

// map - the reason for two type parameters is the returned array can be of any type.
const map = <A, B>(xs: A[], cb: (x: A) => B): B[] => foldl((x, acc) => {
	acc.push(cb(x));
	return acc;
}, [] as B[], xs);

assert.deepEqual(map([1, 2, 3], x => x * 2), [2, 4, 6]);
// To demonstrate usage of return array containing different type
assert.deepEqual(map([1, 2, 3], _x => 'yo'), ['yo', 'yo', 'yo']);

// Reduce
const reduce = <A>([h, ...t]: A[], cb: (pre: A, cur: A) => A) => foldl((x, acc) => cb(x, acc), h, t);

assert.deepEqual(reduce([7, 3, 8], (pre, cur) => pre + cur), 18);
