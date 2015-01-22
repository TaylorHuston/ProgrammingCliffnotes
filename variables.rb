#strings.rb  - Demonstration of basic variable type and syntax

my_string = '...you can say that again...'
puts my_string

name = "Taylor Alexander Huston"
puts 'My name is ' + name + '.'

flexible_type = 'just another'  + ' string'
puts flexible_type
flexible_type = 5 * 12
puts flexible_type


var1 = 8
var2 = var1
puts var1
puts var2
puts ''
var1 = 'eight'
puts var1
puts var2

var1 = 2
var2 = '5'
puts var1.to_s + var2  #Convert var1 to a string
puts var1 + var2.to_i #Convert var2 to an integer

puts '15'.to_f
puts '99.999'.to_f
puts '99.999'.to_i
puts ''
puts '5 is a number'.to_i
puts 'Whatabout 6?'.to_i
puts 'I will fight you'.to_f
puts ''
puts 'string'.to_s
puts 3.to_i

puts gets

puts 'What is your name?'
name = gets.chomp #Remove trailing linebreak
puts 'Your name is ' + name + '?'
puts 'Pleased to meet you, ' + name + '!'