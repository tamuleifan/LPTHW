from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C(^C)."
#Powershell can easily be terminated by the user 
#pressing ctrl-c
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()	#erase the file

print "Now I'm going to ask you for three lines."

i=1
line = ""
for i in range(1, 4):	#get 1 to 3
	prompt = "line %d: " %i
	line += raw_input(prompt) +'\n'
	i += 1

print "I'm goint to write these to the file."

target.write(line)

print "And finally, we close it."
target.close()