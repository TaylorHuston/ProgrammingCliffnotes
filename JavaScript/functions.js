//A basic program going over functions
//Based on http://learn.jquery.com/javascript-101/types/ and
//Codeacademy

var name = prompt("What is your name?");


var sayHi = function (name) {
    console.log("Nice to meet you "+name);
}

sayHi(name); //Must be called AFTER the function is defined

var makeANumber = function () { //All functions are var's
    return 72;
}

var x = makeANumber();
console.log(x);

var myScope = 10;

var simpleFunction = function() {  //Standard local variable scope applies
    var myScope = 20;
    console.log(myScope);
}

simpleFunction();
console.log(myScope);

//Methods
bob = new Object();
bob.setAge = function(age) {  //Object specific method
    bob.age = age;
}
bob.setAge(20);

console.log(bob.age);

var setWeight = function(weight) {
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
allTheCars.push(new Car("Honda", "Civic");
