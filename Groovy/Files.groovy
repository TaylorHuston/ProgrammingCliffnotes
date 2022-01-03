Person johnDoe = new Person()
File file =  new File("john-doe.txt")

println file.getText('UTF-8')

file.eachLine { line, no ->
    if (no == 1) {
        johnDoe.setFirstName(line)
    } else if (no == 2) {
        johnDoe.setLastName(line)
    } else {
        johnDoe.setAge(line.toInteger())
    }
}

// Create a file and populate contents
File textFile = new File("mary-hill.txt")
textFile.withWriter('UTF-8') { writer ->
    writer.writeLine("Mary")
    writer.writeLine("Hill")
    writer.writeLine("30")
}

// Appending contents to a file
textFile.append("1")
textFile << "2"

// Serializing an object to a file
Person thomasMarks = new Person("Thomas", "Marks", 21)
File binFile = new File("thomas-marks.bin")

binFile.withObjectOutputStream { out ->
    out.writeObject(thomasMarks)
}