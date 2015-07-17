//Functions

var name = prompt("What is your name?");

var sayHi = function (name) {
  console.log("Nice to meet you " + name);
}

sayHi(name);

//All functions are var's
var makeANumber = function () {
  return 72;
}

var x = makeANumber();
console.log(x);

//Standard local variable scope applies
var myScope = 10;
var simpleFunction = function () {
  var myScope = 20;
  console.log(myScope);
}
simpleFunction();
console.log(myScope);

var adder = function(x,y) {
  return x+y;
}

var z = adder(2,3);
console.log(z);
