//Advanced Objects and prototypical inheritance

function objects() {
  //Basic object
  var object = {
    prop1: 1,
    method1: function () {
      return prop1;
    }
  }

  console.log(object1.method1());

  //Basic inheritance
  var object2 = Object.create(object1);
  object.prop1 = 2;
  console.log(object1.method1());


  //Constructor
  function Person(n) {
    this.name = n;
    var private = "This is private"
    //Can declare functions within constructor, but this is not recommended, unless you need access to a private variable
    this.speak = function () {
      console.log("Speak");
    }

    //This function wouldn't work as a prototype method because it wouldn't have access to 'private'
    this.sayPrivate = function() {
      console.log(private);
    }
  }

  //Set a constructor's prototype and add a method to it. Recommended way of adding methods.
  Person.prototype = {
      constructor: Person,
      sayName: function () {
        console.log(this.name);
      }
    }
  Person.prototype.repeat = function(toRepeat) {
    console.log(toRepeat);
  }

  var bob = new Person("Bob");
  bob.speak();
  bob.sayName();
  bob.repeat("hello");
  bob.repeat("hello");
  bob.sayPrivate();
  console.log(Object.getPrototypeOf(bob));
  console.log(bob instanceof Person);
  console.log(bob.constructor);

  //All Objects come from inherited prototypes
  console.log(Object.getPrototypeOf({}) == Object.prototype); //True
  console.log(Object.getPrototypeOf(isNaN) == Function.prototype); //True
  console.log(Object.getPrototypeOf([]) == Array.prototype); //True

  console.log(bob.toString()); //Inherited toString function from base Object prototype
  bob.toString = function () {
    return this.name;
  }
  console.log(bob.toString()); //Call overridden toString method


  //Create directly from prototype, no constructor
  var playerPrototype = {
    speak: function () {
      console.log("Speak");
    }
  }
  var george = Object.create(playerPrototype);
  bob.speak();
  george.speak();
  console.log(bob.hasOwnProperty('speak')); //True. Has this function from the constructor
  console.log(george.hasOwnProperty('speak')); //False. George doesn't have this function, it's prototype does

  //Inheritance
  function Employee(n, s) {
    Person.call(n);
    this.status = s;
  }



}
