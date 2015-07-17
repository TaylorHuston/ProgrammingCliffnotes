//Object syntax

//Create an object
var person1 = {};

//Dot notation for setting attributes
person1.name = "John Doe";

//Create object with pre-defined attributes
var person2 = {
  name: "Jane Doe"
};

console.log(person1.name);
console.log(person2.name);

//Object attributes can be other objects
var people = {};
people.person1 = person1;

//Bracket notation
people["person2"] = person2;

console.log(people["person1"].name);
console.log(people.person2.name);

person1.name = "Jack Doe";
console.log(person1.name);
console.log(people.person1.name);

//When create object with a constructor
var phonebookEntry = new Object();

phonebookEntry.name = 'Taylor Huston';
phonebookEntry.number = '(503) 962-9521';
//Define a method
phonebookEntry.phone = function () {
  console.log('Calling ' + this.name + ' at ' + this.number + '...');
};

//Call a method
phonebookEntry.phone();


//Methods
bob = new Object();
bob.setAge = function (age) { //Object specific method
  bob.age = age;
}
bob.setAge(20);

console.log(bob.age);

var setWeight = function (weight) {
  this.weight = weight;
};
bob.setWeight = setWeight; //Use generic functon as object method
bob.setWeight(150);

console.log(bob.weight);


//Constructor
function Car(make, model) {
  this.make = make;
  this.model = model;
}

var myCar = new Car("Toyota", "Prius");
console.log(myCar.make);


var allTheCars = new Array();
allTheCars.push(myCar);
allTheCars[1] = new Car("Ford", "Focus");
allTheCars.push(new Car("Honda", "Civic"));
