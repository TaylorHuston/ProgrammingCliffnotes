#classes.rb - Demonstrate basic class syntax

class Rectangle
  def initialize(length, breadth) #Constructor?
    @length = length
    @breadth = breadth
  end

  def perimeter
    return 2 * (@length + @breadth)
  end

  def area
    return @length * @breadth
  end
end

small_square = Rectangle.new(10,10)
puts small_square.perimeter.to_s #40
puts small_square.area.to_s #100


def add(*numbers) #Can accept any number of numbers
  numbers.inject(0) { |sum, number| sum + number }
end

def add_with_message(message, *numbers)
  "#{message} : #{add(*numbers)}"
end

puts add_with_message("The Sum is", 1, 2, 3)