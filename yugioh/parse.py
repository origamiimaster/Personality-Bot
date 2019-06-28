import re

file = open('./ep1.txt', "r",encoding = "ISO-8859-1")
script = file.read()
file.close()
file = open('./ep2.txt', "r",encoding = "ISO-8859-1")
script += file.read()
file.close()
file = open('./ep3.txt', "r",encoding = "ISO-8859-1")
script += file.read()
file.close()

scriptnolines = script.splitlines()

scriptnoblanks = []
for line in scriptnolines:
	line = re.sub(r'\[[^)]*\]', '', line)
	if not line == "": 
		if not line == None:
			if not line == " ":
				scriptnoblanks.append(str(line))

Yuugi = ""

for line in scriptnoblanks:
	#print(line[:5])
	if line[:5] == "Yuugi":
		Yuugi += line [6:]


#print(Yuugi)
file = open('./yuugi.txt',"w+")
file.write(Yuugi)
file.close()



Yami = ""
for line in scriptnoblanks:
	if line[:4] == "Yami":
		Yami += line [5:]
#print(Yami)
file = open('./yami.txt',"w+")
file.write(Yami)
file.close()

Joey = ""
for line in scriptnoblanks:
	if line[:4] == "Joey":
		Joey += line [5:]
#print(Joey)
file = open('./joey.txt',"w+")
file.write(Joey)
file.close()

Seto = ""
for line in scriptnoblanks:
	if line[:4] == "Seto":
		Seto += line [5:]
#print(Seto)
file = open('./seto.txt',"w+")
file.write(Seto)
file.close()