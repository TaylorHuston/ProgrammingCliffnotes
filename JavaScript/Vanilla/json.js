//Use strinigify to make a JSON object
var string = JSON.stringify({
  name: "Bob",
  born: 1990
});
console.log(string);

//Use parse to extact from JSON
console.log(JSON.parse(string).born);
