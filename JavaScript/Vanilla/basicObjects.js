//Objects

function objects() {
  //Create an object
  var person1 = {};

  //Dot notation for setting attributes
  person1.name = "John Doe";

  //Create object with pre-defined attributes
  //Properties with non cvalid variable names use quotes
  var person2 = {
    firstName: "Jane",
    "last name": "Doe"

    //Objects can contain other objects
    address: {
      street: '123 main street'
      city: 'your Town'
    }
  };

  console.log(person1.name);
  console.log(person2.firstName);
  console.log(person2["last name"]);

  //Object attributes can be other objects
  var people = {};
  people.person1 = person1;

  //Bracket notation
  people["person2"] = person2;

  console.log(people["person1"].name);
  console.log(people.person2.name);

  person1.name = "Jack Doe";
  console.log(person1.name);
  console.log(people.person1.name);

  //When creating an object with a constructor
  var phonebookEntry = new Object();

  phonebookEntry.name = 'Taylor Huston';
  phonebookEntry.number = '(503) 962-9521';

  //Define a method on the object
  phonebookEntry.phone = function () {
    console.log('Calling ' + this.name + ' at ' + this.number + '...');
  };

  //Call a method
  phonebookEntry.phone();

  //Methods
  bob = new Object();
  bob.setAge = function (age) { //Object specific method
    bob.age = age;
  }
  bob.setAge(20);

  console.log(bob.age);

  function setWeight(weight) {
    this.weight = weight;
  };

  //Assign generic functon as an object method
  bob.setWeight = setWeight;
  bob.setWeight(150);

  console.log(bob.weight);

  //Object equality
  var object1 = {
    val: 10
  };
  var object2 = object1;
  var object3 = {
    val: 10
  };
  console.log(object1 == object2); //True
  console.log(object1 == object3); //false
  object1.val = 15;
  console.log(object2.val); //15

  //Bracket notation can use variables
  var population = {}

  function addPop(city, pop) {
    population[city] = pop;
  }
  addPop("New York", "Eleventymillion");
  console.log(population["New York"]);

  addPop("Chicago", "Seventeen Thousand");
  addPop("Seattle", 12);

  //Object for loop
  for (var city in population) {
    console.log(city + " : " + population[city]);
  }

  //Getters and setters. Looks like normal attributes but actually methods. Encapsulation.
  var somePerson = {
    mySex: Male,
    myAge: 25,
    get age() {
      return this.myAge;
    },
    set age(newAge) {
      this.myAge = newAge;
    }
  };
  console.log(somePerson.age);
  somePerson.age = 30;
  console.log(somePerson.age);

  //Add getter or setter to existing object
  Object.defineProperty(somePerson, "sex", {
    get: function () {
      return this.mySex
    },
    set: function (newSex) {
      this.mySex = newSex;
    }
  });
  console.log(somePerson.sex);
  somePerson.sex = "transgender";
  console.log(somePerson.sex);


}

objects();
