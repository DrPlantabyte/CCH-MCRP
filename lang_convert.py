#!/usr/bin/python3
import json, os, re, collections, operator
from os import path

THIS_DIR = path.dirname(path.abspath(__file__))
os.chdir(THIS_DIR)
print(path.abspath('.'))

def main():
	with open('../MC-1.21.4/assets/minecraft/lang/en_us.json', 'rb') as file_in, open('resourcepack/common/assets/minecraft/lang/en_us.json','w') as file_out:
		json_str = file_in.read().decode('utf8', errors='replace')
		src_data = json.loads(json_str)
		out_data = {}
		for key in src_data:
			src_val = src_data[key]
			dst_val = change(key=key, val=src_val)
			if dst_val is not None and src_val != dst_val:
				out_data[key] = dst_val
		print_and_write(json.dumps(sort_dict(out_data), indent='  '), file_out)
#
def print_and_write(text, file_handle):
	print(text)
	file_handle.write(text)
#
def sort_dict(d):
	keys = sorted(d)
	dd = collections.OrderedDict()
	for k in keys:
		dd[k] = d[k]
	return dd
#
def change(key, val):
	# example : if re.search('apple|oak',key) == None: return None
	text = val
	## steel
	if re.search('raw|ore|advancements',key) == None and "golem" not in text.lower():
		text = text.replace('Iron ','Steel ').replace('iron ','steel ')
		text = text.replace(' Iron',' Steel').replace(' iron',' steel')
	## weapons and armor
	if re.search('sword',key) != None:
		text = text.replace('Wooden Sword','Club')
	if re.search('helmet|chestplate|leggings|boots',key) != None:
		text = text.replace('Chainmail Chestplate','Chainmail Shirt').replace('Chainmail Hemlet','Chainmail Hood')
	## animals
	# none
	## plants
	text = text.replace('Dark Oak','Darkwood')
	text = text.replace('Petrified Oak','Petrified Wood')
	if re.search('door|slab|plate|sign|button|stair|planks',key) != None:
		text = text.replace('Oak ','Wooden ').replace('oak ','wooden ')
		text = text.replace('Oak','Wooden').replace('oak','wooden')
	elif "croak" not in text.lower():
		text = text.replace('Oak ','').replace('oak ','')
		text = text.replace('Oak','').replace('oak','')
	text = text.replace('Beetroot','Beet').replace('beetroot','beet')
	text = text.replace('Bone Meal','Fertilizer').replace('bone meal','fertilizer')
	## other stuff
	text = text.replace('End Rod','Glow Rod')
	text = text.replace('Gunpowder','Black Powder')
	text = text.replace('TNT','Bomb')
	return text

#
if __name__ == '__main__':
    main()
#
