//A basic program going over the different variable types in JS

function variables() {
  //Weakly-typed
  var a = "I am a string";
  var b = 100;
  var c = 100.1;
  var d = true;
  var e = a + " " + b; //Concatenation

  console.log(a);
  console.log(b);
  console.log(c);
  console.log(d);
  console.log(e);

  console.log(typeof a); //string
  console.log(typeof b); //number
  console.log(typeof c); //number
  console.log(typeof d); //boolean
  console.log(typeof e); //string

  //Change type
  b = a;

  console.log(b); //I am a string

  //Random value
  var ran = Math.random(); //Between 0 and 1 (but not including 1)

  var x = 1;

  x++;
  console.log(x); //2

  x += 10;
  console.log(x); //12

  x %= 7; //Modulus
  console.log(x); //5

  x *= 10;
  console.log(x); //50
  console.log(x++); //50. Logs x first, then increments
  console.log(++x); //52. Increments, then logs

  //Math has other functions
  x = 215.67;
  var y = Math.round(x);
  var z = Math.floor(x);
  console.log(x); //215.67
  console.log(y); //216
  console.log(z); //215

  var aString = "55"; // String
  console.log(isNaN(aString)); // is Not a Number, true
  var aNumber = Number(aString); // Convert to number
  console.log(isNaN(aNumber)); // is Not a Number, false

  console.log(Math.PI); // BRING ME SOME PIE

  var name = "John";
  console.log("Hello".concat(" ", name, "!")); // Using concat to join strings
  console.log(`Hello ${name}!`); // Using template literals to join strings
  console.log("Hello " + name + "!"); // Using + to join strings
}

variables();
