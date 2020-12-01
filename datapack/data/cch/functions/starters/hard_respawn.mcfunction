teleport @s 8 240 8
execute at @s run setblock ~ ~-1 ~ dirt_block
execute at @s run fill ~ ~ ~ ~ ~1 ~ air
fill 0 250 0 15 255 15 barrier
fill 1 251 1 14 254 14 air
fill 1 251 1 7 251 1 bedrock
fill 1 252 1 7 252 1 redstone_wire
setblock 1 252 1 daylight_detector
