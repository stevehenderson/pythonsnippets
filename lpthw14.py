from sys import argv

script, username = argv

prompt = '>'

print "Hi %s, I'm the %s script."  % (username, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % username
likes = raw_input(prompt)

print "Where do you live?"
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright so you said %r about liking me.
You live in %r..not sure where that is!
And you own a %r computer...sweet!
"""% (likes,lives,computer)



