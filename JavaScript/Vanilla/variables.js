//A basic program going over the different variable types in JS

var varButton = document.getElementById("variables");

function variables() {
  //Weakly-typed
  var a = "I am a string";
  var b = 100;
  var c = 100.10;
  var d = true;

  console.log(a);
  console.log(b);
  console.log(c);
  console.log(d);

  //Change type
  b = a;

  console.log(b);

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
  x = 215.67
  var y = Math.round(x);
  var z = Math.floor(x);
  console.log(x); //215.67
  console.log(y); //216
  console.log(z); //215

  var aString = "55"; //String
  var aNumber = Number(aString);
  console.log(isNaN(aNumber)); //is Not a Number, false
}

varButton.onclick = variables;
