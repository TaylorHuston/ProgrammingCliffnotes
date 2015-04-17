#calc.rb - Basic math operations

puts 1.0 + 2.0
puts 2.0 * 3.0
puts 5.0 - 8.0
puts 9.0 / 2.0

puts 1+2
puts 2*3
puts 5-8
puts 9/2

puts 5**2 #Exponent
puts 7%3 #Modulus
puts (2-5).abs #Absolute value

puts rand #Rand between 0 and 1
puts(rand(100)) #Rand between 0 and 99


def add(*numbers) #Can accept any number of numbers
  numbers.inject(0) {
      |sum, number| sum + number
    }
end

def add_with_message(message, *numbers)
  "#{message} : #{add(*numbers)}"
end

puts add_with_message("The Sum is", 1, 2, 3)
