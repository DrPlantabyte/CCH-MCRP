# Minecraft function generation functions

import blocks

def fill(out, xyz_tuple1, xyz_tuple2, material, blockstate_dict=None):
	x1 = xyz_tuple1[0]
	x2 = xyz_tuple2[0]
	y1 = xyz_tuple1[1]
	y2 = xyz_tuple2[1]
	z1 = xyz_tuple1[2]
	z2 = xyz_tuple2[2]	if blockstate_dict == None:
		out.write(str.format('fill {} {} {} {} {} {} {} replace\n', x1, y1, z1, x2, y2, z2, material))	else:		state_string = ''		count = 0		for k in blockstate_dict:			if(count > 0):				state_string += ','			state_string += k			state_string += '='			state_string += blockstate_dict[k]			count += 1		out.write(str.format('fill {} {} {} {} {} {} {}[{}] replace\n', x1, y1, z1, x2, y2, z2, material,state_string))
def fill_hollow(out, xyz_tuple1, xyz_tuple2, material):
	x1 = xyz_tuple1[0]
	x2 = xyz_tuple2[0]
	y1 = xyz_tuple1[1]
	y2 = xyz_tuple2[1]
	z1 = xyz_tuple1[2]
	z2 = xyz_tuple2[2]
	out.write(str.format('fill {} {} {} {} {} {} {} outline\n', x1, y1, z1, x2, y2, z2, material))

def fill_replace(out, xyz_tuple1, xyz_tuple2, old_material, new_material):
	x1 = xyz_tuple1[0]
	x2 = xyz_tuple2[0]
	y1 = xyz_tuple1[1]
	y2 = xyz_tuple2[1]
	z1 = xyz_tuple1[2]
	z2 = xyz_tuple2[2]
	out.write(str.format('fill {} {} {} {} {} {} {} replace {}\n', x1, y1, z1, x2, y2, z2, new_material, old_material))
def command_block(out, xyz, command, facing='down', needs_redstone=True, conditional=False, type='impulse'):	if type == 'impulse':		prefix = ''	else if type == 'chain':		prefix = 'chain_'	else if type == 'repeating':		prefix = 'repeating_'	else:		raise ValueError(str.format('{} is not a valid command block type. Must be impulse, chain, or repeating',type))	if needs_redstone == False:		auto_val = 1	else:		auto_val = 0	out.write(str.format('setblock {} {} {} minecraft:{}command_block[facing={},conditional={}] replace\n', 			xyz[0], xyz[1], xyz[2], prefix, facing, boolToStr(conditional)))	out.write(str.format('data merge block {} {} {} {{Command:"{}", auto:{}}}\n', 			xyz[0], xyz[1], xyz[2], command, auto_val))def boolToStr(b):	if(b == True):		return 'true'	else:		return 'false'