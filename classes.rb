#classes.rb - Demonstrate basic class syntax

class Rectangle
  attr_accessor :length, :breadth #Getter and Setter shorthand
  
  def initialize(length, breadth) #Constructor
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

small_square.length = 100
small_square.breadth = 100
puts small_square.perimeter #400

#Inheritance
class Square < Rectangle
 def initialize(length)
   @length = length
   @breadth = length
 end
end

perfect_square = Square.new(20)
puts perfect_square.perimeter

#Class with a static method
class MyClass
  def self.cls_method
    return "Static Method"
  end
end

puts MyClass.cls_method
