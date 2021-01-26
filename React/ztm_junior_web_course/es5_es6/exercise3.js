// change everything below to the newer Javascript!

// let + const
let a = 'test';
const b = true;
let c = 789;
a = 'test2';


// Destructuring
const person = {
    firstName : "John",
    lastName  : "Doe",
    age       : 50,
    eyeColor  : "blue"
};

let {firstName, lastName, age, eyeColor} = person;


// Object properties
// let a = 'test';
// let b = true;
// let c = 789;

const okObj = {
  a,
  b,
  c
};


// Template strings
let message = `Hello ${firstName} + have I met you before? I think we met in ${city} last summer no???`;

// default arguments
// default age to 10;
function isValidAge(age = 10) {
    return age;
}

// Symbol
// Create a symbol: "This is my first Symbol"
const sym = Symbol("Hogwarth");
// Arrow functions
const whereAmI = (username, location) => {
    if (username && location) {
        return "I am not lost";
    } else {
        return "I am totally lost!";
    }
}
