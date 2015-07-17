//Input and output

var inputOutput = function () {
  alert("I am an alert box");
  confirm("I am a confirm box, click okay to continue");

  var name = prompt("Use a prompt to get data");

  //Pops up
  alert("Hi " + name);

  //Only visible in debugging tools
  console.log("I'm printed to the console");
  console.log(10 < 5); //Can print boolean
  console.log("blahblahblah".substring(3, 7));
  //Other console options, don't really do anything differnet, more for self documentation
  console.error("I am an error");
  console.info("I'm for general info");
  console.debug("I am a debug message");
  console.warn("I am a warning");
};
