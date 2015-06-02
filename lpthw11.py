print "How old are you?",
age=raw_input()
print "How tall are you?",
height=raw_input()
print "How much do you weigh?",
weight=raw_input()

#https://docs.python.org/2/library/stdtypes.html for old string types r vs s?
print "So, you are %r old, %r tall, and %s heavy." % (age, height, weight)