#More variables and printing

my_name = "Zed A. Shaw"
my_age = 35
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

inches_to_cm = 2.54
pounds_to_kg = 0.453592

print "Let's talk about %s." % my_name
print "He's %d inches tall wich is %d cm." % (my_height,my_height*inches_to_cm)
print "He's %d pounds heavy which is %d kg." % (my_weight, my_weight*pounds_to_kg)
print "Actually thats not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#This line is tricky..
print "If I add %d, %d, amd %d I get %d." % (
   my_age, my_height, my_weight, my_age + my_height+my_weight)

