// Array syntax

function arrays() {
  console.log("test");
  // Creating an array with the constructor to set initial size (though arrays in JS are dynamic anyway)
  let foo = new Array(100);

  // Creating an array with the array literal syntax
  let bar = [1, "a", 3.5, true, 2]; // Not type specific

  console.log(foo.length); // 100
  console.log(bar.length); // 5
  console.log(foo[0]); // Undefined
  foo[0] = "a";
  console.log(foo[0]); // a

  console.log(bar[0]); // 1

  // Push adds to end
  foo.push("z");
  console.log(foo[0]); // a
  console.log(foo.length); // 101
  console.log(foo[100]); // z

  // Pop removes from end
  console.log(foo.pop()); // z
  console.log(foo.length); // 100

  // Shift removes from front
  console.log(bar.shift()); // 1
  // Add to front
  bar.unshift("x");
  console.log(bar[0]); // x

  var fub = new Array();
  console.log(fub.length);

  fub[4] = 4;
  console.log(fub.length); // 5
  console.log(fub[0]); // undefined

  let rand = [1, 5, 3, 9, 8, 3];

  console.log(rand); // [1, 5, 3, 9, 8, 3]
  rand.reverse(); // Reverse the array in place
  console.log(rand); // [3, 8, 9, 5, 3, 1]
  rand.sort(); // Sorts the array in place, but sorts as strings by default
  console.log(rand); // [1, 3, 3, 5, 8, 9]
  // Slice returns a new array with elements from start to end (not including end)
  console.log(rand.slice(1, 4)); // [3, 3, 5]
  console.log(rand.slice(1)); // [3, 3, 5, 8, 9] - from index 1 to end
  console.log(rand.slice(-3)); // [5, 8, 9] - from the end
  console.log(rand.splice(1, 3)); // [3, 3, 5] - removes elements from index 1 to index 3 (not including index 3) and returns them
  console.log(rand); // [1, 8, 9] - original array modified
  rand.splice(1, 0, 2, 4); // Inserts 2 and 4 at index 1 without removing any elements
  console.log(rand); // [1, 2, 4, 8, 9] - original array modified

  let sum = 0;
  rand.forEach(function (someVal) {
    console.log(someVal);
    sum += someVal;
  });
  console.log(sum);

  // Use filter to exclude certain elements
  console.log(
    rand.filter(function (val) {
      return val % 2 == 0;
    })
  );

  // Use map to apply a function to each element of an array and build a NEW array from the results
  console.log(
    rand.map(function (val) {
      return val * 2;
    })
  );

  // Reduce returns a single value based on a function ran on each array element in order. Internal logic looks something like
  // function reduce(array, combine, start) {
  //   var current = start;
  //   for (var i = 0; i < array.length; i++)
  //     current = combine(current, array[i]);
  //   return current;
  // }

  // Use reduce to combine all elements
  console.log(
    rand.reduce(function (x, y) {
      return x + y;
    })
  );

  // Use reduce to find smallest element
  console.log(
    rand.reduce(function (x, y) {
      if (x < y) {
        return x;
      } else {
        return y;
      }
    })
  );

  // 2D array
  let twoD = [
    [1, 2],
    [3, 4],
  ];

  console.log(twoD[0][0]); // 1
  console.log(twoD[1][1]); // 4

  // Join converts array into string with a separator
  console.log(rand.join(" and ")); // 1 and 3 and 3 and 5 and 8 and 9
}

arrays();
