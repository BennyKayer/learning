console.log("Turtle".padStart(10));
console.log("Turtle".padEnd(10));
const fun = (a,b,) => a + b; // ending coma is valid
fun(1,2,);

let obj = {
    username0: "Santa",
    username1: "Rudolf",
    username2: "Grinch"
}

Object.keys(obj).forEach((key, index) => {
    console.log(key, obj[key]);
});

Object.values(obj).forEach(value => {
    console.log(value);
});
Object.entries(obj).forEach(value => {
    console.log(value);
});

Object.entries(obj).map(value => value[1] + value[0].replace("username", ''));

// Async Await
// will come later...
