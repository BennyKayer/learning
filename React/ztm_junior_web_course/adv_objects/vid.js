// reference type
let object1 = { value: 10};
let object2 = object1;
let object3 = { value: 10};
console.log(object1 === object2);
console.log(object1 === object3);
console.log([] === []);
// context
console.log(this);
console.log(this === window);
// instantiation
class Player{
    constructor(name, type){
        this.name = name;
        this.type = type;
    }
    introduce(){
        console.log(`Hi I am ${this.name} and my class is ${this.type}`);
    }
}
class Wizard extends Player {
    constructor(name, type){
        super(name, type);
    }
    castSpell(){
        console.log("FIREBOLTO");
    }
}
const p1 = new Player("BennyKier", "Paladin");
