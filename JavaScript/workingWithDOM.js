//Syntax that targets the DOM

//Grab an element by it's ID
var myElement = document.getElementById("someParent");
//Return the 'type' of node
//1: Element
//2: Attribute
//3: Test
console.log(myElement.nodeType); //1
console.log(myElement.innerHTML);
//Array of any children nodes
console.log(myElement.childNodes.length);

//Grab an array of all elements by tag
var myLists = document.getElementsByTagName("li");
console.log(myLists.length);

//Only li's inside of 'someParent' div
var someLists = myElement.getElementsByTagName("li");
console.log(someLists.length);

//You can get and set attributes on elements
myElement.setAttribute("class", "someClass");
myElement.setAttribute("align", "left");
console.log(myElement.getAttribute("class"));

//Create and append elements
var newDiv = document.createElement("div");
var newText = document.createTextNode("I'm a generated DIV");
newDiv.appendChild(newText);
myElement.appendChild(newDiv);


//Working with forms
var emailField = document.getElementById("email");

//When the user clicks or tabs into field
emailField.onfocus = function () {
  if (emailField.value == "your email") {
    emailField.value = "";
  }
};

//When the user clicks or tabs out of the field
emailField.onblur = function () {
  if (emailField.value == "") {
    emailField.value = "your email";
  }
};
