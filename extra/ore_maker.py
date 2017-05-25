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
	
	min = 3
	max = 5
	# top face
	face = "up"
	n = random.randint(min, max)
	for i in range(0,n):
		if i > 0:
			print(',')
		local_x, local_y, local_z, u, v, size, xr, yr, zr = make_chunk()
		print_chunk(local_x, local_z + 16, local_y, u, v, size, 0, yr, 0, face)
	print(',')
	# bottom face
	face = "down"
	n = random.randint(min, max)
	for i in range(0,n):
		if i > 0:
			print(',')
		local_x, local_y, local_z, u, v, size, xr, yr, zr = make_chunk()
		print_chunk(local_x, 0 - local_z, local_y, u, v, size, 0, yr, 0, face)
		
	print(',')
	# front face
	face = "south"
	n = random.randint(min, max)
	for i in range(0,n):
		if i > 0:
			print(',')
		local_x, local_y, local_z, u, v, size, xr, yr, zr = make_chunk()
		print_chunk(local_x, local_y, local_z + 16, u, v, size, 0, 0, zr, face)
	print(',')
	# back face
	face = "north"
	n = random.randint(min, max)
	for i in range(0,n):
		if i > 0:
			print(',')
		local_x, local_y, local_z, u, v, size, xr, yr, zr = make_chunk()
		print_chunk(local_x, local_y, 0 - local_z, u, v, size, 0, 0, zr, face)
	print(',')
	# left face
	face = "west"
	n = random.randint(min, max)
	for i in range(0,n):
		if i > 0:
			print(',')
		local_x, local_y, local_z, u, v, size, xr, yr, zr = make_chunk()
		print_chunk(0 - local_z, local_y, local_x, u, v, size, xr, 0, 0, face)
	print(',')
	# right face
	face = "east"
	n = random.randint(min, max)
	for i in range(0,n):
		if i > 0:
			print(',')
		local_x, local_y, local_z, u, v, size, xr, yr, zr = make_chunk()
		print_chunk(local_z + 16, local_y, local_x, u, v, size, xr, 0, 0, face)
	
	
	print("""
	]
}""")

def make_chunk():
	size = 3 * random.random() + 1
	t = 0.5 * size * math.sqrt(2)
	local_x =  (16 - (2 * t)) * random.random() + t
	local_y =  (16 - (2 * t)) * random.random() + t
	local_z = size * (0.25 - 0.5 * random.random())
	xr, yr, zr = rand_orientation()
	u = (16 - size) * random.random()
	v = (16 - size) * random.random()
	return local_x, local_y, local_z, u, v, size, xr, yr, zr
	

def rand_orientation():
	x_rot = random.random() * 2 * math.pi
	y_rot = random.random() * 2 * math.pi
	z_rot = random.random() * 2 * math.pi
	return x_rot, y_rot, z_rot

def print_chunk(x, y, z, u, v, size, x_rot, y_rot, z_rot, face):
	nx = round_to_quarter(x)
	ny = round_to_quarter(y)
	nz = round_to_quarter(z)
	nsize = round_to_quarter(size / 2)
	nx_rot = round_rotation(x_rot) 
	ny_rot = round_rotation(y_rot)
	nz_rot = round_rotation(z_rot)
	nu = round_to_quarter(u)
	nv = round_to_quarter(v)
	while nu+nsize > 16:
		nu -= 1
	while nv+nsize > 16:
		nv -= 1
	
	print('		{	"from": [ ',nx - nsize,', ',ny - nsize,', ',nz - nsize,' ], ')
	print('			"to": [ ',nx + nsize,', ',ny + nsize,', ',nz + nsize,' ], ')
	if(nx_rot != 0):
		print('			"rotation": { "origin": [ ',nx,', ',ny,', ',nz,' ], "axis": "x", "angle": ',nx_rot,' },')
	if(ny_rot != 0):
		print('			"rotation": { "origin": [ ',nx,', ',ny,', ',nz,' ], "axis": "y", "angle": ',ny_rot,' },')
	if(nz_rot != 0):
		print('			"rotation": { "origin": [ ',nx,', ',ny,', ',nz,' ], "axis": "z", "angle": ',nz_rot,' },')
	print('			"faces": {')
	tindex = 0
	if(face != "up"):
		if(tindex != 0):
			print(',')
		print('				"down":  { "uv": [ ',nu,', ',nv,', ',nu+nsize,', ',nv+nsize,' ], "texture": "#ore", "cullface": "',face,'" }', end='')
		tindex += 1
	if(face != "down"):
		if(tindex != 0):
			print(',')
		print('				"up":    { "uv": [ ',nu,', ',nv,', ',nu+nsize,', ',nv+nsize,' ], "texture": "#ore", "cullface": "',face,'" }', end='')
		tindex += 1
	if(face != "south"):
		if(tindex != 0):
			print(',')
		print('				"north": { "uv": [ ',nu,', ',nv,', ',nu+nsize,', ',nv+nsize,' ], "texture": "#ore", "cullface": "',face,'" }', end='')
		tindex += 1
	if(face != "north"):
		if(tindex != 0):
			print(',')
		print('				"south": { "uv": [ ',nu,', ',nv,', ',nu+nsize,', ',nv+nsize,' ], "texture": "#ore", "cullface": "',face,'" }', end='')
		tindex += 1
	if(face != "east"):
		if(tindex != 0):
			print(',')
		print('				"west":  { "uv": [ ',nu,', ',nv,', ',nu+nsize,', ',nv+nsize,' ], "texture": "#ore", "cullface": "',face,'" }', end='')
		tindex += 1
	if(face != "west"):
		if(tindex != 0):
			print(',')
		print('				"east":  { "uv": [ ',nu,', ',nv,', ',nu+nsize,', ',nv+nsize,' ], "texture": "#ore", "cullface": "',face,'" }', end='')
		tindex += 1
	print()
	print('			}')
	print('		}', end='')

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