# Learning Python the Hard Way L15
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again bro:"
file_again = raw_input("> ")

txt_again = open(file_again)

print "Here's the second file %r:" % file_again
print txt_again.read()




