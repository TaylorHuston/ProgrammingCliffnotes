#methodss.rb - Demonstration of some basic method syntax

def say_moo num  #Note methods don't need ()
    puts 'Mooooo...'*num  #Prints num times
end

say_moo 3 #call say_moo with the argument 3

x = 1
def multiply(x)  #Can use () for readability though
    x = x*2  #local scope
    puts x  #2
  x  #Last line is auto-returned, no need for an explicit Return statement
end
y = multiply x
puts x  #1
puts y  #2


#Recursive method
def ask_recursively(question)
  puts question
  reply = gets.chomp.downcase
  if reply == 'yes'
    return true  #Can use explicit Return if needed
  elsif reply == 'no'
    return false
  else
    puts 'Please answer "yes" or "no".'
    ask_recursively(question)
  end
end

puts ask_recursively("Does 1+1=2?")


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

Increment = lambda { |x|  return x+1 }  #lambda
puts Increment.call(7)  #8

puts

#Pass an acutal code block to a method
def three_times
  yield
  yield
  yield
end

three_times { puts "hi" } #Will print "hi" three times

def my_yield(param)
  yield("Bob")
  yield(param)
end

my_yield("Taylor") do |s|
  puts s
end


#Default parameters
def say_hi(name="Bob")
  puts "Hello #{name}"
end

say_hi("George")
say_hi

puts

#Procs aren't tehcnically methods, but serve the same purpose as blocks of re-usable code
cube = Proc.new { |x| x ** 3 }
puts [1, 2, 3].collect!(&cube)

#Pass a proc into a method
phrase = Proc.new do
    puts "Hello there!"
end

def greeter(&phrase)
    yield
end

greeter(&phrase)

#Call a proc directly
phrase.call


#Lambdas server a similar prupose as procs
strings = ["leonardo", "donatello", "raphael", "michaelangelo"]

symbolize = lambda { |x| x.to_sym }

symbols = strings.collect(&symbolize)

puts symbols.inspect
