// ================================
// ES6 (ECMAScript 2015) FEATURES
// ================================


// --------------------------------
// let & const
// --------------------------------

let count = 10;        // block scoped, reassignable
const PI = 3.1416;     // block scoped, not reassignable


// --------------------------------
// Arrow Functions
// --------------------------------

const add = (a, b) => a + b;
const square = x => x * x;


// --------------------------------
// Template Literals
// --------------------------------

const name = "Amin";
const age = 22;

const message = `My name is ${name} and I am ${age} years old`;


// --------------------------------
// Default Parameters
// --------------------------------

function greet(user = "Guest") {
  return `Hello ${user}`;
}


// --------------------------------
// Destructuring (Array)
// --------------------------------

const numbers = [10, 20, 30];
const [first, second] = numbers;


// --------------------------------
// Destructuring (Object)
// --------------------------------

const user = {
  id: 1,
  role: "Student"
};

const { id, role } = user;


// --------------------------------
// Spread Operator (Array)
// --------------------------------

const a = [1, 2];
const b = [...a, 3, 4];


// --------------------------------
// Spread Operator (Object)
// --------------------------------

const extraInfo = { country: "Bangladesh" };
const fullUser = { ...user, ...extraInfo };


// --------------------------------
// Rest Parameter
// --------------------------------

function sum(...nums) {
  return nums.reduce((total, n) => total + n, 0);
}


// --------------------------------
// for...of Loop
// --------------------------------

for (const num of numbers) {
  console.log(num);
}


// --------------------------------
// Optional Chaining
// --------------------------------

const student = {
  profile: {
    email: "test@mail.com"
  }
};

student.profile?.email;
student.contact?.phone; // undefined (no error)


// --------------------------------
// Nullish Coalescing
// --------------------------------

const value = null ?? "default value";


// --------------------------------
// Modules (ES6)
// --------------------------------

// export
export const version = "ES6";

// import
// import { version } from "./file.js";


// --------------------------------
// Best Practices
// --------------------------------

// Use const by default
// Prefer arrow functions for small logic
// Use destructuring for cleaner code
