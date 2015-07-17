//Conditionals and loops

var age = prompt("How old are you?");

if (age > 30) {
  console.log("Damn you old");
} else {
  console.log("Yung'in");
}

if (true && true) {
  console.log("true");
}

if (false || true) {
  console.log("true");
}

if (true && false) {
  console.log("false"); //Won't print
}

console.log(1 == 1); //True
console.log(1 == "1"); //True, type conversion
console.log(1 === 1); //True
console.log(1 === "1"); //False, strict comparison
console.log(1 != 1); //False

var score1 = 100;
var score2 = 200;
//Ternary      *condition* ? *result if true* : *result if false*
var highScore = (score1 > score2) ? score1 : score2;


//Loops
for (var i = 0; i < 5; i++) {
  console.log(i);
}

for (var i = 0; i < 5000; i++) {
  if (i % 2 == 0) {
    continue; //Move to next loop iteration
  }
  console.log(i);
  if (i == 15) {
    break; //End Loop
  }
}

var x = 0;
while (x < 10) {
  x++;
  console.log(x);
}

do {
  x--;
  console.log(x);
} while (x > 0);


//Switch
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
