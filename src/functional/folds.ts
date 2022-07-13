import assert from 'node:assert/strict';

// recursive addition of elements of an array
const sum = ([h, ...t]: number[]): number => (h === undefined ? 0 : h + sum(t));

assert.equal(sum([1, 2, 3]), 6);
assert.equal(sum([5]), 5); // array with 1 element
assert.equal(sum([]), 0); // empty array

// recursive multiplication of lements of an array
const product = ([h, ...t]: number[]): number =>
	h === undefined ? 1 : h * product(t);

assert.equal(product([2, 2, 3]), 12);
assert.equal(product([5]), 5);
assert.equal(product([]), 1);

/* as we can see sum and product are almost same. The things that vary is the base case value -
 * (0 for sum and 1 for product) and the operation. Let's generalize it.
 */
const foldr = <A, B>(f: (x: A, acc: B) => B, acc: B, [h, ...t]: A[]): B =>
	h === undefined ? acc : f(h, foldr(f, acc, t));

const sumFoldr = (xs: number[]) => foldr((x, acc) => x + acc, 0, xs);
assert.equal(sumFoldr([1, 2, 3]), 6);

const productFoldr = (xs: number[]) => foldr((x, acc) => x * acc, 1, xs);
assert.equal(productFoldr([2, 2, 3]), 12);

/* now let's look at foldl */
const foldl = <A, B>(f: (x: A, acc: B) => B, acc: B, [h, ...t]: A[]): B =>
	h === undefined ? acc : foldl(f, f(h, acc), t);

const sumFoldl = (xs: number[]) => foldl((x, acc) => x + acc, 0, xs);
assert.equal(sumFoldl([1, 2, 3]), 6);

const productFoldl = (xs: number[]) => foldl((x, acc) => x * acc, 1, xs);
assert.equal(productFoldl([2, 2, 3]), 12);

/* let's implement a couple of JavaScript standard apis using folds: map, reduce, not exact but close enough. */
// map - the reason for two type parameters is the returned array can be of any type.
const map = <A, B>(xs: A[], cb: (x: A) => B): B[] =>
	foldl(
		(x, acc) => {
			acc.push(cb(x));
			return acc;
		},
		[] as B[],
		xs,
	);

assert.deepEqual(
	map([1, 2, 3], (x) => x * 2),
	[2, 4, 6],
);
// to demonstrate usage of return array containing different type
assert.deepEqual(
	map([1, 2, 3], (_x) => 'ho'),
	['ho', 'ho', 'ho'],
);

// reduce
const reduce = <A>([h, ...t]: A[], cb: (pre: A, cur: A) => A) =>
	foldl((x, acc) => cb(x, acc), h, t);

assert.deepEqual(
	reduce([7, 3, 8], (pre, cur) => pre + cur),
	18,
);

/* pipe and compose */
/* define type for identity */
type IdType<A> = (x: A) => A;

const double = (i: number) => i * 2;
const triple = (i: number) => i * 3;
const quadruple = (i: number) => i * 4;

const fns = [double, triple, quadruple];

const plumber =
	<A>(fn1: IdType<A>, fn2: IdType<A>) =>
	(x: A) =>
		fn2(fn1(x));

// since plumber needs two functions to form the pipeline, we need something to start with the
// first function in the array and that something is the id function.
const idNumber: IdType<number> = (x) => x; // id function for number type

let acc = idNumber;

for (const fn of fns) {
	acc = plumber(acc, fn);
}

assert.equal(acc(1), 24); // acc is the final pipe function

// pipe([f1, f2, f3])(x) = f3(f2((f1(x))))
const pipe = <A>(fns: Array<IdType<A>>) =>
	foldl(
		(fn, acc) => (x) => acc(fn(x)),
		(x: A) => x,
		fns,
	);

const half = (x: number) => x / 2;
const third = (x: number) => x / 3;
const tenTimes = (x: number) => x * 10;

const pipeline = pipe([half, third, tenTimes]);
// this is equivalent to tenTimes(third(half(24))) === 40
assert.equal(pipeline(24), tenTimes(third(half(24))));

/* compose: compose([f1, f2, f3])(x) = f1(f2((f3(x)))) */
const compose = <A>(fns: Array<IdType<A>>) =>
	foldr(
		(fn, acc) => (x) => fn(acc(x)),
		(x: A) => x,
		fns,
	);

const plusOne: IdType<number> = (x) => x + 1;
// or add type to the parameter to conform to IdType<number>
const fiveTimes = (x: number) => x * 5;

const composition = compose([plusOne, fiveTimes]);
// this is equivalent to plusOne(fiveTimes(10)) === 51
assert.equal(composition(10), plusOne(fiveTimes(10)));

/* now comes the difficult part - foldl and foldr in terms of each other */
const foldlR = <A, B>(f: (x: A, acc: B) => B, init: B, elems: A[]) =>
	foldr(
		(e, acc) => (x) => acc(f(e, x)), // e is the element from the elems array
		(b: B) => b,
		elems,
	)(init);

// foldl usage - ((((0 * 10 + 1) * 10 + 2) * 10 + 3) * 10 + 4)
const digitSumOp = (x: number, acc: number) => acc * 10 + x;
const digitsToSum = (xs: number[]) => foldl(digitSumOp, 0, xs);
assert.equal(digitsToSum([2, 3, 4, 5]), 2345);

const digitsToSumFoldlR = (xs: number[]) => foldlR(digitSumOp, 0, xs);
assert.equal(digitsToSumFoldlR([2, 3, 4, 5]), 2345);

const foldrL = <A, B>(f: (x: A, acc: B) => B, init: B, elems: A[]) =>
	foldl(
		(e, acc) => (x) => acc(f(e, x)), // e is the element from the elems array
		(b: B) => b,
		elems,
	)(init);

// foldr usage - (16 / (8 / (4/2)))
const succesiveDivideOp = (x: number, acc: number) => x / acc;
const successiveDivide = (divisor: number, xs: number[]) =>
	foldr(succesiveDivideOp, divisor, xs);
assert.equal(successiveDivide(2, [16, 8, 4]), 4);

const successiveDivideFoldrL = (divisor: number, xs: number[]) =>
	foldrL(succesiveDivideOp, divisor, xs);
assert.equal(successiveDivideFoldrL(2, [16, 8, 4]), 4);
