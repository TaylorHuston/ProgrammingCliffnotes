//Date object syntax

var today = new Date(); //Current date and time

console.log(today);

var y2k = new Date(2000, 0, 1); //Months are 0-index

//Dates have a rang of self-explanatory methods
console.log(y2k.getMonth());
console.log(y2k.getDate()); //Day of month (1-31)
console.log(y2k.getDay()); //Day of week (0-6)
console.log(y2k.getTime()); //Milliseconds since 1/1/1970

today.setMonth(5);
console.log(today);

var date1 = new Date(2000, 0, 1);
var date2 = new Date(2000, 0, 1);

console.log(date1 == date2) //False, two different objects
console.log(date1.getTime() == date2.getTime()) //True
