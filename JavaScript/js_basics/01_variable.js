// for console output
console.log("JavaScript is running");

/*
---------------------------------
Variable Declaration
---------------------------------
*/

// 'let' allows reassignment (block scoped)
let age = 22;
age = 23;

// 'const' does NOT allow reassignment
const country = "Bangladesh";
// country = "India"; ❌ TypeError

// 'const' object properties CAN be changed
const user = {
  name: "Amin",
  age: 22
};
user.age = 23; // ✅ allowed


