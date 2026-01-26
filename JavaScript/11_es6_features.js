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
// find and filter
// --------------------------------

const products =[
  {id:1, name:"p1", price:121},
  {id:2, name:"p2", price:122},
  {id:3, name:"p3", price:121},
]

const result= products.find(products=>products.price==121);
console.log(result); // if not found output undefined


const result1= products.filter(products=>products.price==13321);
console.log(result1); // if not true output is empty array


const id_sum= products.map(product=> product.id*2);
console.log(id_sum);


const id_sum1= products.forEach(product=> product.id*2);
console.log(id_sum1); // not return 

// --------------------------------
// Nullish Coalescing
// --------------------------------

const value = null ?? "default value";


// --------------------------------
// Modules (ES6)
// --------------------------------

// export
// export const version = "ES6";

// import
// import { version } from "./file.js";


// Use const by default
// Prefer arrow functions for small logic
// Use destructuring for cleaner code
