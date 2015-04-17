#strings.rb  - Demonstration of basic string related syntax

puts 'Hello, world!'
puts ''
puts 'Good-bye.'

puts 'I like ' + 'apple pie.'

puts 'blink' * 4

puts 12 + 12
puts '12' + '12'
puts '12 + 12'

puts 2 * 5
puts '2' * 5
puts '2 * 5'

puts 'You\'re swell!'

letters = 'aAbBcCdDeE'
puts letters.upcase
puts letters.downcase
puts letters.swapcase
puts letters.capitalize
puts letters.reverse
puts ' a'.capitalize
puts letters

number = 4
name = "Taylor"

puts "The number #{number} is the same as " + number.to_s
puts "Hi " + name + " are you related to the other #{name} I know?"

puts "Hi Bob".include?("Bob")


puts "Ruby is a beautiful language".start_with?("Ruby")
puts "I can't work with any other language but Ruby".end_with?("Ruby")
puts "I am a Rubyist".index("R")

puts 'Fear is the path to the dark side'.split

puts "I should look into your problem when I get time".gsub('I','We')
puts 'RubyMonk'.gsub(/[aeiou]/,'1')

puts `date`


puts 'What is your name?'
name = gets.chomp #Remove trailing linebreak
puts 'Your name is ' + name + '?'
puts 'Pleased to meet you, ' + name + '!'


puts "Homer" =~ /er/  #Regexp
phone = "(907) 111-2233"
puts phone.gsup(/\D/, "") #Strip out any non-digits
