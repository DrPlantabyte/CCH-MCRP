#!/usr/bin/python3

import shutil
import distutils
from distutils.dir_util import copy_tree
import sys
import os
from os import path
import hashlib
import zipfile

this_dir = path.dirname(path.abspath(__file__))

MC_VERSION = 'MC20'

texture_dirs = ["x16", "x32", "x64", "x128", "x256"]
resourcepack_dir = path.join(this_dir, "resourcepack")
datapack_dir = path.join(this_dir, "datapack")
dist_dir = path.join(this_dir, "distributables")
build_dir = path.join(this_dir, "temp")


def main():
	# from build scripts
	import lang_convert
	lang_convert.main()
	# setup dirs
	if not(path.exists(dist_dir)):
		os.makedirs(dist_dir)
	else:
		cleanDir(dist_dir)
	if not(path.exists(build_dir)):
		os.makedirs(build_dir)
	else:
		cleanDir(build_dir)	
	for tex_src in texture_dirs:
		common_dir = path.join(resourcepack_dir, 'common')
		src_dir = path.join(resourcepack_dir, tex_src)
		if not path.exists(src_dir):
			# texture not supported
			continue
		print("\n\tBuilding texture pack '%s'..." % tex_src)
		# setup build dirs
		tmp_build_dir = path.join(build_dir, tex_src)
		if not(path.exists(tmp_build_dir)):
			os.makedirs(tmp_build_dir)
		# copy sources
		copy_tree(common_dir, tmp_build_dir)
		copy_tree(src_dir, tmp_build_dir)
		# distribute as .zip file
		zip_file = path.join(dist_dir, "CCH_MCRP_%s_%s.zip" % (MC_VERSION, tex_src))
		zipDir(tmp_build_dir, zip_file)
	## distribute the datapack
	print(str.format("\n\tBuilding datapacks..."))
	for dpack in os.listdir(datapack_dir):
		zipDir(path.join(datapack_dir, dpack), path.join(dist_dir, "CCH_datapack_%s_%s.zip" % (dpack, MC_VERSION)))
	
	# clean-up
	shutil.rmtree(build_dir)
def cleanDir(dir_path):
	for f in os.listdir(dir_path):
		inner_file = path.join(dir_path, f)
		if path.isdir(inner_file):
			shutil.rmtree(inner_file)
		else:
			os.remove(inner_file)
def zipDir(src_dir, dest_filepath):
	print(str.format("Zipping '{}' to '{}'", src_dir, dest_filepath))
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
	print(str.format("Hashing file '{}' with SHA1", filepath))
	hasher = hashlib.sha1()
	with open(filepath, 'rb') as f:
		while True:
			data = f.read(4096)
			if not data:
				break
			hasher.update(data)
	sha1_hash = hasher.hexdigest()
	print(str.format("\t'{}'", sha1_hash))
	return sha1_hash

def listFiles(root_dir):
	fl = []
	for root, dirs, files in os.walk(root_dir):
		rel_dirpath = path.relpath(root, start=root_dir)
		for f in files:
			rel_filepath = rel_dirpath + os.sep + f
			fl.append(rel_filepath)
	return fl

main()
