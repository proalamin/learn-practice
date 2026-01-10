// ================================
// JavaScript Loops
// ================================


/*
---------------------------------
for Loop
---------------------------------
- Runs code a fixed number of times
*/

for (let i = 1; i <= 5; i++) {
  console.log(i); // prints 1 to 5
}


/*
---------------------------------
while Loop
---------------------------------
- Runs while condition is true
*/

let count = 1;

while (count <= 3) {
  console.log(count); // prints 1 to 3
  count++;
}


/*
---------------------------------
do...while Loop
---------------------------------
- Runs at least once (condition checked later)
*/

let num = 1;

do {
  console.log(num); // runs once even if condition false
  num++;
} while (num <= 2);


/*
---------------------------------
for...of Loop
---------------------------------
- Used for arrays and iterable objects
*/

let colors = ["red", "green", "blue"];

for (let color of colors) {
  console.log(color);
}


/*
---------------------------------
for...in Loop
---------------------------------
- Used for object properties
*/

let user = {
  name: "Amin",
  age: 22,
  city: "Dhaka"
};

for (let key in user) {
  console.log(key + ":", user[key]);
}


/*
---------------------------------
break Statement
---------------------------------
- Stops the loop immediately
*/

for (let i = 1; i <= 5; i++) {
  if (i === 3) {
    break; // loop stops at 3
  }
  console.log(i);
}


/*
---------------------------------
continue Statement
---------------------------------
- Skips current iteration
*/

for (let i = 1; i <= 5; i++) {
  if (i === 3) {
    continue; // skips 3
  }
  console.log(i);
}


/*
---------------------------------
Looping Arrays with forEach
---------------------------------
*/

let numbers = [10, 20, 30];

numbers.forEach(function (num) {
  console.log(num);
});


/*
---------------------------------
Best Practices
---------------------------------
*/

// Use for...of for arrays
// Use for...in for objects
// Avoid infinite loops
// Keep loop logic simple
