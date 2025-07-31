time set 1000
scoreboard objectives add days_survived dummy "Days Survived"
scoreboard objectives setdisplay sidebar days_survived
forceload add 0 0 15 15
fill 0 253 0 15 255 15 minecraft:barrier
fill 1 254 1 14 254 14 minecraft:air
fill 1 254 2 1 254 7 minecraft:redstone_wire
setblock 1 254 1 minecraft:daylight_detector
setblock 1 254 8 minecraft:command_block[facing=down]{Command:"scoreboard players add @a days_survived 1"}
scoreboard objectives add time_alive minecraft.custom:minecraft.time_since_death "Ticks Lived"
scoreboard players set @a days_survived 0
