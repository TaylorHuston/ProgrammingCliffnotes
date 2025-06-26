// Conditionals and loops

function flowControl() {
  let age = 29;

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
    console.log("false"); // Won't print
  }

  console.log(1 == 1); // True
  console.log(1 == "1"); // True, type conversion
  console.log(1 === 1); // True
  console.log(1 === "1"); // False, strict equality
  console.log(1 != 1); // False

  console.log(Boolean("")); // False
  console.log(Boolean("non-empty")); // True
  console.log(Boolean("false")); // True
  console.log(Boolean(0)); // False
  console.log(Boolean(3)); // True

  let score1 = 100;
  let score2 = 200;
  // Ternary      *condition* ? *result if true* : *result if false*
  let highScore = score1 > score2 ? score1 : score2;
  console.log(highScore); // 200

  // Loops
  for (let i = 0; i < 5; i++) {
    console.log(i);
  }

  // This loop will print off odd numbers 1..15
  for (let i = 0; i < 5000; i++) {
    if (i % 2 == 0) {
      continue; // Move to next loop iteration
    }
    console.log(i);
    if (i == 15) {
      break; // End Loop
    }
  }

  // This loop will print all numbers 1..10
  let x = 0;
  while (x < 10) {
    x++;
    console.log(x);
  }

  do {
    x--;
    console.log(x);
  } while (x > 0);

  // Switch
  let lunch = "Sammich";
  switch (lunch) {
    case "Sammich":
      console.log("Sammich, like a sandwich but with 10% more redneck.");
      break;
    case "Candy":
      console.log("Soup is for little kids. Eat a fatburger like an adult.");
      break;
    default:
      console.log("Not hungry?");
  }
}

flowControl();
