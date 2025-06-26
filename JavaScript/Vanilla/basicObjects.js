//Objects

function objects() {
  // Create an object
  let person1 = {};

  // Dot notation for setting attributes
  person1.name = "John Doe";

  // Create object with pre-defined attributes
  // Properties with non valid variable names use quotes
  let person2 = {
    firstName: "Jane",
    "last name": "Doe",
    // Objects can contain other objects
    address: {
      street: "123 main street",
      city: "your Town",
    },
  };

  console.log(person1.name);
  console.log(person2.firstName);
  console.log(person2["last name"]);

  // Object attributes can be other objects
  let people = {};
  people.person1 = person1;

  // Bracket notation
  people["person2"] = person2;

  console.log(people["person1"].name);
  console.log(people.person2.name);

  person1.name = "Jack Doe"; // Update attribute
  console.log(person1.name); // Jack Doe
  console.log(people.person1.name); // Jack Doe
  console.log("name" in person1); // True
  console.log("age" in person1); // False
  delete person1.name; // Remove attribute
  console.log("name" in person1); // False
  console.log(Object.keys(person2)); // ['firstName', 'last name', 'address']
  console.log(Object.keys(people)); // ['person1', 'person2']
  console.log(Object.values(people)); // [ { name: 'Jack Doe' }, { firstName: 'Jane', 'last name': 'Doe', address: { street: '123 main street', city: 'your Town' } } ]
  console.log(Object.values(person2)); // [ 'Jane', 'Doe', { street: '123 main street', city: 'your Town' } ]
  console.log(Object.entries(person2)); // [ [ 'firstName', 'Jane' ], [ 'last name', 'Doe' ], [ 'address', { street: '123 main street', city: 'your Town' } ] ]
  console.log(people.person2.address); // { street: '123 main street', city: 'your Town' }

  // When creating an object with a constructor
  let phonebookEntry = new Object();

  phonebookEntry.name = "Jack Huston";
  phonebookEntry.number = "860-555-1212";

  // Define a method on the object
  phonebookEntry.phone = function () {
    console.log("Calling " + this.name + " at " + this.number + "...");
  };

  // Call a method
  phonebookEntry.phone();

  // Methods
  let bob = new Object();
  bob.setAge = function (age) {
    // Object specific method
    bob.age = age;
  };
  bob.setAge(20);

  console.log(bob.age);

  function setWeight(weight) {
    this.weight = weight;
  }

  // Assign generic function as an object method
  bob.setWeight = setWeight;
  bob.setWeight(150);

  console.log(bob.weight);

  // Object equality
  let object1 = {
    val: 10,
  };
  let object2 = object1;
  let object3 = {
    val: 10,
  };
  console.log(object1 == object2); // True
  console.log(object1 == object3); // False
  object1.val = 15;
  console.log(object2.val); // 15

  // Bracket notation can use variables
  let population = {};

  function addPop(city, pop) {
    population[city] = pop;
  }
  addPop("New York", "Eleventymillion");
  console.log(population["New York"]);

  addPop("Chicago", "Seventeen Thousand");
  addPop("Seattle", 12);

  // Object for loop
  for (let city in population) {
    console.log(city + " : " + population[city]);
  }

  // Getters and setters. Looks like normal attributes but actually methods. Encapsulation.
  let somePerson = {
    mySex: "Male",
    myAge: 25,
    get age() {
      return this.myAge;
    },
    set age(newAge) {
      this.myAge = newAge;
    },
  };
  console.log(somePerson.age);
  somePerson.age = 30;
  console.log(somePerson.age);

  // Add getter or setter to existing object
  Object.defineProperty(somePerson, "sex", {
    get: function () {
      return this.mySex;
    },
    set: function (newSex) {
      this.mySex = newSex;
    },
  });
  console.log(somePerson.sex);
  somePerson.sex = "transgender";
  console.log(somePerson.sex);
}

objects();
