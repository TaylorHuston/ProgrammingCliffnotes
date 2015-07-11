//A basic program going over the different input and output methods
//Based on http://learn.jquery.com/javascript-101/types/ and
//Codeacademy

var inputOutput = function () {
  alert("I am an alert box");
  confirm("I am a confirm box, click okay to continue");

  var name = prompt("Use a prompt to get data");

  alert("Hi " + name);

  console.log("I'm printed to the console");
  console.log(10 < 5); //Can print boolean
  console.log("blahblahblah".substring(3, 7));
};
