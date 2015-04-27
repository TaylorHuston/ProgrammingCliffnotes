#flowcontrol.rb  - Demonstration of the different conditional statements in Ruby

puts 1 < 2  #True
puts 2 < 1  #False
puts 1 == 1 #True
puts 1 != 2  #True

puts 'cats' < 'dogs'
puts

puts 'Type a number'
x = gets.chomp
x = x.to_i  #Convert to integer

if x > 100
    puts 'Big number'
elsif x > 10  #Notice the spelling
    puts 'Medium number'
else
    puts 'Small number'
end

puts 'Type another 1, 2 or 3'
x = gets.chomp
x = x.to_i  #Convert to integer

case x  #Like a switch statement
  when 1
    puts 'One'
  when 2
    puts 'Two'
  when 3
    puts 'Three'
  else
    puts 'Cheater'
end

gets

puts true && true
puts true || false
puts true && false

gets

puts "Shorthand" if true #Shorthand if synatx

gets

x = 2
unless x == 1
  puts "x doesn't equal 1"
end

puts x == 2 ? "It is equal to 2" : "It is not equal to 2" #Shorthand comparison, first is reult if true, second is result if false

gets
