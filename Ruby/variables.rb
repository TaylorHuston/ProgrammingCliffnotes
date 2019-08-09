#strings.rb  - Demonstration of basic variable type and syntax

my_string = '...you can say that again...'
puts my_string

gets

name = "Taylor Alexander Huston"
puts 'My name is ' + name + '.' #String concatenation

gets

flexible_type = 'just another'  + ' string'
puts flexible_type
flexible_type = 5 * 12 #Variables are strictly typed
puts flexible_type

gets

var1 = 8
var2 = var1
puts var1 #8
puts var2 #8

puts

var1 = 'eight'
puts var1 #eight
puts var2 #8

gets

var1 = 2
var2 = '5'
puts var1.to_s + var2  #Convert var1 to a string
puts var1 + var2.to_i #Convert var2 to an integer

gets

puts '15'.to_f    #Convert to float
puts '99.999'.to_f    #Convert to float
puts '99.999'.to_i    #Convert to int

puts
puts '5 is a number'.to_i #Convert to interger (strip off any text)
puts 'Whatabout 6?'.to_i  #Can't convert, number not first character
puts 'I will fight you'.to_f  #Nothing to conver

gets

puts true.class
puts false.class

x = true
puts true.class
puts x
puts !x

puts

SOMECONSTANT = 100 #Naming convention for constants
SOMECONSTANT = 200 #Not a true constant since it will let you do this, but it will throw a warning
puts SOMECONSTANT

puts

#Symbols. Guaranteed to be unique and immutable
puts :string == "string" #false
puts :string == "string".to_sym #true
puts "string" == :string.to_s #true

puts

puts 'a'.class
puts 5.class
puts 3.2.class
puts :string.class
puts true.class
