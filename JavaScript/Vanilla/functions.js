function functions() {

  //Standard functions are hoisted when the file is first loaded, can be used before they are defined
  var x = makeANumber();
  console.log(x); //72

  function makeANumber() {
    return 72;
  }

  var name = "Taylor"

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

  //Call the returned function automatically
  var third = multiplier(3)(5);
  console.log(third);

  //Standard recursion rules apply
  function power(base, expon) {
    if (expon == 0) {
      return 1;
    } else {
      return base * power(base, expon--);
    }
  }

  //Functions always have access to a special 'arguments' variable
  function someArgs(myBool) {
    var someBool = myBool;
    for (var i = 1; i < arguments.length; i++) {
      console.log(arguments[i]);
    }
    return;
  }
  someArgs(true, 1, 2, 3);

  //Passing functions to other functions is very powerful
  var anotherArray = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  //In this example you can use any function in the palce of test to filter on any criteria (note that filter is a standard array method, only defined here manually as an example)
  function filter(array, test) {
    var passed = [];
    for (var i = 0; i < array.length; i++) {
      if (test(array[i])) {
        passed.push(array[i]);
      }
    }
    return passed;
  }

  //Pass anonymous function to filter, in this case one that test for even numbers
  console.log(filter(anotherArray, function (number) {
    return (number % 2 == 0);
  }));

  //Apply allows you to call a function and specify the 'this', followed by an array of args
  function speak(x, y) {
    console.log("I am a " + this.type + ", " + x + " " + y);
  }

  var someObject = {
    type: "Human"
  };

  speak.apply(someObject, [10, 12]);

  //Call is similar, but doesn't take the arguments as an array
  speak.call({type: "Cat"}, "Hello", 47);
}

functions();
