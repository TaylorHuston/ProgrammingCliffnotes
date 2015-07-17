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

//Random value
var ran = Math.random(); //Between 0 and 1


var x = 1;
x++;
console.log(x);
x += 10;
console.log(x);
x %= 7; //Modulus
console.log(x);
console.log(x++); //Logs x first, then increments
console.log(++x); //Increments, then logs

//Math has other functions
x = 215.67
var y = Math.round(x);
console.log(x); //215.67
console.log(y); //216
