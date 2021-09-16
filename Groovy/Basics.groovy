//Groovy can be used as a scripting language without needing to declare classes, here are some other key differences/enhancements between it and Java

println 'Groovy world!'

//Support static and dynamic binding
int x = 47
println(x) //47

def y = 12
println(y) //12

y = "Hello"
println(y) //Hello


//Supports enhanced loops, these both give the same output of 0 through 5
0.upto(4) {println "$it"}
5.times{println "$it"}

println()

//Even numbers less than 7
0.step(7,2){println "$it"}

println()

//No defined array type, but lists are supportd
def myList = ["A", 12, "Bannannanna"]
println(myList) //[A, 12, Bannannanna]
myList.add("Weee")
println(myList) //[A, 12, Bannannanna, Weee]
println(myList.contains("A")) //True
println(myList.isEmpty()) //False
println(myList.get(2)) //Bannannanna

def myList2 = [11,6,23,19,-4]
println(myList2) //[11,6,23,19,-4]
myList2.sort()
println(myList2) //[-4, 6, 11, 19, 23]
myList2.pop()
println(myList2) //[-4, 6, 11, 19]
myList2.remove(2)
println(myList2) //[-4, 6, 19]

String name = "Bob"
def name2 = "Sally"

println name.getClass()  //String
println name2.getClass()  //String


