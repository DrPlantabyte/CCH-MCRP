fin = open("C:/Users/Cybergnome/Documents/Minecraft/Resource Packs/1.11/CCH_V1-03_16x/assets/minecraft/lang/en_us.lang", "r")
fin2 = open("C:/Users/Cybergnome/Documents/Minecraft/Resource Packs/1.12/default/assets/minecraft/lang/en_us.lang", "r")
fout = open("C:/Users/Cybergnome/Documents/Minecraft/Resource Packs/1.12/CCH-Minecraft/x16/assets/minecraft/lang/en_us.lang","w")

set = {}
for ln in fin2.readlines():
	try:
		eq_index = ln.index("=")
		k = ln[0:eq_index]
		v = ln[eq_index+1:len(ln)]
		set[k]=v
	except:
		pass

for ln in fin.readlines():
	try:
		eq_index = ln.index("=")
		k = ln[0:eq_index]
		v = ln[eq_index+1:len(ln)]
		set[k]=v
	except:
		pass

lines = []
for k, v in set.items():
	ln = k + "=" + v
	lines.append(ln)

lines.sort()

for ln in lines:
	fout.write(ln)

fin.close()
fin2.close()
fout.close()
