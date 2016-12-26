from sys import argv

script, user_name, age = argv
prompt1 = '----'
prompt2 = '>'

print "Hi, %s. I am %s and will ask you a few questions." %(user_name, script)
print "How is it going %s ?" %(user_name)
how_r_u = raw_input(prompt1+prompt2)
print "Where do you live %s ?" %(user_name)
lives = raw_input(prompt1+prompt2)
print "What kind of computer do you have?"
computer = raw_input(prompt1+prompt2)

print """
All right. So you said you are %r 
And you are %r years old.
And you live in %r.
And you have a %r computer
""" %(how_r_u, age, lives, computer)