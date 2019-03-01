//Timer related events in JS

function simpleMessage() {
  console.log("5 seconds have passed");
}

//Run once after 5 seconds
setTimeout(simpleMessage, 5000);

var myImage = document.getElementById("slideImage");
var images = ["_images/cat1.jpg", "_images/cat2.jpg", "_images/cat3.jpg"];
var slideIndex = 0;

function slideshow() {
  myImage.setAttribute("src", images[slideIndex]);
  slideIndex++;
  if (slideIndex >= images.length) {
    slideIndex = 0;
  }
}

//Run every 5 seconds
var myInterval = setInterval(slideshow, 5000);

//Stop the interval if user clicks on image
myImage.onclick = function () {
  clearInterval(myInterval);
}
