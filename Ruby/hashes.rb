#hashes.rb - Demonstration of basic hash syntax

student_ages = {
    :Jack => 10,
    :Jill => 12,
    :Bob => 14
  }

puts student_ages.keys
puts student_ages.values
puts
puts student_ages["Jack"]
student_ages["Tom"] = 13
puts student_ages["Tom"]

puts student_ages.to_a.inspect

puts

#Iterate over the hash
student_ages.each do |name, age|
    puts "#{name} is  #{age} years old"
end

puts


h1 = {"a" => 111, "b" =>222 }
h2 = {"b" => 333, "c" =>444 }

#Merge the two hashes, using the lowest value for any conflicts
h1.merge!(h2) do |key, old, new|
  if old < new
    old
  else
    new
  end
end

puts h1

puts h1.map { |k, v| "#{k}: #{v *20}" }.inspect

puts "Type in a string"
text = gets.chomp

words = text.split(" ")

frequencies = Hash.new(0)

#Count the frequency of each word
words.each do |word|
    frequencies[word] +=1
end

#Sort by the frequency of each word
frequencies = frequencies.sort_by do |count|
    count
end
