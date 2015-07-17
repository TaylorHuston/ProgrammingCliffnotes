//A basic program going over the different variable types in JS

//Weakly-typed
var a = "I am a string";
var b = 100;
var c = 100.10;
var d = true;

alert(a);
alert(b);
alert(c);
alert(d);

//Change type
b = a;

alert(b);

//Create an object
var person1 = {};

//Dot notation for setting attributes
person1.name = "John Doe";

//Create object with pre-defined attributes
var person2 = {
  name: "Jane Doe"
};

alert(person1.name);
alert(person2.name);

//Object attributes can be other objects
var people = {};
people.person1 = person1;

//Bracket notation
people["person2"] = person2;

alert(people["person1"].name);
alert(people.person2.name);

person1.name = "Jack Doe";
alert(person1.name);
alert(people.person1.name);

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


// Creating an array with the constructor to set initial size
var foo = new Array(100);

// Creating an array with the array literal syntax
var bar = [1, "a", 3.5, true, 2]; //Not type specific

alert(foo.length);
alert(bar.length);
alert(foo[0]); //Undefined
alert(bar[0]);

foo.push("a");
alert(foo[0]); //Still undefined
alert(foo.length);
alert(foo[100]);

alert(foo.pop());
alert(foo.length);

alert(bar.shift());
bar.unshift("x");
alert(bar[0]);

var fub = new Array();
console.log(fub.length);

fub[4] = 4;
console.log(fub.length); //5
console.log(fub[0]); //undefined

var 2 d = [[1, 1], [1, 1]];

var ran = Math.random(); //Between 0 and 1
