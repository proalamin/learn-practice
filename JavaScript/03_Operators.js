// ================================
// JavaScript Operators
// ================================


/*
---------------------------------
Arithmetic Operators
---------------------------------
- Used for mathematical calculations
*/

let a = 10;
let b = 3;

a + b; // addition → 13
a - b; // subtraction → 7
a * b; // multiplication → 30
a / b; // division → 3.333...
a % b; // modulus (remainder) → 1
a ** b; // exponentiation → 1000


/*
---------------------------------
Assignment Operators
---------------------------------
- Assign values to variables
*/

let x = 10;

x += 5;  // x = x + 5 → 15
x -= 3;  // x = x - 3 → 12
x *= 2;  // x = x * 2 → 24
x /= 4;  // x = x / 4 → 6


/*
---------------------------------
Comparison Operators
---------------------------------
- Compare values and return boolean
*/

5 == "5";   // true  (loose comparison - avoid)
5 === "5";  // false (strict comparison - recommended)

10 != "10";  // false
10 !== "10"; // true

8 > 5;   // true
8 < 5;   // false
8 >= 8;  // true
5 <= 3;  // false


/*
---------------------------------
Logical Operators
---------------------------------
- Used with boolean values
*/

true && false; // AND → false
true || false; // OR  → true
!true;         // NOT → false


/*
---------------------------------
Ternary Operator
---------------------------------
- Short form of if-else
*/

let age = 20;

let result = age >= 18
  ? "Adult"
  : "Minor";

console.log(result);


/*
---------------------------------
Type Operators
---------------------------------
*/

typeof "JavaScript"; // string
typeof 10;           // number
typeof true;         // boolean
typeof undefined;    // undefined
typeof null;         // object (JS bug)


/*
---------------------------------
String Operators
---------------------------------
*/

let firstName = "Md";
let lastName = "Amin";

// String concatenation
let fullName = firstName + " " + lastName;

console.log(fullName);


/*
---------------------------------
Logical Assignment Operators (ES2021)
---------------------------------
*/

let isLoggedIn = false;

// Assign only if false
// (If the first value is false, the second value is assigned.)
isLoggedIn ||= true; // true

// -----------------

let count = 0;

// Assign only if null or undefined 
// (If the first value is undefined or null, the second value is assigned.)
count ??= 5; // 0 (unchanged)


/*
---------------------------------
Operator Precedence
---------------------------------
- Determines execution order
*/

let value = 10 + 5 * 2; // 20 (multiplication first)
let value2 = (10 + 5) * 2; // 30 (parentheses first)


/*
---------------------------------
Best Practices
---------------------------------
*/

// Always use === instead of ==
// Use parentheses to avoid confusion
// Keep expressions simple and readable
