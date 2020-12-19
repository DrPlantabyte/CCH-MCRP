scoreboard objectives add days_survived dummy "Days Survived"
scoreboard players set @a days_survived 0
forceload add 0 0 15 15
fill 0 250 0 15 255 15 minecraft:barrier
fill 1 251 1 14 254 14 minecraft:air
fill 1 251 2 1 251 7 minecraft:redstone_wire
setblock 1 251 1 minecraft:daylight_detector
setblock 1 251 8 minecraft:command_block[facing=down]{Command:"scoreboard players add @a days_survived 1"}





fill 0 0 0 15 15 15 minecraft:bedrock
fill 1 1 1 14 14 14 minecraft:air
scoreboard objectives add time_alive minecraft.custom:minecraft.time_since_death "Ticks Lived"
setblock 1 1 1 minecraft:command_block[facing=up]{Command:"execute as @a if score @s time_alive matches 1 run spreadplayers 0 0 64 1536 true @s"}

teleport @s 8 240 8
execute at @s run setblock ~ ~-1 ~ dirt_block
execute at @s run fill ~ ~ ~ ~ ~1 ~ air
fill 0 250 0 15 255 15 barrier
fill 1 251 1 14 254 14 air
fill 1 251 1 7 251 1 bedrock
fill 1 252 1 7 252 1 redstone_wire
setblock 1 252 1 daylight_detector
