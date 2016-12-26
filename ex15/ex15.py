from sys import argv    #take in features from sys

script, filename = argv    #assign argv variables

txt = open(filename)	#get the filename and return the file handle

print "Here's your file %r:" %filename	#nothing fancy
print txt.read() 	#read is a function on file, read out file's content


print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
