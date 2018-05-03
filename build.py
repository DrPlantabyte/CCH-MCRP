#!/usr/bin/python3

import shutil
import sys
import os
import hashlib
import zipfile

this_dir = os.path.dirname(os.path.realpath(__file__))

source_dirnames = ["x16"]
project_dirs=[]

def main():
	if not(os.path.exists(str(this_dir) + os.sep + "distributables")):
		os.makedirs(str(this_dir) + os.sep + "distributables")
	for src in source_dirnames:
		src_dir = str(this_dir) + os.sep + src
		zip_file = str(this_dir) + os.sep + "distributables" + os.sep + "CCH-Minecraft_" + src + ".zip"
		the_files = listFiles(src_dir)
		zipFiles(src_dir, the_files, zip_file, zipfile.ZIP_STORED)
		hasher = hashlib.sha1()
		with open(zip_file, 'rb') as f:
			while True:
				data = f.read(4096)
				if not data:
					break
				hasher.update(data)
		sha1_hash = hasher.hexdigest()
		fout = open(zip_file+"_sha1.txt","w")
		fout.write(sha1_hash)
		fout.close()
	world_dir = str(this_dir) + os.sep + "world"
	world_zip = str(this_dir) + os.sep + "distributables" + os.sep + "world.zip"
	zipFiles(world_dir, listFiles(world_dir), world_zip, zipfile.ZIP_DEFLATED)

def zipFiles(source_root, file_list, dest_file, compression):
	# note: Minecraft is bad at handling compressed zip files
	zout = zipfile.ZipFile(dest_file, mode="w", compression=compression, allowZip64=True)
	try:
		for filename in file_list:
			input_file = str(source_root) + os.sep + str(filename)
			zipped_file = str(filename)
			zout.write(input_file, arcname=zipped_file)
	finally:
		zout.close()

def listFiles(root_dir):
	fl = []
	for root, dirs, files in os.walk(root_dir):
		rel_dirpath = os.path.relpath(root, start=root_dir)
		for f in files:
			rel_filepath = rel_dirpath + os.sep + f
			fl.append(rel_filepath)
	return fl

main()
