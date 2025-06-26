const a = 4; // a is a global variable, it can be accessed by the functions below

function foo() {
  const b = a * 3; // b cannot be accessed outside foo function, but can be accessed by functions
  // Defined inside foo
  function bar(c) {
    const b = 2; // Another `b` variable is created inside bar function scope
    // The changes to this new `b` variable don't affect the old `b` variable
    console.log(a, b, c);
  }

  bar(b * 4);
}

foo(); // 4, 2, 48

// Let vs Var
function run() {
  var foo = "Foo"; // var is function-scoped or globally-scoped
  let bar = "Bar"; // let is block-scoped, meaning it is only accessible within the block it is defined in

  console.log(foo, bar); // Foo Bar

  {
    var moo = "Mooo";
    let baz = "Bazz";
    console.log(moo, baz); // Mooo Bazz
    console.log(foo, bar); // Foo Bar
  }

  console.log(moo); // Mooo
  //console.log(baz); // ReferenceError
}

// Closures
function makeCounter() {
  let count = 0;
  return function () {
    count++;
    return count;
  };
}

const counter1 = makeCounter();
const counter2 = makeCounter();

counter1(); // 1
counter1(); // 2

counter2(); // 1 ← separate memory!

function makeGreeter(name) {
  return function () {
    console.log("Hello, " + name + "!");
  };
}

const greeter1 = makeGreeter("Taylor");
const greeter2 = makeGreeter("Alex");

greeter1(); // "Hello, Taylor!"
greeter2(); // "Hello, Alex!"

run();
