#strings.rb  - Based on Learn To Program, 2nd Ed.

puts 1 < 2
puts 2 < 1
puts 1 == 1
puts 1 != 2

puts 'cats' < 'dogs'

puts 'Type a number'
x = gets.chomp
x = x.to_i



if x > 100
    puts 'Big number'
elsif x > 10
    puts 'Medium number'
else
    puts 'Small number'
end

i = 0
while i < 10
    puts i
    i = i + 1
end

5.times do |x|
    puts x
end