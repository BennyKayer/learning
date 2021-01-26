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

const circ = (diameter: number) => {
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
let s: string;
let aa: number;
let isll: boolean;

let ninjas: string[];
// error in browser not one here
// ninjas.push("arthur");
let nums: number[] = [];
let bools: boolean[] = [];

let mix: (string | number)[] = [];

let uid: string | number;

let ninjaOne: object = {};
ninjaOne = [];

let ninjaTwo: {
  name: string;
  age: number;
  belt: string;
};

// #6
let a: any = 25;
a = true;

// #7
let greet = (): void => {
  console.log("hello world");
};
// greet = 's'
let ff: Function;

const add = (a: number, b: number, opt?: boolean, opttoo: boolean = true) => {
  return a + b;
};

add(5, 15);
// add(5)
// add('xd', 'xd')

const minus = (a: number, b: number): number => {
  return a - b;
};
let result = minus(10, 7);

// #9
type StringOrNum = string | number;
type Ninja = { name: string; age: number; belt: StringOrNum };

// #10
let gree: (a: string, b: string) => void;
gree = (name: string, greeting: string) => {
  console.log(name + greeting);
};

let calc: (a: number, b: number, c: string) => number;
calc = (numOne: number, numTwo: number, action: string) => {
  if (action === "add") {
    return numOne + numTwo;
  } else {
    return numOne;
  }
};

let logDeatils: (obj: Ninja) => void;
logDeatils = (ninja: Ninja): void => {
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
