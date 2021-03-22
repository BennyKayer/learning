const basket = ['apples', 'oranges','grapes'];

for (let i=0; i < basket.length; i++){
    console.log(basket[i]);
}

basket.forEach(item => {
    console.log(item);
});

// for of - python's for in
// this one is iterated
for (item of basket) {
    console.log(item);
}
// for in - loop over keys
// this one is enumerated
const detailedBasket = {
    apples: 5,
    oranges: 10,
    grapes: 1000,
}
for (item in detailedBasket){
    console.log(item);
}
