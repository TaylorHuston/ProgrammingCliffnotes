//Syntax that targets the DOM
var domButton = document.getElementById("dom");

function dom() {
  // Grab an element by it's ID
  var myElement = document.getElementById("someParent");
  //Return the 'type' of node
  //1: Element
  //2: Attribute
  //3: Text
  console.log(myElement.nodeType); //1

  console.log(myElement.innerHTML);

  // NodeList of any children nodes
  console.log(myElement.childNodes.length);

  // Grab a NodeList of all elements by tag
  var myLists = document.getElementsByTagName("li");
  console.log(myLists.length);

  // Only li's inside of 'someParent' div
  var someLists = myElement.getElementsByTagName("li");
  console.log(someLists.length);

  // You can get and set attributes on elements
  myElement.setAttribute("class", "someClass");
  myElement.setAttribute("align", "left");
  console.log(myElement.getAttribute("class"));

  //Add a class
  myElement.className = "someOtherClass";
  console.log(myElement.getAttribute("class"));

  //Create and append elements
  var newDiv = document.createElement("div");
  var newText = document.createTextNode("I'm a generated DIV");
  newDiv.appendChild(newText);
  myElement.appendChild(newDiv);

  //Editing CSS

  //Add style directly
  myElement.style.backgroundColor = "green";

  //Working with forms

  //Grab a soecific field
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

  var myForm = document.getElementById("myForm");

  //Check if a checkbox is checked when 'submitting' form
  myForm.onsubmit = function () {
    var isChecked = document.getElementById("myCheckbox");
    if (isChecked) {
      alert("The checkbox is checked");
    } else {
      alert("The checkbox isn't checked");
    }
    return false; //Prevents the form from actually submitting
  };

  const button = document.getElementById("my-button");

  button.addEventListener("click", function () {
    alert("You clicked me!");
  });
}

domButton.onclick = dom;
