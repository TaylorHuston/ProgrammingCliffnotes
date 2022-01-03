Person person = new Person()

person.setFirstName("John")
person.setLastName("Doe")
person.setAge(49)

try {
    person.getFirstName().toLong()
} catch (NumberFormatException e) {
    assert e instanceof NumberFormatException
    println "Cannot convert a String to a Long"
}