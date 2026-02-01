/*
---------------------------------
Data Types
---------------------------------
*/

// Primitive data types -> Primitive → stores single value, stored by value
let name = "JavaScript"; // string
let count = 10;         // number
let isActive = true;    // boolean
let x;                  // undefined
let y = null;           // null

// Non-primitive data types -> Non-Primitive → stores collection/structure, stored by reference
let numbers = [1, 2, 3]; // array
let person = {           // object
  name: "Amin",
  age: 22
};

// Check data type
console.log(typeof name); // string
console.log(typeof null); // object (JavaScript bug)


/*
---------------------------------
Type Conversion
---------------------------------
*/

// Explicit type conversion
Number("10");   // converts string to number
String(20);     // converts number to string
Boolean(1);     // converts to boolean (true)

// Implicit type conversion
"5" + 1; // "51" (number converted to string)
"5" - 1; // 4    (string converted to number)