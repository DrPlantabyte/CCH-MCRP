#!/usr/bin/python3

import json
import sys
import os
import zipfile
import tempfile
import shutil
import math


demo_size = 3
demo_space = demo_size + 3

def main():
	options = []
	files = []
	for arg in sys.argv:
		if(str(arg).startswith('-')):
			options.append(str(arg))
		else:
			files.append(str(arg))
	if(len(sys.argv) < 2) or (len(files) < 1) or ('-h' in options):
		printHelp()
	mcFile = files[0];
	if not os.path.exists(mcFile):
		print('file "{}" does not exist'.format(sys.argv[1]))
		printHelp()
	verbose = '-v' in options
	tempDirHandler = tempfile.TemporaryDirectory()
	tempDir = tempDirHandler.name
	try:
		zipHandler = zipfile.ZipFile(sys.argv[1] , 'r')
		zipHandler.extractall(tempDir)
		zipHandler.close()
		dataDir = os.path.join(tempDir,'data')
		assetDir = os.path.join(tempDir,'assets')
		blocksAndStates = getBlocksAndStates(assetDir, verbose) 
		languageDir = os.path.join(assetDir, 'minecraft', 'lang')
		langFilename = os.listdir(languageDir)[0]
		languageFile = os.path.join(languageDir, langFilename)
		entities = getEntitiesFromLanguageFile(languageFile, 'minecraft', verbose)
		size = int(1 + math.sqrt(len(entities) + len(blocksAndStates)))
		pos = [int(-1*size/2), 0, int(-1*size/2)]
		last_location = printBlockCommands(blocksAndStates, pos, size)
		printEntityZooCommands(entities, pos, size, last_location)
		print('kill @e[type=item]')
	finally:
		# cleanup
		tempDirHandler.cleanup()
	# done
	exit(0)

blockBlacklist = ['minecraft:item_frame', 'minecraft:lava', 'minecraft:water']
doorList = ['minecraft:dark_oak_door', 'minecraft:iron_door', 'minecraft:spruce_door', 'minecraft:jungle_door', 'minecraft:oak_trapdoor', 'minecraft:spruce_trapdoor', 'minecraft:oak_door', 'minecraft:acacia_door']
def getBlocksAndStates(assetDir, verbose=False):
	blocks = {}
	for namespace in os.listdir(assetDir):
		blockstateDir = os.path.join(assetDir, namespace, 'blockstates')
		if not os.path.exists(blockstateDir):
			continue
		for blockfile in os.listdir(blockstateDir):
			if not blockfile.endswith('.json'):
				continue
			blockname = blockfile.replace('.json','')
			block = '{ns}:{bn}'.format(ns=namespace, bn=blockname)
			if(block in blockBlacklist or block in doorList):
				continue
			if(verbose):
				print('block:', block)
			blocks[block] = []
			with open(os.path.join(blockstateDir, blockfile)) as fin:
				bsContent = json.load(fin)
			if('variants' in bsContent):
				# normal block
				states = bsContent['variants']
				if(len(states) > 1):
					# has block states
					for state in states:
						blocks[block].append(str(state))
						if(verbose):
							print('\t:', state)
			elif('multipart' in bsContent):
				# auto-states, treat as no states
				pass
			else:
				print('UNIDENTIFIED BLOCKSTATE FORMAT', file=sys.stderr)
	return blocks

entityBlacklist = ['minecraft:player', 'minecraft:cat', 'minecraft:fishing_bobber', 'minecraft:killer_bunny']
def getEntitiesFromLanguageFile(languageFile, namespace, verbose=False):
	entities = []
	with open(languageFile) as fin:
		langContent = json.load(fin)
	for key in langContent:
		if(key.startswith('entity.minecraft.')):
			# entity name
			entityBaseName = key.replace('entity.minecraft.','')
			if('.' in entityBaseName):
				index = entityBaseName.index('.')
				entityBaseName = entityBaseName[:index]
			entityName = '{ns}:{bn}'.format(ns=namespace, bn=entityBaseName)
			if(entityName in entityBlacklist):
				continue
			if verbose:
				print('entity:',entityName)
			entities.append(entityName)
	return list(set(entities))

def printBlockCommands(blocksAndStates, offset, size):
	x = 0
	y = 0
	z = 0
	for block in blocksAndStates:
		pos = (offset[0]+x, offset[1]+y, offset[2]+z)
		states = blocksAndStates[block]
		bx = pos[0]*demo_space
		bz = pos[2]*demo_space
		if(len(states) < 2):
			print('fill ~{x1} ~{y1} ~{z1} ~{x2} ~{y2} ~{z2} {b} destroy'
				.format(b=block, x1=bx, y1=pos[1], z1=bz, x2=bx+demo_size-1, y2=pos[1]+demo_size-1, z2=bz+demo_size-1))
		else:
			by = pos[1]
			for state in states:
				print('fill ~{x1} ~{y1} ~{z1} ~{x2} ~{y2} ~{z2} {b}[{s}] destroy'
					.format(b=block, s=state, x1=bx, y1=by, z1=bz, x2=bx+demo_size-1, y2=by, z2=bz+demo_size-1))
				by += 1
		x += 1
		if(x >= size):
			x = 0
			z += 1
	return (x, y, z)

def printEntityZooCommands(entities, offset, size, continue_point):
	x = continue_point[0]
	y = continue_point[1]
	z = continue_point[2]
	for entity in entities:
		pos = (offset[0]+x, offset[1]+y, offset[2]+z)
		bx = pos[0]*demo_space
		bz = pos[2]*demo_space
		# label
		row = [' ', ' ', ' ', ' ']
		shortname = entity.replace('minecraft:','')
		row[0] = shortname
		for i in range(3):
			if(len(row[i]) > 15):
				tmp = row[i]
				row[i] = tmp[:15]
				row[i+1] = tmp[15:]
		#
		print('fill ~{x1} ~{y1} ~{z1} ~{x2} ~{y2} ~{z2} {b} destroy'
				.format(b='minecraft:bedrock', x1=bx, y1=pos[1]-1, z1=bz, x2=bx+demo_size-1, y2=pos[1]-1, z2=bz+demo_size-1))
		print('fill ~{x1} ~{y1} ~{z1} ~{x2} ~{y2} ~{z2} {b} destroy'
				.format(b='minecraft:bedrock', x1=bx, y1=pos[1]+4, z1=bz, x2=bx+demo_size-1, y2=pos[1]+4, z2=bz+demo_size-1))
		print('setblock ~{x1} ~{y1} ~{z1} minecraft:sign[rotation=2]{{Text1:"{{\\"text\\":\\"{t1}\\"}}", Text2:"{{\\"text\\":\\"{t2}\\"}}", Text3:"{{\\"text\\":\\"{t3}\\"}}", Text4:"{{\\"text\\":\\"{t4}\\"}}"}}'
				.format(t1=row[0], t2=row[1], t3=row[2], t4=row[3], x1=bx, y1=pos[1], z1=bz+demo_size-1))
		print('summon {e} ~{x1} ~{y1} ~{z1} {{NoAI:1,Invulnerable:1}}'
				.format(e=entity, x1=bx+0.5, y1=pos[1], z1=bz+0.5))
		#
		x += 1
		if(x >= size):
			x = 0
			z += 1
		

def printHelp():
	print("missing argument", "usage: python3 "+os.path.basename(__file__)+" <path to minecraft version jar>", sep='\n\t')
	exit(0)
main()
