// ==================================
// JavaScript Control Flow
// ==================================


/*
---------------------------------
if Statement
---------------------------------
- Executes code if condition is true
*/

let age = 20;

if (age >= 18) {
  console.log("Adult");
}


/*
---------------------------------
if...else Statement
---------------------------------
- Executes one block if true,
  another if false
*/

let score = 45;

if (score >= 50) {
  console.log("Pass");
} else {
  console.log("Fail");
}


/*
---------------------------------
else if Ladder
---------------------------------
- Checks multiple conditions
*/

let marks = 75;

if (marks >= 80) {
  console.log("A+");
} else if (marks >= 70) {
  console.log("A");
} else if (marks >= 60) {
  console.log("B");
} else {
  console.log("Fail");
}


/*
---------------------------------
switch Statement
---------------------------------
- Used instead of multiple if-else
*/

let day = 3;

switch (day) {
  case 1:
    console.log("Saturday");
    break;

  case 2:
    console.log("Sunday");
    break;

  case 3:
    console.log("Monday");
    break;

  default:
    console.log("Invalid day");
}


/*
---------------------------------
Truthy & Falsy in Conditions
---------------------------------
- Used frequently in control flow
*/

let username = "";

if (username) {
  console.log("User exists");
} else {
  console.log("No username"); // runs
}


/*
---------------------------------
Short-circuit Evaluation
---------------------------------
*/

let isLoggedIn = true;

// AND (&&) stops if first is false
isLoggedIn && console.log("Welcome user");

// OR (||) stops if first is true
let displayName = username || "Guest";
console.log(displayName);


/*
---------------------------------
Ternary Operator
---------------------------------
- Short form of if-else
*/

let isAdult = age >= 18
  ? "Yes"
  : "No";

console.log(isAdult);


/*
---------------------------------
Nested Conditions
---------------------------------
*/

let hasCard = true;
let balance = 100;

if (hasCard) {
  if (balance > 50) {
    console.log("Payment successful");
  } else {
    console.log("Insufficient balance");
  }
}


/*
---------------------------------
Best Practices
---------------------------------
*/

// Use switch for fixed values
// Avoid deep nesting (use early return)
// Prefer ternary for simple conditions
