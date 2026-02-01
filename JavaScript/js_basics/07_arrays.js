// ================================
// JavaScript Arrays
// ================================


/*
---------------------------------
Array Declaration
---------------------------------
- Array is a non-primitive data type
- Used to store multiple values
*/

let numbers = [1, 2, 3, 4, 5];
let fruits = ["apple", "banana", "mango"];


/*
---------------------------------
Accessing Array Elements
---------------------------------
- Index starts from 0
*/

console.log(numbers[0]); // 1
console.log(fruits[2]);  // mango


/*
---------------------------------
Array Length
---------------------------------
- Returns total number of elements
*/

console.log(numbers.length); // 5


/*
---------------------------------
Adding Elements
---------------------------------
*/

// Add element at end
numbers.push(6);

// Add element at start
numbers.unshift(0);

console.log(numbers); // [0,1,2,3,4,5,6]


/*
---------------------------------
Removing Elements
---------------------------------
*/

// Remove last element
numbers.pop();

// Remove first element
numbers.shift();

console.log(numbers); // [1,2,3,4,5]


/*
---------------------------------
Looping Through Arrays
---------------------------------
*/

// Using for loop
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}

// Using for...of loop (recommended)
for (let fruit of fruits) {
  console.log(fruit);
}


/*
---------------------------------
Array Methods (Very Important)
---------------------------------
*/

// map → transforms array
let squared = numbers.map(num => num * num);
console.log(squared); // [1,4,9,16,25]

// filter → selects elements
let evenNumbers = numbers.filter(num => num % 2 === 0);
console.log(evenNumbers); // [2,4]

// reduce → combines values
let total = numbers.reduce((sum, num) => sum + num, 0);
console.log(total); // 15


/*
---------------------------------
find & includes
---------------------------------
*/

// find → returns first matching value
let found = numbers.find(num => num > 3);
console.log(found); // 4

// includes → checks existence
console.log(numbers.includes(3)); // true
console.log(numbers.includes(10)); // false


/*
---------------------------------
Array Destructuring
---------------------------------
*/

let [first, second] = fruits;
console.log(first);  // apple
console.log(second); // banana


/*
---------------------------------
Spread Operator with Arrays
---------------------------------
*/

let newNumbers = [...numbers, 6, 7];
console.log(newNumbers);


/*
---------------------------------
Best Practices
---------------------------------
*/

// Use map/filter/reduce instead of loops
// Avoid modifying original array when possible
// Use const for arrays (mutation allowed)
