$(document).ready(function () { //Function is an even handler that happens when the document is ready

  //Can select with elemeny type, class, or id.  Essentially same as using CSS selectors.
  $("h1");
  $(".myClass");
  $("#myId");


  $('h1').text("This header was changed by jQuery");

  //You can also find elements by traversing
  $("#myList").find("li"); //Essentially same as $("myList li");
  $("#myList").children("li"); //Essentially same as $("myList > li");
  $("#myList").find("li").first().next(); //Second list item
  $("#myList").find("li").first().parent(); //The myList UL
  $("#myList").closest(".text"); //First ancestor with that class

  $(".class1").filter(".class2"); //Everything with class1 AND class2

  //Launch external JS functions
  $('#variabbles').on('click', function () {
    inputOutput();
  });
  $('#inputoutput').on('click', function () {
    inputOutput();
  });
  $('#flowcontrol').on('click', function () {
    inputOutput();
  });
  $('#inputoutput').on('click', function () {
    inputOutput();
  });
  $('#inputoutput').on('click', function () {
    inputOutput();
  });

  //Add content
  $("#mainParagraph").before('Before '); //Before siblng
  $("#mainParagraph").after('After '); //After sibling
  $("#mainParagraph").prepend('Prepend '); //First child
  $("#mainParagraph").append('Append '); //Last child


  $('#clickToShow').on('click', function () {
    $('#slideout').slideToggle();
    $('#fadein').fadeToggle();
  });
  //There are lots of other mouse events like mouseEnter and mouseLeave
  //There are keyboard events like keydown and keyup

  var price = +$(this).data('price'); //Get the string from the data-price tag and convert it to a number
  var quantity = +$(this).val(); //Value from a field

  $(this).css({
    '<attr>': '<value>'
  }); //Add a CSS rule

  $(this).toggleClass('<class>'); //Add/remove a CSS class

  $(this).animate({
    '<direction>': ,
    '<amount>'
  }, < speed > );

});
