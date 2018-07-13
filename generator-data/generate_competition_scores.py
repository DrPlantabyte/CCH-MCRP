#! python3
this_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(this_dir)
	with open(os.path.join(func_dir,'z__competition_score_update.mcfunction'),'w') as update_out, open(os.path.join(func_dir,'z__competition_scoreboard_init.mcfunction'),'w') as init_out, open(os.path.join(func_dir,'z__competition_go_north.mcfunction'),'w') as start_north_out, open(os.path.join(func_dir,'z__competition_go_west.mcfunction'),'w') as start_west_out, open(os.path.join(func_dir,'z__competition_go_south.mcfunction'),'w') as start_south_out, open(os.path.join(func_dir,'z__competition_go_east.mcfunction'),'w') as start_east_out, open(os.path.join(func_dir,'z__competition_spawn_update.mcfunction'),'w') as spawn_update_out:
			entry['type']=data['Type'][n]
			entry['var'] =data['Variable'][n]
			entry['name']=data['Name'][n]
			entry['pts'] =data['Points'][n]
			entry['cat'] =data['Category'][n]
			#print('{var}({type}) = {pts}\t{name} ({cat})'.format(**entry))
			init_command = 'scoreboard objectives add {var} {type} {name}\n'.format(**entry)
					'scoreboard players set @s ptval {pts}\n'+
					'scoreboard players operation @s temp += @s {var}\n'+
					'scoreboard players operation @s temp *= @s ptval\n'+
					'scoreboard players operation @s score += @s temp\n\n').format(**entry)
	lines = file_in.readlines()
	file_in.close()
	for ln in lines: