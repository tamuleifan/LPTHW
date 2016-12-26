from sys import argv

script, filename = argv

print "I will read the file %r." % filename
txt = open(filename)

print txt.read()
txt.close()