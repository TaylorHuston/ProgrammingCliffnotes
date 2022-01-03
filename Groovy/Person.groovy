//Groovyy convenience annotations
import groovy.transform.Canonical

@Canonical
class Person implements Serializable {
    String firstName
    String lastName
    int age
}
