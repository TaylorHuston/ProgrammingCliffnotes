const a = 4; // a is a global variable, it can be accessed by the functions below

function foo() {
  const b = a * 3; // b cannot be accessed outside foo function, but can be accessed by functions
  // defined inside foo
  function bar(c) {
    const b = 2; // another `b` variable is created inside bar function scope
    // the changes to this new `b` variable don't affect the old `b` variable
    console.log(a, b, c);
  }

  bar(b * 4);
}

foo(); // 4, 2, 48

// Let vs Var
function run() {
  var foo = "Foo";
  let bar = "Bar";

  console.log(foo, bar); // Foo Bar

  {
    var moo = "Mooo";
    let baz = "Bazz";
    console.log(moo, baz); // Mooo Bazz
  }

  console.log(moo); // Mooo
  console.log(baz); // ReferenceError
}

run();
