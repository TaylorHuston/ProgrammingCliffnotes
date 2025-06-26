//Functions

function functions() {
  //Standard functions are hoisted when the file is first loaded, can be used before they are defined
  let x = makeANumber();
  console.log(x); //72

  function makeANumber() {
    return 72;
  }

  let name = "Taylor";

  //Anonymous functions are not hoisted, must be defined in the code before they are used
  let sayHi = function (name) {
    console.log("Nice to meet you " + name);
  };

  sayHi(name);

  //Standard local variable scope applies
  let myScope = 10;

  function simpleFunction() {
    let myScope = 20;
    console.log(myScope); //20
  }
  simpleFunction();
  console.log(myScope); //10

  let adder = function (x, y) {
    return x + y;
  };

  let z = adder(2, 3);
  console.log(z); //5

  //Functions can return other functions and assign them
  function multiplier(factor) {
    return function (number) {
      return number * factor;
    };
  }

  let twice = multiplier(2); //Returns an instance of the nested function above with number = 2;
  console.log(twice(5));

  //Call the returned function automatically
  let third = multiplier(3)(5);
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
    let someBool = myBool;
    for (let i = 1; i < arguments.length; i++) {
      console.log(arguments[i]);
    }
    return;
  }
  someArgs(true, 1, 2, 3);

  function sum() {
    let total = 0;
    for (let i = 0; i < arguments.length; i++) {
      total += arguments[i];
    }
    return total;
  }
  console.log(sum(1, 2, 3));

  //Passing functions to other functions is very powerful
  let anotherArray = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  //In this example you can use any function in the palce of test to filter on any criteria (note that filter is a standard array method, only defined here manually as an example)
  function filter(array, test) {
    let passed = [];
    for (let i = 0; i < array.length; i++) {
      if (test(array[i])) {
        passed.push(array[i]);
      }
    }
    return passed;
  }

  //Pass anonymous function to filter, in this case one that test for even numbers
  console.log(
    filter(anotherArray, function (number) {
      return number % 2 == 0;
    })
  );

  //Apply allows you to call a function and specify the 'this', followed by an array of args
  function speak(x, y) {
    console.log("I am a " + this.type + ", " + x + " " + y);
  }

  let someObject = {
    type: "Human",
  };

  speak.apply(someObject, [10, 12]);

  //Call is similar, but doesn't take the arguments as an array
  speak.call(
    {
      type: "Cat",
    },
    "Hello",
    47
  );

  // Arrow functions are a more concise syntax for writing functions, they do not have their own 'this' context
  const square = (x) => {
    return x * x;
  };

  const person1 = {
    name: "Taylor",
    sayHi: function () {
      console.log("Hi, my name is", this.name);
    },
  };

  person1.sayHi(); // "Hi, my name is Taylor"

  const person2 = {
    name: "Taylor",
    sayHi: () => {
      console.log("Hi, my name is", this.name);
    },
  };

  person2.sayHi(); // "Hi, my name is undefined"
  // In this case, 'this' does not refer to the person object, but to the global context (or undefined in strict mode)
  // Arrow functions do not have their own 'this', they inherit it from the surrounding lexical scope
  // This means that if you use an arrow function inside a method, it will not have
  // access to the object it is defined in, which can lead to unexpected behavior.
}

functions();
