import random
import math

random.seed()

def main():
	print("""{
	"parent": "minecraft:block/block",
	"textures": {
		"particle": "#ore"
	},
	"elements": [
		{   "from": [ 0, 0, 0 ],
			"to": [ 16, 16, 16 ],
			"faces": {
				"down":  { "texture": "#base", "cullface": "down" },
				"up":    { "texture": "#base", "cullface": "up" },
				"north": { "texture": "#base", "cullface": "north" },
				"south": { "texture": "#base", "cullface": "south" },
				"west":  { "texture": "#base", "cullface": "west" },
				"east":  { "texture": "#base", "cullface": "east" }
			}
		},""")
	
	min = 2
	max = 5
	# top face
	face = "up"
	n = random.randint(min, max)
	cache = []
	for i in range(0,n):
		while True:
			local_x1, local_y1, local_z1, local_x2, local_y2, local_z2 = make_chunk()
			cube = (local_x1, 16 + local_z1, local_y1, local_x2, 16 + local_z2, local_y2)
			if(instersection_validation(cube, cache)):
				cache.append(cube)
				break
	for i in range(0,n):
		if i > 0:
			print(',')
		print_chunk(cache[i], face)
	print(',')
	# bottom face
	face = "down"
	n = random.randint(min, max)
	cache = []
	for i in range(0,n):
		while True:
			local_x1, local_y1, local_z1, local_x2, local_y2, local_z2 = make_chunk()
			cube = (local_x1, 0 - local_z2, local_y1, local_x2, 0 - local_z1, local_y2)
			if(instersection_validation(cube, cache)):
				cache.append(cube)
				break
	for i in range(0,n):
		if i > 0:
			print(',')
		print_chunk(cache[i], face)
	print(',')
	# front face
	face = "south"
	n = random.randint(min, max)
	cache = []
	for i in range(0,n):
		while True:
			local_x1, local_y1, local_z1, local_x2, local_y2, local_z2 = make_chunk()
			cube = (local_x1, local_y1, 16 + local_z1, local_x2, local_y2, 16 + local_z2)
			if(instersection_validation(cube, cache)):
				cache.append(cube)
				break
	for i in range(0,n):
		if i > 0:
			print(',')
		print_chunk(cache[i], face)
	print(',')
	# back face
	face = "north"
	n = random.randint(min, max)
	cache = []
	for i in range(0,n):
		while True:
			local_x1, local_y1, local_z1, local_x2, local_y2, local_z2 = make_chunk()
			cube = (local_x1, local_y1, 0 - local_z2, local_x2, local_y2, 0 - local_z1)
			if(instersection_validation(cube, cache)):
				cache.append(cube)
				break
	for i in range(0,n):
		if i > 0:
			print(',')
		print_chunk(cache[i], face)
	print(',')
	# right face
	face = "east"
	n = random.randint(min, max)
	cache = []
	for i in range(0,n):
		while True:
			local_x1, local_y1, local_z1, local_x2, local_y2, local_z2 = make_chunk()
			cube = (16 + local_z1, local_y1, local_x1, 16 + local_z2, local_y2, local_x2)
			if(instersection_validation(cube, cache)):
				cache.append(cube)
				break
	for i in range(0,n):
		if i > 0:
			print(',')
		print_chunk(cache[i], face)
	print(',')
	# left face
	face = "west"
	n = random.randint(min, max)
	cache = []
	for i in range(0,n):
		while True:
			local_x1, local_y1, local_z1, local_x2, local_y2, local_z2 = make_chunk()
			cube = (0 - local_z2, local_y1, local_x1, 0 - local_z1, local_y2, local_x2)
			if(instersection_validation(cube, cache)):
				cache.append(cube)
				break
	for i in range(0,n):
		if i > 0:
			print(',')
		print_chunk(cache[i], face)
	
	
	print("""
	]
}""")

def make_chunk():
	max_size = 7
	size_x =  max(1, max_size * random.random())
	size_y =  max(1, max_size * random.random())
	local_x1 =  (16 - size_x) * random.random()
	local_y1 =  (16 - size_y) * random.random()
	local_z1 = 0
	local_x2 = local_x1 + size_x
	local_y2 = local_y1 + size_y
	local_z2 =  max(0.5, size_x * size_y / max_size / 2)
	return local_x1, local_y1, local_z1, local_x2, local_y2, local_z2
	
def instersects(cube1, cube2):
	return _instersects(cube1, cube2) or _instersects(cube2, cube1)
	
def _instersects(cube1, cube2):
	xmin = min(cube1[0], cube1[3])
	ymin = min(cube1[1], cube1[4])
	zmin = min(cube1[2], cube1[5])
	xmax = max(cube1[0], cube1[3])
	ymax = max(cube1[1], cube1[4])
	zmax = max(cube1[2], cube1[5])
	if(cube2[0] >= xmin and cube2[0] <= xmax and cube2[1] >= ymin and cube2[1] <= ymax and cube2[2] >= zmax and cube2[2] <= zmax):
		return True
	if(cube2[3] >= xmin and cube2[3] <= xmax and cube2[4] >= ymin and cube2[4] <= ymax and cube2[5] >= zmax and cube2[5] <= zmax):
		return True
	return False

def instersection_validation(cube, list_of_cubes):
	if(len(list_of_cubes) == 0):
		return True
	for cube2 in list_of_cubes:
		if(instersects(cube,cube2)):
			return False
	return True
		
	
def print_chunk(cube, face):
	x1 = round_to_quarter(cube[0])
	y1 = round_to_quarter(cube[1])
	z1 = round_to_quarter(cube[2])
	x2 = round_to_quarter(cube[3])
	y2 = round_to_quarter(cube[4])
	z2 = round_to_quarter(cube[5])
	
	
	
	
	print('		{	"from": [ ',x1,', ',y1,', ',z1,' ], ')
	print('			"to": [ ',x2,', ',y2,', ',z2,' ], ')
	print('			"faces": {')
	tindex = 0
	if(face != "up"):
		if(tindex != 0):
			print(',')
		print('				"down":  { ',uv_string(x1,z1,x2,z2),', "texture": "#ore", "cullface": "',face,'" }', end='')
		tindex += 1
	if(face != "down"):
		if(tindex != 0):
			print(',')
		print('				"up":    { ',uv_string(x1,z1,x2,z2),', "texture": "#ore", "cullface": "',face,'" }', end='')
		tindex += 1
	if(face != "south"):
		if(tindex != 0):
			print(',')
		print('				"north": { ',uv_string(x1,y1,x2,y2),', "texture": "#ore", "cullface": "',face,'" }', end='')
		tindex += 1
	if(face != "north"):
		if(tindex != 0):
			print(',')
		print('				"south": { ',uv_string(x1,y1,x2,y2),', "texture": "#ore", "cullface": "',face,'" }', end='')
		tindex += 1
	if(face != "east"):
		if(tindex != 0):
			print(',')
		print('				"west":  { ',uv_string(z1,y1,z2,y2),', "texture": "#ore", "cullface": "',face,'" }', end='')
		tindex += 1
	if(face != "west"):
		if(tindex != 0):
			print(',')
		print('				"east":  { ',uv_string(z1,y1,z2,y2),', "texture": "#ore", "cullface": "',face,'" }', end='')
		tindex += 1
	print()
	print('			}')
	print('		}', end='')

def uv_string(u1,v1,u2,v2):
	umin = min(abs(u1),abs(u2))
	vmin = min(abs(v1),abs(v2))
	umax = max(abs(u1),abs(u2))
	vmax = max(abs(v1),abs(v2))
	if(umax > 16):
		umax -= umin
		umin = 0
	if(vmax > 16):
		vmax -= vmin
		vmin = 0
	return '"uv": [ ' + str(umin) + ', ' + str(vmin) + ', ' + str(umax) + ', ' + str(vmax) + ' ]'

def round_to_quarter(n):
	return round(n * 4,0) / 4
def round_rotation(r):
	# only -45/-22.5/0/22.5/45 is allowed by Minecraft
	degrees = r * 180 / math.pi
	while r > 180:
		r -= 360
	while r < -180:
		r += 360
	ticks = round(degrees / (360 / 22.5) ,0)
	while(ticks > 2):
		ticks -= 4
	while(ticks < -2):
		ticks += 4
	return ticks * -22.5

main()