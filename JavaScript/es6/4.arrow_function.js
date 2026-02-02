
// function declaration
function sum(num1, num2=0){
    const total= num1+num2;
    console.log(total);
}
sum(20,22);

// function expression
const addition= function(num1, num2){
    return num1 + num2;
}
const result = addition(33, 43);
console.log(result);


// arrow function
const add2=(n1, n2) => n1 + n2;
const r_add2= add2(232,2);
console.log(r_add2);


// multi line arrow function. --> Requires an explicit return
const add3=(n1, n2) => {
    const result=n1 + n2;
    return result;
};
const r_add3= add3(232,2000);
console.log(r_add3);
