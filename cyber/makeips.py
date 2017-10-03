#Simple porgram t create a random set of ips given
#a desired count on the command line
#
# usage:  python makeip.py 4
#
# (Creates 4 ips addresses)
#
from sys import argv


ip_counts= int(argv[1])

#
#Make the ips using a series
#
def series():
	a=1
	b=1
	c=1
	d=1
	i=0
	while(i<ip_counts):
		print "{0}.{1}.{2}.{3}".format(a,b,c,d)
		d=d+1
		if(d>255):
			d=0
			c=c+1
			if(c>255):
				c=0
				b=b+1
				if(b>255):
					b=0
					a=a+1
					if(a>255):
						print "exceeded block address..exiting"
						i=ip_counts
		i=i+1


#
#Generate the set of ips using random number generator
#
def randomips():
	i=0


series()
