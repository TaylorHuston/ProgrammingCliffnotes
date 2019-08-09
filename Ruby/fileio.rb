#r - Read from start
#r+ - Read and write
#w - Write from start (wipes file)
#w+ Read and write from start (wipes file)
#a - Append to end
#a+ -Read from start, append to end

require 'FileUtils'

#Print this file name
puts __FILE__

#Print absolute path to this file
puts File.expand_path(__FILE__)

#Print the relative path to the file
puts File.dirname(__FILE__)

#Generate a theoretical filepath
puts File.join(File.dirname(__FILE__), "Temp\ Directory")

#Create a new file to write to
file = File.new('testfile.txt', 'w')

file.close

#Open or create new file and auto close
file = File.open('testfile2.txt', 'w') do |file|
  file.puts "abcd\nefghij\nklmn\nop\nqrstuv\nw\nxyz"
end

file = File.open('testfile2.txt', 'r') do |file|
  puts file.gets #Read line
  puts file.read(1) #Read 1 charactter
end

file = File.open('testfile2.txt', 'r') do |file|
  file.each_line do |line|
    puts line
  end
end

file = File.new('testfile2.txt', 'r+')

puts file.pos
puts file.read(3)
puts file.pos
file.pos = 1
puts file.read(1)
file.pos +=6
puts file.pos
puts file.read(6)

file.close


puts File.exist?('testfile.txt')

File.rename('testfile.txt', 'testfile3.txt')
FileUtils.copy('testfile2.txt', 'testfile4.txt')
File.delete('testfile3.txt')
File.delete('testfile2.txt')
File.delete('testfile4.txt')

puts Dir.pwd
Dir.chdir('..')
puts Dir.pwd
