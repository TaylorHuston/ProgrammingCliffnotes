class HelloWorld {
    static void main(String[] args) {
        println "Hello World"

        Person person = new Person()

        person.setFirstName("John")
        person.setLastName("Doe")
        person.setAge(49)

        println person.toString()
    }
}