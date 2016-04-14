//Basic string functions

function strings() {
  var s = "Supercalifragilisticexpealadocious";
  console.log(s);
  console.log(s.length); //34

  var formatted = "Quoth the raven:\n\t\"Nevermore!\"";
  console.log(formatted);

  //String have a variety of self-explanatory methods
  var alpha = "abcdefghijklmnopqrstuvwxyz"
  console.log(alpha.length); //26
  console.log(alpha.indexOf("efg")); //First occurence, 4
  console.log(alpha.indexOf("DDDD")); //Returns -1
  console.log(alpha.charAt(11)); //l
  console.log(alpha.toUpperCase());
  console.log(alpha.slice(12, 18)); //Between position from 12 to 17 (doesn't include 18)
  console.log(alpha.replace("lmnop", "ponml"));

  var phrase = "This is a phrase";
  var words = phrase.split(" "); //Splits at a space into an array
  console.log(words);

  //Comparison is case-sensitive
  var str1 = "aardvark";
  var str2 = "beluga";
  var str3 = "Beluga";

  console.log(str1 < str2); //True
  console.log(str1 < str3); //False

  //Can force convert to string
  var number = 7;
  var myString = String(number);
  myString = "0" + myString;
  console.log(myString);
}

strings();

