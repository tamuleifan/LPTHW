from sys import argv    #take in features from sys

script, filename_1, filename_2 = argv    #assign argv variables

txt_1 = open(filename_1)	#get the filename and return the file handle

print "Here's your file %r:" %filename_1	#nothing fancy
print txt_1.read() 	#read is a function on file, read out file's content

txt_1.close()

txt_2 = open(filename_2)	#get the filename and return the file handle

print "Here's your file %r:" %filename_2	#nothing fancy
print txt_2.readline() 
print txt_2.readlines()

txt_2.close()