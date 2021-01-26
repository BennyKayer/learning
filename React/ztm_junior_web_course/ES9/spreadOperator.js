// Object spread operator
const zoo = {
	tiger : 23,
	lion: 5,
	monkey: 2
}

const {tiger, ...rest} = zoo;

//array
const array = [1, 2, 3, 4, 5];

function sum(a,b,c,d,e) {
	return a + b + c + d + e;
}

console.log(sum(...array));