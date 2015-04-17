#flowcontrol.rb  - Demonstration of conditionals, loops and if/then syntax

puts 1 < 2
puts 2 < 1
puts 1 == 1
puts 1 != 2

puts 'cats' < 'dogs'
puts

puts 'Type a number'
x = gets.chomp
x = x.to_i

puts

if x > 100
    puts 'Big number'
elsif x > 10
    puts 'Medium number'
else
    puts 'Small number'
end

puts

puts "Shorthand" if true


i = 0
while i < 5 do
    puts "i " + i.to_s
    i = i + 1
end

puts

5.times do |y|
    puts "y " + y.to_s
end

puts

x = 0
until x > 5 do
  puts "x " + x.to_s
  x = x+1
end

puts

array = [1, 2, 3, 4, 5]

for i in array
  puts "array["+i.to_s+"] " + i.to_s
end

puts

array.each do |i|
  puts "array["+i.to_s+"] " + i.to_s
end
