"use strict";
const addUID = (obj) => {
    let uid = Math.floor(Math.random() * 100);
    return Object.assign(Object.assign({}, obj), { uid });
};
const addUID2 = (obj) => {
    let uid = Math.floor(Math.random() * 100);
    return Object.assign(Object.assign({}, obj), { uid });
};
let docOne = addUID({ name: "yoshi", age: 40 });
// let docTwo = addUID('sd')
console.log(docOne.name);
const docoThree = {
    uid: 1,
    resourceName: "person",
    data: { name: "shaun" },
};
const docoFour = {
    uid: 1,
    resourceName: "person",
    data: [{ name: "shaun", age: 12 }],
};
