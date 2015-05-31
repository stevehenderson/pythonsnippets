def kitchen():
	print "Welcome to the kicthen!"
	print "What would you like to do next?"
	print "1=Go to the living room"
	print "2=Go to the grage"
	
	cmd = input("Enter you choice:")
	if(cmd)==2:
		garage()
	elif (cmd==1):
		livingroom()
	else:
		kitchen()

def garage():
	print "Welcome to the garage!"
	print "What would you like to do next?"
	print "1=Go to the kitchen"
	print "2=Get in the car"
	
	cmd = input("Enter you choice:")
	if (cmd==2):
		print "Varoooom!  That was fun."
		garage()
	elif (cmd==1):
		kitchen()
	else:
		print "invalid command!!"
		garage()


def livingroom():
	print "Welcome to the livingroom!"
	print "What would you like to do next?"
	print "1=Go to the kitchen"
	print "2=Watch TV"
	
	cmd = input("Enter you choice:")
	if (cmd==2):
		print "This is the VOICE!!..its over"
		livingroom()
	elif (cmd==1):
		kitchen()
	else:
		livingroom()

#start  in kitchen
kitchen()
