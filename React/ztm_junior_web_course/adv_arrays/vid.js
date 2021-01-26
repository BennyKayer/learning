let array = [1,2,10,15];
// array.forEach((num) => {
//     array.push(num * 2);
//     array.shift();
// })
//map
const mapArray = array.map(num => num * 2);
console.log("array", array);
console.log("mapArray", mapArray);
//filter
const filterArray = array.filter(num => num > 5);
console.log("filterArray", filterArray);
//reduce
const reduceArray = array.reduce((accumulator, num) => {
    return accumulator + num;
}, 0);
console.log("reduce", reduceArray);
