const urls = [
	'https://jsonplaceholder.typicode.com/users',
	'https://jsonplaceholder.typicode.com/posts',
	'https://jsonplaceholder.typicode.com/albums',
]

const getData = async function() {
	const [users, posts, albums] =  await Promise.all(urls.map(url => {
		const resp = await fetch(url);
		return resp.json();
	}));
	console.log("users", users);
	console.log("posts", posts);
	console.log("albums", albums);
}

const getData2 = async function() {
	const arrayOfPromises = urls.map(url => fetch(url));
	for await (request of arrayOfPromises){
		const data = await request.json();
		console.log(data);
	}
}