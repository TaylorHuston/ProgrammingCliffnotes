// Basic error handling

function sqrRoot(x) {
  try {
    if (x === "")
      throw {
        message: "Can't Square Root Nothing",
      };
    if (isNaN(x))
      throw {
        message: "Can't Square Root Strings",
      };
    if (x < 0)
      throw {
        message: "Sorry No Imagination",
      };
    return "sqrt(" + x + ") = " + Math.sqrt(x);
  } catch (err) {
    return err.message;
  }
}

function writeIt() {
  console.log(sqrRoot("four"));
  console.log(sqrRoot(""));
  console.log(sqrRoot("4"));
  console.log(sqrRoot("-4"));
}

writeIt();
