Person John = new Person()

John.setFirstName("John")
John.setLastName("Doe")
John.setAge(49)

// Create Closure that prints String representation of a person
Closure personToString = { Person person ->
    println person.toString()
}

// Create Closure that prints full name of a person
Closure personFullName = { Person person ->
    println person.firstName + " " + person.lastName
}

// Pass Closure to a method and execute it
handlePerson(personToString, johnDoe)
handlePerson(personFullName, johnDoe)
}

static void handlePerson(Closure c, Person p) {
if (p == null) {
    throw new RuntimeException("A person instance cannot be null")
}

c(p)
}