#strings.rb  - Demonstration of basic string related syntax

puts 'Hello, world!'
puts
puts 'Good-bye.'

puts 'I like ' + 'apple pie.'

puts 'blink' * 4 #Print a sting multiple times

gets

puts 12 + 12
puts '12' + '12' #1212
puts '12 + 12'

puts 2 * 5
puts '2' * 5 #22222
puts '2 * 5'

puts 'You\'re swell!' #Escape a character

gets

letters = 'aAbBcCdDeE'
puts letters
puts letters.length
puts letters.upcase
puts letters.downcase
puts letters.swapcase
puts letters.capitalize
puts letters.reverse
puts ' a'.capitalize
puts letters
letters.reverse!
puts letters

gets

number = 4
name = "Taylor"

puts "The number #{number} is the same as " + number.to_s #String interpolation
puts "Hi " + name + " are you related to the other #{name} I know?"

puts "Hi Bob".include?("Bob")

gets

puts "Ruby is a beautiful language".start_with?("Ruby")
puts "I can't work with any other language but Ruby".end_with?("Ruby")
puts "I am a Rubyist".index("R")

gets

puts 'Fear is the path to the dark side'.split #split onto mutiple lines

gets

puts "I should look into your problem when I get time".gsub('I','We')
puts 'RubyMonk'.gsub(/[aeiou]/,'1')

puts `date`

gets

puts 'What is your name?'
name = gets.chomp #Remove trailing linebreak
puts 'Your name is ' + name + '?'
puts 'Pleased to meet you, ' + name + '!'


puts "Homer" =~ /er/  #Regexp, 3, index of first match
phone = "(907) 111-2233"
puts phone.gsub(/\D/, "") #Strip out any non-digits

gets

#You can grab strings for editing with %Q
cur_weather = %Q{It's a hot day outside. Grab your umbrellas...}

single_quoted = 'ice cream \n followed by it\'s a party!'
double_quoted = "ice cream \n followed by it\'s a party!"

puts single_quoted #ice cream \n followed by it's a party!
puts double_quoted #ice cream
                   #  followed by it's a party!

name[0] = "B" #Strings can use array notation
puts name
name[0] = "Yaaa"
puts name

puts name.class #String