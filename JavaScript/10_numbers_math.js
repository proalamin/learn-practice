// ================================
// JavaScript Numbers & Math
// ================================


/*
---------------------------------
Number Declaration
---------------------------------
- JavaScript has only ONE number type
*/

let a = 10;        // integer
let b = 3.14;      // floating point
let c = 1e5;       // 100000 (exponential notation)


/*
---------------------------------
Number Methods
---------------------------------
*/

let num = 12.5678;

num.toFixed(2);      // "12.57" → rounds to 2 decimals
num.toPrecision(4); // "12.57" → total digits


/*
---------------------------------
Converting to Number
---------------------------------
*/

Number("10");      // 10
parseInt("10.5");  // 10
parseFloat("10.5");// 10.5


/*
---------------------------------
NaN (Not a Number)
---------------------------------
*/

let result = "abc" / 2;

console.log(result);        // NaN
console.log(isNaN(result)); // true


/*
---------------------------------
Infinity
---------------------------------
*/

let big = 1 / 0;
console.log(big); // Infinity


/*
---------------------------------
Math Object
---------------------------------
- Used for mathematical operations
*/

Math.PI; // 3.141592653589793


/*
---------------------------------
Math Rounding Methods
---------------------------------
*/

Math.round(4.6); // 5  (nearest)
Math.floor(4.9); // 4  (down)
Math.ceil(4.1);  // 5  (up)
Math.trunc(4.9); // 4  (remove decimal)


/*
---------------------------------
Math Power & Root
---------------------------------
*/

Math.pow(2, 3); // 8
Math.sqrt(16);  // 4
Math.abs(-10);  // 10


/*
---------------------------------
Math Min & Max
---------------------------------
*/

Math.min(1, 3, 5); // 1
Math.max(1, 3, 5); // 5


/*
---------------------------------
Random Numbers
---------------------------------
*/

Math.random(); // random number between 0 and 1

// Random number between 1 and 10
let randomNum = Math.floor(Math.random() * 10) + 1;
console.log(randomNum);


/*
---------------------------------
Number Comparison
---------------------------------
*/

0.1 + 0.2 === 0.3; // false (floating point issue)

// Correct way
(0.1 + 0.2).toFixed(2) == 0.3; // true


/*
---------------------------------
Best Practices
---------------------------------
*/

// Use Math.floor for random integers
// Be careful with floating point precision
// Use Number() for safe conversion
