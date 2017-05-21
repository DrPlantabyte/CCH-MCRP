import shutil
import sys
import os
import hashlib

this_dir = os.path.dirname(os.path.realpath(__file__))

vanilla_minecraft_dir = os.path.realpath(str(this_dir) + "/../default")
project_dirs=[str(this_dir) + os.sep + "x16"]

def getHash(filepath):
	fin = open(filepath, "rb")
	hasher = hashlib.sha256()
	while True:
		data = fin.read(4096)
		if not data:
			break
		hasher.update(data)
	fin.close()
	return str(hasher.hexdigest())

for root, dirs, files in os.walk(vanilla_minecraft_dir):
	rel_dirpath = str(root).replace(str(vanilla_minecraft_dir), "")
	for local_dir in project_dirs:
		for f in files:
			rel_filepath = rel_dirpath + os.sep + f
			vanilla_filepath = vanilla_minecraft_dir + rel_filepath
			local_filepath = local_dir + rel_filepath
			#print(vanilla_filepath, "?=", local_filepath)
			if os.path.exists(local_filepath):
				# found a project file with a corresponding vanilla minecraft file
				# keep it only if it is different
				vanilla_hash = getHash(vanilla_filepath)
				local_hash   = getHash(local_filepath)
				if local_hash == vanilla_hash:
					print("Removing unmodified file:", rel_filepath)
					os.remove(local_filepath)
				else:
					print("Keeping modified file:", rel_filepath)