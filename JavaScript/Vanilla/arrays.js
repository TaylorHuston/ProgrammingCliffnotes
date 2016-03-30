//Array syntax
//var functionButton = document.getElementById("arrays");

function arrays() {
  console.log("test");
  // Creating an array with the constructor to set initial size (though arrays in JS are dynamic anyway)
  var foo = new Array(100);

  // Creating an array with the array literal syntax
  var bar = [1, "a", 3.5, true, 2]; //Not type specific

  console.log(foo.length); //100
  console.log(bar.length); //5
  console.log(foo[0]); //Undefined
  foo[0] = "a";
  console.log(foo[0]); //a

  console.log(bar[0]); //1

  //Push adds to end
  foo.push("z");
  console.log(foo[0]); //a
  console.log(foo.length); //101
  console.log(foo[100]); //z

  //Pop removes from end
  console.log(foo.pop()); //z
  console.log(foo.length); //100

  //Shift removes from front
  console.log(bar.shift()); //1
  //Add to front
  bar.unshift("x");
  console.log(bar[0]); //x

  var fub = new Array();
  console.log(fub.length);

  fub[4] = 4;
  console.log(fub.length); //5
  console.log(fub[0]); //undefined

  var rand = [1, 5, 3, 9, 8, 3];

  var reverse = rand.reverse();
  console.log(reverse);

  var sorted = rand.sort();
  console.log(sorted); //1,3,3,5,8,9

  //Use forEach to run a function on each element of an array
  var sum = 0;
  sorted.forEach(function (someVal) {
    console.log(someVal);
    sum += someVal;
  });
  console.log(sum);

  //Use filter to exclude certain elements
  console.log(sorted.filter(function (val) {
    return (val % 2 == 0);
  }));

  //Use map to apply a function to each element of an array and build a NEW array from the results
  console.log(sorted.map(function (val) {
    return (val * 2);
  }));

  //Reduce returns a single value based on a function ran on each array element in order. Internal logic looks something like
  //function reduce(array, combine, start) {
  //var current = start;
  //for (var i = 0; i < array.length; i++)
  //current = combine(current, array[i]);
  //return current;
  //}

  //Use reduce to combine all elements
  console.log(sorted.reduce(function (x, y) {
    return x + y;
  }));

  //Use reduce to find smallest element
  console.log(sorted.reduce(function (x, y) {
    if (x < y) {
      return x;
    } else {
      return y;
    }
  }));

  //2D array
  var twoD = [[1, 1], [1, 1]];

  //Join converts array into string with a separator
  console.log(rand.join(" and ")); //1 and 3 and 3 and 5 and 8 and 9


}

//functionButton.onclick = arrays;
arrays();
