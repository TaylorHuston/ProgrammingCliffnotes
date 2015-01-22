#hashes.rb - Demonstration of basic hash syntax

student_ages = {
    "Jack" => 10,
    "Jill" => 12,
    "Bob" => 14
  }

puts student_ages.keys
puts student_ages.values
puts
puts student_ages["Jack"]
student_ages["Tom"] = 13
puts student_ages["Tom"]

student_ages.each do |name, age|
    puts "#{name} is  #{age}'s old"
end