#flowcontrol.rb  - Demonstration of loop and if/then syntax

puts 1 < 2
puts 2 < 1
puts 1 == 1
puts 1 != 2

puts 'cats' < 'dogs'
puts

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
puts

i = 0
while i < 10
    puts i
    i = i + 1
end
puts

5.times do |x|
    puts x
end
puts

array = [1, 2, 3, 4, 5]

for i in array
  puts i
end
puts

array.each do |i|
  puts i
end