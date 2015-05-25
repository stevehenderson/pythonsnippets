#pythonchallenge2
#
#Unscramble a string:
#see:  	http://www.pythonchallenge.com/pc/def/map.html

from string import maketrans

theString ="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
theurl = "map"
intab="abcdefghijklmnopqrstuvwxyz"
outtab="cdefghijklmnopqrstuvwxyzab"
trantab=maketrans(intab,outtab)
print(theString.translate(trantab))
print(theurl.translate(trantab) + ".html")

