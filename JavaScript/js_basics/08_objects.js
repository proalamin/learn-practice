// ================================
// JavaScript Objects
// ================================


/*
---------------------------------
Object Declaration
---------------------------------
- Object is a non-primitive data type
- Stores data in key-value pairs
*/

const user = {
  name: "Amin",
  age: 22,
  city: "Dhaka"
};


/*
---------------------------------
Accessing Object Properties
---------------------------------
*/

// Dot notation (recommended)
console.log(user.name); // Amin

// Bracket notation (useful for dynamic keys)
console.log(user["age"]); // 22


/*
---------------------------------
Adding & Updating Properties
---------------------------------
*/

user.email = "amin@example.com"; // add new property
user.age = 23;                   // update existing property

console.log(user);


/*
---------------------------------
Deleting Properties
---------------------------------
*/

delete user.city;
console.log(user);


/*
---------------------------------
Object with Methods
---------------------------------
- Function inside object is called method
*/

const person = {
  name: "Amin",
  greet: function () {
    console.log("Hello, " + this.name);
  }
};

person.greet(); // Hello, Amin


/*
---------------------------------
this Keyword
---------------------------------
- Refers to the current object
*/

const car = {
  brand: "Toyota",
  showBrand() {
    console.log(this.brand);
  }
};

car.showBrand(); // Toyota


/*
---------------------------------
Looping Through Objects
---------------------------------
*/

// Using for...in
for (let key in user) {
  console.log(key + ":", user[key]);
}


/*
---------------------------------
Object Methods (Built-in)
---------------------------------
*/

console.log(Object.keys(user));   // array of keys
console.log(Object.values(user)); // array of values
console.log(Object.entries(user));// key-value pairs


/*
---------------------------------
Object Destructuring
---------------------------------
*/

const { name, age } = user;
console.log(name);
console.log(age);


/*
---------------------------------
Spread Operator with Objects
---------------------------------
*/

const extraInfo = {
  country: "Bangladesh",
  role: "Student"
};

const fullUser = { ...user, ...extraInfo };
console.log(fullUser);


/*
---------------------------------
Nested Objects
---------------------------------
*/

const student = {
  name: "Amin",
  address: {
    city: "Dhaka",
    zip: 1207
  }
};

console.log(student.address.city); // Dhaka


/*
---------------------------------
Optional Chaining (ES2020)
---------------------------------
- Prevents runtime error
*/

console.log(student.address?.city);   // Dhaka
console.log(student.contact?.phone);  // undefined


/*
---------------------------------
Best Practices
---------------------------------
*/

// Use const for objects
// Use dot notation when possible
// Avoid deep nesting
// Use optional chaining for safety
