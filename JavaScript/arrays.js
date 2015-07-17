//Array syntax

// Creating an array with the constructor to set initial size (though arrays in JS are dynamic anyway)
var foo = new Array(100);

// Creating an array with the array literal syntax
var bar = [1, "a", 3.5, true, 2]; //Not type specific

console.log(foo.length); //100
console.log(bar.length); //5
console.log(foo[0]); //Undefined
foo[0] = "a";
console.log(foo[0]); //a

console.log(bar[0]); //1

//Push adds to end
foo.push("z");
console.log(foo[0]); //a
console.log(foo.length); //101
console.log(foo[100]); //z

//Pop removes from end
console.log(foo.pop()); //z
console.log(foo.length); //100

//Shift removes from front
console.log(bar.shift()); //1
//Add to front
bar.unshift("x");
console.log(bar[0]); //x

var fub = new Array();
console.log(fub.length);

fub[4] = 4;
console.log(fub.length); //5
console.log(fub[0]); //undefined

var rand = [1, 5, 3, 9, 8, 3];

var reverse = rand.reverse();
console.log(reverse);

var sorted = rand.sort();
console.log(sorted);

//2D array
var twoD = [[1, 1], [1, 1]];
