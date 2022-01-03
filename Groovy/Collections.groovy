Person Bob = new Person(firstName: "Bob", lastName: "Smith", age: 75)
Person John = new Person(firstName: "John", lastName: "Doe", age: 45)
Person Sally = new Person(firstName: "Sally", lastName: "Hill", age: 30)

def allPersons = [Bob, John, Sally]

assert allPersons instanceof List //true
assert allPersons.size() == 3
assert allPersons[2] == Sally

allPersons.each {
    println it
}

allPersons.eachWithIndex { Person entry, int i ->
    println i + ": " + entry
}

allPersons.find {
    it.lastName == "Hill"
} == Sally