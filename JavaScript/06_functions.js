// ================================
// JavaScript Functions
// ================================


/*
---------------------------------
Function Declaration
---------------------------------
- Standard way to define a function
- Hoisted (can be called before definition)
*/

function greet() {
  console.log("Hello JavaScript");
}

greet(); // function call


/*
---------------------------------
Function Parameters & Arguments
---------------------------------
*/

function add(a, b) {
  return a + b; // returns sum
}

let result = add(5, 3);
console.log(result); // 8


/*
---------------------------------
Function Expression
---------------------------------
- Function stored in a variable
- NOT hoisted
*/

const multiply = function (a, b) {
  return a * b;
};

console.log(multiply(4, 5)); // 20


/*
---------------------------------
Arrow Function (ES6)
---------------------------------
- Shorter syntax
- Does NOT have its own 'this'
*/

const subtract = (a, b) => {
  return a - b;
};

// Single-line arrow function
const square = x => x * x;

console.log(subtract(10, 5)); // 5
console.log(square(4));       // 16


/*
---------------------------------
Default Parameters
---------------------------------
- Used when argument is missing
*/

function welcome(name = "Guest") {
  console.log("Welcome " + name);
}

welcome("Amin");
welcome(); // uses default value


/*
---------------------------------
Return Statement
---------------------------------
- Ends function execution
- Sends value back
*/

function checkAge(age) {
  if (age >= 18) {
    return "Adult";
  }
  return "Minor";
}

console.log(checkAge(20));
console.log(checkAge(15));


/*
---------------------------------
Function Scope
---------------------------------
- Variables inside function
  are not accessible outside
*/

function testScope() {
  let msg = "Inside function";
  console.log(msg);
}

testScope();
// console.log(msg); ❌ ReferenceError


/*
---------------------------------
Rest Parameters
---------------------------------
- Accepts unlimited arguments
*/

function sumAll(...numbers) {
  let total = 0;

  for (let num of numbers) {
    total += num;
  }

  return total;
}

console.log(sumAll(1, 2, 3, 4)); // 10


/*
---------------------------------
Callback Function
---------------------------------
- Function passed as argument
*/

function process(value, callback) {
  callback(value);
}

process("Hello", function (msg) {
  console.log(msg);
});


/*
---------------------------------
Best Practices
---------------------------------
*/

// Use arrow functions for small logic
// Keep functions small and reusable
// Use meaningful function names
