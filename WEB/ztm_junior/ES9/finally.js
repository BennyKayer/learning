const urls = [
	'https://swapi.co/api/people/1',
	'https://swapi.co/api/people/2',
	'https://swapi.co/api/people/3',
	'https://swapi.co/api/people/4'
]

Promise.all(urls.map( url => {
	return fetch(url).then(resp => resp.json());
})).then(array => {
	//throw Error; // to see what finally reveives when catch tirggers
	for (item of array){
		console.log(array.indexOf(item), item);
	}
}).catch (error => console.log("Fix it: "))
.finally(data => console.log("extra: ", data));