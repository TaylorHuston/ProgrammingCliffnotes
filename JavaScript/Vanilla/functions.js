//Functions
var functionButton = document.getElementById("functions");

function functions() {

  //Standard functions are hoisted when the file is first loaded, can be used before they are defined
  var x = makeANumber();
  console.log(x); //72

  function makeANumber() {
    return 72;
  }

  var name = prompt("What is your name?");

  //Anonymous functions are not hoisted, must be defined in the code before they are used
  var sayHi = function (name) {
    console.log("Nice to meet you " + name);
  }

  sayHi(name);

  //Standard local variable scope applies
  var myScope = 10;

  function simpleFunction() {
    var myScope = 20;
    console.log(myScope); //20
  }
  simpleFunction();
  console.log(myScope); //10

  var adder = function (x, y) {
    return x + y;
  }

  var z = adder(2, 3);
  console.log(z); //5

  //Functions can return other functions and assign them
  function multiplier(factor) {
    return function (number) {
      return number * factor;
    }
  }

  var twice = multiplier(2); //Returns an instance of the nexted function above with number = 2;
  console.log(twice(5));

  //Standard recursion rules apply
  function power(base, expon) {
    if (expon == 0) {
      return 1;
    } else {
      return base * power(base, expon--);
    }
  }
}

functionButton.onclick = functions;
