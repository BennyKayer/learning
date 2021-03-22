//Evaluate these:
//#1
[2] === [2] //false
{} === {} //false

//#2 what is the value of property a for each object.
const object1 = { a: 5 };
const object2 = object1; //object2 now references object1
const object3 = object2; //object3 now references object1
const object4 = { a: 5}; //new object
object1.a = 4;
//object1, object2, object3 a = 4
//object4 a = 5

//#3 create two classes: an Animal class and a Mamal class.
// create a cow that accepts a name, type and color and has a sound method that moo's her name, type and color.
class Animal{
    constructor(name, type){
        this.name = name;
        this.type = type;
    }
}
class Mammal extends Animal{
    constructor(name, type, color){
        super(name, type);
        this.color = color;
    }
}
class Cow extends Mammal{
    constructor(name, type, color){
        super(name, "Cow", "White");
    }
    mooInfo(){
        console.log(`Mooo name is ${this.name} I am a ${this.type} and moooo color is ${this.color}`);
    }
}
const sandie = new Cow("Sandie");
sandie.mooInfo();
