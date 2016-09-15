#classes.rb - Demonstrate basic class syntax

class Rectangle
  attr_accessor :length, :breadth #Getter and Setter shorthand

  @@total = 0  #Class variable, shared across all instances of class

  #Static method
  def self.what_am_i?
    puts "I'm a rectangle"
  end

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

Rectangle.what_am_i? #I'm a rectangle

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
  
  #Override method
  def area
    @length * @length
  end

end

perfect_square = Square.new(20)
puts perfect_square.perimeter #80
puts perfect_square.area #400

puts Rectangle.total #2


#Class with coded setters and getters
class Car
  def initialize (make, model)
    @make = make
    @model = model
  end

  #Getters
  def make
    @make
  end

  def model
    @model
  end

  #Setter
  def model= (new_model)
    @model = new_model
  end
end

myCar = Car.new("Toyota", "Prius")
puts myCar.make #Toyota
puts myCar.model #Prius
myCar.model = "Camry"
puts myCar.model #Camry


#Class with a static method
class MyClass

  def self.cls_method
    return "Static Method"
  end

end

puts MyClass.cls_method #Static Method

#Add method to class outside of original definition
def MyClass.other_method
  return "Other Method"
end

puts MyClass.other_method #Other Method


#Module allows for namespacing
module ModuleOne
  class SomeClass
    def initialize
      puts "Module One"
    end
  end
end
  
module ModuleTwo
 class SomeClass
   def initialize
     puts "Module Two"
   end
 end
end
    
mod1 = ModuleOne::SomeClass.new
mod2 = ModuleTwo::SomeClass.new


#Modules allow for mixins (multple inheritance-ish)
module Names
  attr_accessor :firstname, :lastname
end

module Number
  attr_accessor :phonenumber
end

class Person
  include Names
  include Number
end

some_guy = Person.new
some_guy.firstname = "Bob"
some_guy.phonenumber = 1112223344
puts some_guy.firstname
puts some_guy.phonenumber


class ToDoList
  include Enumerable  #Include an official Ruby module
  attr_accessor :items
  
  #Including Enumerable requires you include a each method
  #Similar to say, a Java Interface
  def each
    @items.each do |item|
      yield item
    end
  end
end

my_list = ToDoList.new
my_list.items = ['laundry','dishes','vacuum']

#Possible since items is an array
my_list.items.select do |item|
  puts item
end

#Possible because we added each method
my_list.select do |item|
  puts item
end


#Extends is like include but for a class, not just instances of a class
module ToExtend
  def say
    puts "I am saying a thing"
  end
end

class ExtenderAma
  extend ToExtend
end

ExtenderAma.say
