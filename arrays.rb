names = ['Bob', 'Dick', 'Harry']
puts names
puts
puts names[0]


names.each do |name|
  puts 'Hi ' +name
end



favorites = []
favorites.push 'Apples'
favorites.push 'Oranges'
puts favorites[0]
puts favorites.last
puts favorites.length
puts favorites.pop
puts favorites
puts favorites.length