// Solve the below problems:


// #1) Check if this array includes the name "John".
const dragons = ['Tim', 'Johnathan', 'Sandy', 'Sarah'];
dragons.includes("John");

// #2) Check if this array includes any name that has "John" inside of it. If it does, return that
// name or names in an array.
const dragons = ['Tim', 'Johnathan', 'Sandy', 'Sarah'];
dragons.filter((name) => name.includes("John"));

// #3) Create a function that calulates the power of 100 of a number entered as a parameter
const power = (base) => (exponent) => base ** exponent;
const power100 = power(100);
console.log(power100(2)); // 10000

// #4) Useing your function from #3, put in the paramter 10000. What is the result?
// Research for yourself why you get this result
const power10000 = power(10000);
console.log(power10000(10));
