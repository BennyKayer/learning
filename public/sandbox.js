"use strict";
// #2
// const character = "mario";
// console.log(character);
// const inputs = document.querySelectorAll("input");
// inputs.forEach((input) => {
//   console.log(input);
// });
// #3
// Values ok types no
let character = "mario";
character = "luigi";
// character = false
let age = 30;
let isBlackBelt = false;
const circ = (diameter) => {
    return diameter * Math.PI;
};
console.log(circ(5));
// console.log(circ("xd"));
// #4
let names = ["luigi", "mario", "yoshi"];
names.push("wario");
// names.push(3)
// names[0] = 3
let mixed = ["ken", 3, true];
mixed.push("xd");
mixed.push(4);
mixed.push(false);
mixed[0] = false;
let ninja = {
    name: "mario",
    belt: "black",
    age: 30,
};
// ninja.age = false
// ninja.skills = ['xd', 'wont work']
// ninja = {
//   isBlack: false
// }
// #5
let s;
let aa;
let isll;
let ninjas;
// error in browser not one here
// ninjas.push("arthur");
let nums = [];
let bools = [];
let mix = [];
let uid;
let ninjaOne = {};
ninjaOne = [];
let ninjaTwo;
// #6
let a = 25;
a = true;
// #7
let greet = () => {
    console.log("hello world");
};
// greet = 's'
let ff;
const add = (a, b, opt, opttoo = true) => {
    return a + b;
};
add(5, 15);
// add(5)
// add('xd', 'xd')
const minus = (a, b) => {
    return a - b;
};
let result = minus(10, 7);
// #10
let gree;
gree = (name, greeting) => {
    console.log(name + greeting);
};
let calc;
calc = (numOne, numTwo, action) => {
    if (action === "add") {
        return numOne + numTwo;
    }
    else {
        return numOne;
    }
};
let logDeatils;
logDeatils = (ninja) => {
    console.log(ninja.age);
    console.log(ninja.name);
    console.log(ninja.belt);
};
// #11
// const anchor: HTMLAnchorElement | null = document.querySelector("a");
// if (anchor) {
//   console.log(anchor.href);
// }
// const ul = document.querySelector("ul")!;
// console.log(ul);
// console.log(anchor?.href);
