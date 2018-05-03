#!/usr/bin/python3

import shutil
import sys
import os
import hashlib
import zipfile

this_dir = os.path.dirname(os.path.realpath(__file__))

texture_dirs = ["x16"]
datapack_dir = os.path.join(this_dir, "datapack")
dist_dir = os.path.join(this_dir, "distributables")


def main():
	if not(os.path.exists(dist_dir)):
		os.makedirs(dist_dir)
	for tex_src in texture_dirs:
		src_dir = os.path.join(this_dir, tex_src)
		zip_file = os.path.join(dist_dir, "CCH_resourcepack_" + str(tex_src) + ".zip")
		zipDir(src_dir, zip_file)
	zipDir(datapack_dir, os.path.join(dist_dir, "CCH_datapack.zip"))

def zipDir(src_dir, dest_filepath):
	the_files = listFiles(src_dir)
	zipFiles(src_dir, the_files, dest_filepath, zipfile.ZIP_STORED)
	sha1_hash = hashFile(dest_filepath)
	fout = open(dest_filepath+"_sha1.txt","w")
	fout.write(sha1_hash)
	fout.close()

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
def hashFile(filepath):
	hasher = hashlib.sha1()
	with open(filepath, 'rb') as f:
		while True:
			data = f.read(4096)
			if not data:
				break
			hasher.update(data)
	sha1_hash = hasher.hexdigest()
	return sha1_hash

def listFiles(root_dir):
	fl = []
	for root, dirs, files in os.walk(root_dir):
		rel_dirpath = os.path.relpath(root, start=root_dir)
		for f in files:
			rel_filepath = rel_dirpath + os.sep + f
			fl.append(rel_filepath)
	return fl

main()
