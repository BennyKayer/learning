const addUID = <T extends object>(obj: T) => {
  let uid = Math.floor(Math.random() * 100);
  return { ...obj, uid };
};

interface Person {
  name: string;
  age: number;
}

const addUID2 = <T extends Person>(obj: T) => {
  let uid = Math.floor(Math.random() * 100);
  return { ...obj, uid };
};

let docOne = addUID({ name: "yoshi", age: 40 });
// let docTwo = addUID('sd')

console.log(docOne.name);

interface Resource<T> {
  uid: number;
  resourceName: string;
  data: T;
}

const docoThree: Resource<object> = {
  uid: 1,
  resourceName: "person",
  data: { name: "shaun" },
};

const docoFour: Resource<Person[]> = {
  uid: 1,
  resourceName: "person",
  data: [{ name: "shaun", age: 12 }],
};
