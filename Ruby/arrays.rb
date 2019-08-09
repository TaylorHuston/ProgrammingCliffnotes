#arrays.rb - Demonstration of basic array/range syntax

names = ['Bob', 'Dick', 'Harry']
puts names #Lists each value on it's own line
puts
puts names[0] #Bob
puts
puts names.inspect #['Bob', 'Dick', 'Harry']
puts
puts names.join(",") #Bob,Dick,Harry
puts
puts names.include?('Bob') #True

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
puts favorites[0] #Apples
puts favorites.last #Grapes
puts favorites.length #3
gets
puts favorites.pop
puts favorites.inspect #["apples", "Oranges"]
puts favorites.length #2
puts favorites.shift #Apples
favorites.unshift('Plums')
puts favorites.inspect #["Plums", "Oranges"]

gets

x = "1,2,3,4,5"
y = x.split(",")
puts y.inspect #[1, 2, 3, 4, 5]
puts y.reverse.inspect

gets

puts [1, 2, 3, 4, 5].map { |i| i + 1 } #Add 1 to each value
puts

puts [1, 2, 3, 4, 5].collect { |i| i + 1 } #Same as map
puts

puts [1, 2, 3, 4, 5, 6].select {|number| number % 2 == 0} #Print even numbers
puts

puts [1, 2, 3, 4, 5, 6].reject {|number| number < 4} #4,5,6 (doesn't change array)
puts

puts [1, 2, 3, 4, 5, 6].delete_if{|i| i < 4 } #4,5,6 (values are actually removed)
puts

array = [[1,2,3],[4,5,6]]
puts array[0].inspect
puts array[1][1]

gets

array = [3,1,5,7,6,4,2]
array.sort!
puts array.inspect #[1, 2, 3, 4, 5, 6, 7]
array.delete_at(2)
puts array.inspect #[1, 2, 4, 5, 6, 7]
array.delete(7)
puts array.inspect #[1, 2, 4, 5, 6]

gets

favorites.push 'Bannanas'
favorites.push 'Grapefruit'
favorites.push 'Tangerine'
puts favorites.inspect #["Plums", "Oranges", "Bannanas", "Grapefruit", "Tangerine"]
puts favorites.sort.inspect #["Bannanas", "Grapefruit", "Oranges", "Plums", "Tangerine"]
puts favorites.sort_by {|fruit| fruit.length }.inspect #["Plums", "Oranges", "Bannanas", "Tangerine", "Grapefruit"]

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
puts (1..10).reject {|i| i.even? } #Find all instances where boolean is false

puts

puts (1..10).any? {|i| i % 3==0 } #Are there any instances where this is true?
puts (1..10).all? {|i| i % 3==0 } #Are all instances true?

puts (1..10).inject(100) {|memo, n| memo +n }.inspect #Set memo to 100, add everything in range into it

puts

array = [3,1,5,7,6,4,2]
array.sort! { |x, y| y <=> x } #Fancy way of sorting in reverse order
puts array.inspect
