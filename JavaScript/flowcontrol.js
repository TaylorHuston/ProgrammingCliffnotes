//A basic program going over the different conditionals and loops

var age = prompt("How old are you?");

if (age > 30) {
  console.log("Damn you old");
} else {
  console.log("Yung'in");
}

console.log(1 == 1); //True
console.log(1 == "1"); //True, type conversion
console.log(1 === 1); //True
console.log(1 === "1"); //False, strict comparison

for (var i = 0; i < 5; i++) {
  console.log(i);
}

var x = 0;
while (x < 10) {
  x++;
  console.log(x);
}

do {
  x--
  console.log(x);
} while (x > 0);

var lunch = "Sammich";
switch (lunch) {
case "Sammich":
  console.log("Sammich, like a sandwich but with 10% more redneck");
  break;

case "Soup":
  console.log("Soup is for little kids. Eat a fatburger like a man.");
  break;

default:
  console.log("Not hungry?");
}
