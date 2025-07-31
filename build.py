#!/usr/bin/python3

import shutil
import distutils
from distutils.dir_util import copy_tree
import sys
import json
import os
from os import path
import hashlib
import zipfile
import re
from pathlib import Path
from typing import Callable

this_dir = Path(__file__).absolute().parent

MC_VERSION = '1.21.8'
HOME_DIR = Path(os.path.expanduser("~")).absolute()
MC_SOURCE_FILE = HOME_DIR / f'AppData/Roaming/.minecraft/versions/{MC_VERSION}/{MC_VERSION}.jar'
MC_ASSETS_DIR = this_dir.parent / f'MC-{MC_VERSION}'

texture_dirs = ["x16", "x32", "x64", "x128", "x256"]
resourcepack_dir = this_dir / "resourcepack"
datapacks_dir = this_dir / "datapack"
dist_dir = this_dir / "distributables"
build_dir = this_dir / "temp"


def main():
	# extract minecraft assets
	if not MC_ASSETS_DIR.is_dir():
		unzip(MC_SOURCE_FILE, MC_ASSETS_DIR, r'^((assets|data)/.*|.+\.(?!class).*)$')
	# read and update pack format numbers
	with (MC_ASSETS_DIR / "version.json").open("r") as fin:
		version_data = json.load(fin)
	resource_pack_format = version_data["pack_version"]["resource"]
	data_pack_format = version_data["pack_version"]["data"]
	update_json_file(resourcepack_dir / "common/pack.mcmeta", lambda d: d["pack"].update(pack_format=resource_pack_format))
	for dp_dir in [p for p in datapacks_dir.iterdir() if p.is_dir()]:
		update_json_file(dp_dir / "pack.mcmeta", lambda d: d["pack"].update(pack_format=data_pack_format))

	# rebuild the lang file
	import lang_convert
	lang_convert.convert_lang(
		MC_ASSETS_DIR / 'assets/minecraft/lang/en_us.json',
		resourcepack_dir / 'common/assets/minecraft/lang/en_us.json'
	)

	# rebuild the doors and trapdoors
	src_tex_dir = MC_ASSETS_DIR / 'assets/minecraft/textures'
	src_item_models_dir = MC_ASSETS_DIR / 'assets/minecraft/models/item'
	dst_item_models_dir = resourcepack_dir / 'common/assets/minecraft/models/item'
	for door_src_model in [Path(x) for x in src_item_models_dir.glob('*_door.json')]:
		if door_src_model.name.startswith('template_'):
			# skip templates
			continue
		print(f'Applying door item update to {door_src_model.name}')
		dst_path = dst_item_models_dir / door_src_model.name
		block_name = door_src_model.name.replace('_door.json','')
		top_tex = f'block/{block_name}_door_top'
		btm_tex = f'block/{block_name}_door_bottom'
		assert (src_tex_dir / f'{top_tex}.png').exists(), f'{top_tex} tecture does not exist'
		assert (src_tex_dir / f'{btm_tex}.png').exists(), f'{btm_tex} tecture does not exist'
		model_data = {
			"parent": "cch:item/door_item",
			"textures": {
				"bottom": f"minecraft:{btm_tex}",
				"top": f"minecraft:{top_tex}"
			}
		}
		with dst_path.open('w') as fout:
			json.dump(model_data, fout, indent='    ')

	src_block_models_dir = MC_ASSETS_DIR / 'assets/minecraft/models/block'
	dst_block_models_dir = resourcepack_dir / 'common/assets/minecraft/models/block'
	for trapdoor_src_model in [Path(x) for x in src_block_models_dir.glob('*_trapdoor_*.json')]:
		if trapdoor_src_model.name.startswith('template_'):
			# skip templates
			continue
		print(f'Applying trapdoor update to {trapdoor_src_model.name}')
		dst_path = dst_block_models_dir / trapdoor_src_model.name
		block_name, trapdoor_type = trapdoor_src_model.stem.split('_trapdoor_')
		assert trapdoor_type in ('top', 'bottom', 'open')
		with trapdoor_src_model.open('r') as fin:
			src_data = json.load(fin)
		tex = src_data['textures']['texture']
		#if tex.lstrip('minecraft:').replace()
		if (src_tex_dir / f"{tex.replace('minecraft:','').replace('trapdoor', 'planks')}.png").exists():
			new_tex = tex.replace('trapdoor', 'planks')
		elif (src_tex_dir / f"{tex.replace('minecraft:','').replace('_trapdoor', '')}.png").exists():
			new_tex = tex.replace('_trapdoor', '')
		elif (src_tex_dir / f"{tex.replace('minecraft:','').replace('trapdoor', 'block')}.png").exists():
			new_tex = tex.replace('trapdoor', 'block')
		else:
			raise FileNotFoundError(f"Could not find appropriate texture for {trapdoor_src_model.name}")
		model_data = {
			"parent": f"cch:block/trapdoor_{trapdoor_type}",
			"textures": {
				"texture": new_tex
			}
		}
		with dst_path.open('w') as fout:
			json.dump(model_data, fout, indent='    ')

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
		zip_file = path.join(dist_dir, "CCH_MCRP_MC%s_%s.zip" % (MC_VERSION, tex_src))
		zipDir(tmp_build_dir, zip_file)
	## distribute the datapack
	print(str.format("\n\tBuilding datapacks..."))
	for dpack in os.listdir(datapacks_dir):
		zipDir(path.join(datapacks_dir, dpack), path.join(dist_dir, "CCH_datapack_%s_%s.zip" % (dpack, MC_VERSION)))
	
	# clean-up
	shutil.rmtree(build_dir)

def unzip(zip_filepath: str|Path, dest_dirpath: str|Path, regex_filter: str=None):
	if regex_filter is None:
		regex_filter = ".*"
	regex = re.compile(regex_filter)

	with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
		# List of matching files
		matching_files = [f for f in zip_ref.namelist() if regex.search(f)]

		if not matching_files:
			print(f"No files matched the pattern '{regex_filter}'.")
			return

		# Ensure the output directory exists
		os.makedirs(dest_dirpath, exist_ok=True)

		# Extract matching files
		for file in matching_files:
			zip_ref.extract(file, path=dest_dirpath)
			print(f"Extracted: {file}")

def update_json_file(filepath: str|Path, update_fn: Callable[[dict],None]):
	with Path(filepath).open("r") as fin:
		data = json.load(fin)
	update_fn(data)
	with Path(filepath).open("w") as fout:
		json.dump(data, fout, indent='\t')

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
