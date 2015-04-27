#arrays.rb - Demonstration of basic array/range syntax

names = ['Bob', 'Dick', 'Harry']
puts names
puts
puts names[0]
puts
puts names.inspect
puts
puts names.join(",")
puts
puts names.include?('Bob')

gets

names.each do |name|
  puts 'Hi ' +name
end
puts

names.clear

puts names

gets

favorites = []
favorites.push 'Apples'
favorites << 'Oranges'
favorites.push 'Grapes'
puts favorites[0]
puts favorites.last
puts favorites.length
gets
puts favorites.pop
puts favorites.inspect
puts favorites.length
puts favorites.shift
favorites.unshift('Plums')
puts favorites.inspect

gets

x = "1,2,3,4,5"
y = x.split(",")
puts y.inspect
puts y.reverse.inspect

gets

puts [1, 2, 3, 4, 5].map { |i| i + 1 } #Add 1 to each value
puts

puts [1, 2, 3, 4, 5, 6].select {|number| number % 2 == 0}
puts

puts [1,2,3,4,5,6,7].delete_if{|i| i < 4 }
puts

array = [[1,2,3],[4,5,6]]
puts array[0].inspect
puts array[1][1]

gets

array = [3,1,5,7,6,4,2]
array.sort!
puts array.inspect
array.delete_at(2)
puts array.inspect
array.delete(7)
puts array.inspect

gets

inclusiveRange = 1..10  #1 through 10
puts inclusiveRange.inspect
puts inclusiveRange.end  #10
puts
exclusiveRange = 1...10 #1 through 9
puts exclusiveRange.inspect
puts exclusiveRange.end  #Also 10

array = [*inclusiveRange]
puts array.inspect

gets
 
puts inclusiveRange.find {|i| i%3==0 } #Find the first instance where boolean is true
puts (1..10).find {|i| i%3==0 } #Find the first instance where boolean is true
puts (1..10).detect {|i| i%3==0 } #Find the first instance where boolean is true

puts

puts (1..10).find_all {|i| i % 3==0 } #Find all instances where boolean is true
puts (1..10).select {|i| i % 3==0 } #Find all instances where boolean is true

puts

puts (1..10).any? {|i| i % 3==0 } #Are there any instances where this is true?
puts (1..10).all? {|i| i % 3==0 } #Are all instances true?

