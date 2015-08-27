//Basic string functions

var s = "Supercalifragilisticexpealadocious";
console.log(s);
console.log(s.length);

var formatted = "Quoth the raven:\n\t\"Nevermore!\"";
console.log(formatted);

//String have a variety of self-explanatory methods
var alpha = "abcdefghijklmnopqrstuvwxyz"
console.log(alpha.indexOf("e")); //First occurence
console.log(alpha.indexOf("DDDD")); //Returns -1
console.log(alpha.charAt(11)); //l
console.log(alpha.toUpperCase());
console.log(alpha.slice(12, 18)); //Between position from 12 to 17 (doesn't include 18)
console.log(alpha.replace("lmnop", "ponml"));

var phrase = "This is a phrase";
var words = phrase.split(" "); //Splits at a space
console.log(words);

//Comparison is case-sensitive
var str1 = "aardvark";
var str2 = "beluga";
var str3 = "Beluga";

console.log(str1 < str2); //True
console.log(str1 < str3); //False
