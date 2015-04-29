#classes.rb - Demonstrate basic class syntax

class Rectangle
  attr_accessor :length, :breadth #Getter and Setter shorthand
  
  
  @@total = 0  #Class variable
  def initialize(length, breadth) #Constructor
    @length = length  #Instance variable
    @breadth = breadth
    @@total += 1
  end

  def perimeter
    return 2 * (@length + @breadth)
  end

  def area
    @length * @breadth  #Return statement optional
  end
  
  #Reader method for class variable
  def self.total
    @@total
  end

end

small_rect = Rectangle.new(10,15)
puts small_rect.perimeter.to_s #50
puts small_rect.area.to_s #150

small_rect.length = 100
small_rect.breadth = 100
puts small_rect.perimeter #400

#Inheritance
class Square < Rectangle
  
 def initialize(length)
   @length = length
   @breadth = length
   @@total += 1
 end

  
end

perfect_square = Square.new(20)
puts perfect_square.perimeter #80

puts Rectangle.total #2

#Class with a static method
class MyClass

  def self.cls_method
    return "Static Method"
  end

end

puts MyClass.cls_method
