const movePlayer = (distance, direction) => {
	//return new Promise(resolve, reject) ?
}

movePlayer(100, "Left")
	.then( () => movePlayer(200, "Right"))
	.then( () => movePlayer(10, "Left"))
	.then( () => movePlayer(300, "Right"))

// === (it's just syntactic sugar)

async function playerStart() {
	const firstMove = await movePlayer(100, "Left");
	await movePlayer(200, "Right");
	await movePlayer(10, "Left");
	await movePlayer(300, "Right");
}

// I can use await in front of any function that returns a promise

fetch("https://jsonplaceholder.typicode.com/users")
	.then( resp => resp.json() )
	.then(console.log)

// === 

async function fetchUsers(){
	let response = await fetch("https://jsonplaceholder.typicode.com/users");
	response = response.json();
	console.log(response);
}

async function fetchUsers2() {
	const response = await fetch("https://jsonplaceholder.typicode.com/users");
	const data = await response.json();
	console.log(data);
}

