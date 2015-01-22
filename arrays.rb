#arrays.rb - Demonstration of basic array syntax

names = ['Bob', 'Dick', 'Harry']
puts names
puts
puts names[0]
puts

names.each do |name|
  puts 'Hi ' +name
end
puts

favorites = []
favorites.push 'Apples'
favorites.push 'Oranges'
puts favorites[0]
puts favorites.last
puts favorites.length
puts favorites.pop
puts favorites
puts favorites.length
puts

puts [1, 2, 3, 4, 5].map { |i| i + 1 }
puts

puts [1, 2, 3, 4, 5, 6].select {|number| number % 2 == 0}
puts

puts [1,2,3,4,5,6,7].delete_if{|i| i < 4 }