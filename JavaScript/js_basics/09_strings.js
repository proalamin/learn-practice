// ================================
// JavaScript Strings
// ================================


/*
---------------------------------
String Declaration
---------------------------------
- String represents text data
*/

let singleQuote = 'Hello';
let doubleQuote = "JavaScript";
let templateString = `Welcome to JS`;


/*
---------------------------------
String Length
---------------------------------
- Returns number of characters
*/

let text = "JavaScript";
console.log(text.length); // 10


/*
---------------------------------
Accessing Characters
---------------------------------
- Index starts from 0
*/

console.log(text[0]); // J
console.log(text.charAt(4)); // S


/*
---------------------------------
String Concatenation
---------------------------------
*/

let firstName = "Md";
let lastName = "Amin";

// Using + operator
let fullName1 = firstName + " " + lastName;

// Using template literals (recommended)
let fullName2 = `${firstName} ${lastName}`;

console.log(fullName1);
console.log(fullName2);


/*
---------------------------------
Template Literals
---------------------------------
- Allows variables and expressions
*/

let age = 22;
let message = `My name is ${firstName} and I am ${age} years old.`;
console.log(message);


/*
---------------------------------
String Methods (Common)
---------------------------------
*/

let str = "  Hello JavaScript World  ";

str.toUpperCase();   // converts to uppercase
str.toLowerCase();   // converts to lowercase
str.trim();          // removes whitespace
str.trimStart();     // removes start whitespace
str.trimEnd();       // removes end whitespace


/*
---------------------------------
Extracting Parts of String
---------------------------------
*/

str.slice(2, 7);       // "Hello"
str.substring(2, 7);  // "Hello"


/*
---------------------------------
Replacing String Content
---------------------------------
*/

let msg = "I love JavaScript";
msg.replace("love", "learn"); // "I learn JavaScript"


/*
---------------------------------
Search in Strings
---------------------------------
*/

msg.includes("Java");   // true
msg.indexOf("Java");   // 7
msg.startsWith("I");   // true
msg.endsWith("Script");// true


/*
---------------------------------
Split String
---------------------------------
- Converts string to array
*/

let skills = "HTML,CSS,JavaScript";
let skillArray = skills.split(",");
console.log(skillArray);


/*
---------------------------------
String Comparison
---------------------------------
*/

"apple" === "apple"; // true
"apple" > "banana"; // false (lexicographical)


/*
---------------------------------
Escape Characters
---------------------------------
*/

let quote = "He said \"Hello\"";
console.log(quote);


/*
---------------------------------
Best Practices
---------------------------------
*/

// Use template literals instead of +
// Use trim() for user input
// Strings are immutable (original not changed)
