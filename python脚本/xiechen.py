def grep(pattern):
	print("Searching for", pattern)
	while True:
		line=(yield)
		if pattern in line:
			print(line)

sc=grep("you")
next(sc)
sc.send("i love you")
sc.send('fuck you')

sc.close()
