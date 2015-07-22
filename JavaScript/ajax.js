//Basic AJAX example


var myRequest;

if (window.XMLHttpRequest) { //Most browesrs
  myRequest = new XMLHttpRequest();
} else if (window.ActiveXObject) { //Internet Exploder
  myRequest = new ActiveXObject("Microsoft.XMLHTTP");
}

myRequest.onreadystatechange = function () {
  console.log();
};

//THIS IS THE SAME CODE AS IN TUTORIAL BUT GIVING ERRORS, INVESTIGATING

//Open
myRequest.open('GET', 'simple.txt', true);
//Send with any params
myRequest.send(null);

//Doesn't wait for request to continue file
console.log("I'm still running");
