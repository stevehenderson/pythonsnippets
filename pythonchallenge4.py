#http://www.pythonchallenge.com/pc/def/ocr.html
import operator

#Number of occurance defining 'rare'
RARE=10

chars = {}
positions = {}
counter=0
with open("ocr.txt") as f:
  while True:
    c = f.read(1)
    counter=counter+1
    if not c:
      print "End of file"
      break
    #place in a hashmap
    if c in chars:
    	#print "adding!!!!!!!!"
    	chars[c]=chars[c]+1
    else:
    	chars[c]=1
    	positions[c]=counter
print "HISTOGRAM"
print "---------"
for c in chars:
	if chars[c] < RARE:
		print c,chars[c],": line ",positions[c]

sorted_chars = sorted(positions.items(), key=operator.itemgetter(1))


print "\nRARE CHARS IN FILE ORDER"
print "------------------------"

for c,v in sorted_chars:
	if chars[c] < RARE:
		print c,v