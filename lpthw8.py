formatter = "%r %r %r %r"


for i in range(1,10):
	print formatter % (1,2,3,4)
	print formatter % ("one", "two", "three", "four")
	print formatter % (True, False, False, True)
	print formatter % (formatter, formatter, formatter, formatter)
	print formatter % (
		"I had this thing.",
		"That you could type up right.",
		"But it din't sing",
		"So I said goodnight."
	)
	print"\n\n"
