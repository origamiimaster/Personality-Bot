import re

file = open('./ep1.txt', "r")
script = file.read()
file.close()
file = open('./ep2.txt', "r")
script += file.read()
file.close()
file = open('./ep3.txt', "r")
script += file.read()
file.close()

scriptnolines = script.splitlines()

#print(scriptnolines)
scriptnoblanks = []
for line in scriptnolines:
	line = re.sub(r'\[[^)]*\]', '', line)
	if not line == "": 
		if not line == None:
			if not line == " ":
				scriptnoblanks.append(str(line))
#print(scriptnoblanks)

Yuugi = ""

for line in scriptnoblanks:
	#print(line[:5])
	if line[:5] == "Yuugi":
		Yuugi += line [6:]


print(Yuugi)
file = open('./Yuugi.txt',"w+")
file.write(Yuugi)
file.close()



Yami = ""
for line in scriptnoblanks:
	#print(line[:4])
	if line[:4] == "Yami":
		Yami += line [5:]


print(Yami)
file = open('./Yami.txt',"w+")
file.write(Yami)
file.close()




Joey = ""

for line in scriptnoblanks:
	#print(line[:5])
	if line[:4] == "Joey":
		Joey += line [5:]


print(Joey)
file = open('./Joey.txt',"w+")
file.write(Joey)
file.close()





Seto = ""
for line in scriptnoblanks:
	if line[:4] == "Seto":
		Seto += line [5:]
print(Seto)
file = open('./Seto.txt',"w+")
file.write(Seto)
file.close()
