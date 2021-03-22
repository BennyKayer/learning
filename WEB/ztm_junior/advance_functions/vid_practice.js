const square = (x) => x * x;
const greet = (name) => {
    console.log(`Hello ${name} how are you doing today?`);
}
//Closures - child scope always has access to the parent scope
//Currying
const multiply = (a,b) => a * b;
const curriedMultiply = (a) => (b) => a * b;
const multiplyByFive = curriedMultiply(5);
//Compose
const compose = (f,g) => (a) => f(g(a));
const sum = (num) => num + 1;
compose(sum, sum)(5);
// Avoiding side effects creates functional purity
// basically function returns value
// changes logs etc are side effects
//
