#methodss.rb - Demonstration of some basic method syntax

def say_moo num
    puts 'Mooooo...'*num  #Prints num times
end

say_moo 3 #call say_moo with the argument 3

x = 1
def multiply x
    x = x*2  #local scope
    puts x  #2
    return x
end
y = multiply x
puts x  #1
puts y  #2


#Recursive method
def ask_recursively question
  puts question
  reply = gets.chomp.downcase
  if reply == 'yes'
    return true
  elsif reply == 'no'
    return false
  else
    puts 'Please answer "yes" or "no".'
    ask_recursively(question)
  end
end

puts ask_recursively "Does 1+1=2?"


#Pass hash to method
def add(*numbers)
  numbers.inject(0) { |sum, number| sum + number }  
end

def subtract(*numbers)
  current_result = numbers.shift
  numbers.inject(current_result) { |current_result, number| current_result - number }  
end

def calculate(*arguments)
  # if the last argument is a Hash, extract it 
  # otherwise create an empty Hash
  options = arguments[-1].is_a?(Hash) ? arguments.pop : {}
  options[:add] = true if options.empty?
  return add(*arguments) if options[:add]
  return subtract(*arguments) if options[:subtract]
end

puts calculate(4, 5, add: true)  #9
puts calculate(-10, 2, 3, add: true)  #-5
puts calculate(4, 5, subtract: true)  #-1
puts calculate(-10, 2, 3, subtract: true)  #-15 