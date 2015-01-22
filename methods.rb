#methodss.rb - Demonstration of some basic method syntax

def say_moo number_to_say
    puts 'Mooooo...'*number_to_say
end

say_moo 3

x = 1
def multiply x
    x = x*2
    puts x
    return x
end
y = multiply x
puts x
puts y


def ask_recursively question
  puts question
  reply = gets.chomp.downcase
  if reply == 'yes'
    return true
  elsif reply == 'no'
    return false
  else
    puts 'Please answer "yes" or "no".'
    ask_recursively question  #  This is the magic line.
  end
end

puts ask_recursively "Does 1+1 = 2?"