setworldspawn ~-3 ~ ~-3spawnpoint @a ~ ~ ~scoreboard objectives add days dummy "Days Survived"
scoreboard objectives setdisplay list daysgamerule commandBlockOutput falsefill ~-16 ~-9 ~-16 ~16 ~11 ~16 minecraft:barrier hollow
fill ~-15 ~-9 ~-15 ~15 ~-1 ~15 minecraft:bedrock hollow
fill ~-14 ~-2 ~-14 ~14 ~-2 ~14 minecraft:glowstone replacefill ~-1 ~-7 ~-1 ~1 ~-1 ~1 minecraft:barrier hollow
fill ~-15 ~10 ~-15 ~15 ~32 ~15 minecraft:barrier replace
fill ~-15 ~33 ~-15 ~15 ~64 ~15 minecraft:barrier replace
fill ~-15 ~65 ~-15 ~15 ~96 ~15 minecraft:barrier replace
fill ~-15 ~97 ~-15 ~15 ~128 ~15 minecraft:barrier replace
fill ~-15 ~129 ~-15 ~15 ~160 ~15 minecraft:barrier replace
fill ~-15 ~161 ~-15 ~15 ~192 ~15 minecraft:barrier replace
fill ~-15 ~193 ~-15 ~15 ~224 ~15 minecraft:barrier replace
fill ~-15 ~225 ~-15 ~15 ~255 ~15 minecraft:barrier replace
fill ~-14 ~10 ~-14 ~14 ~32 ~14 minecraft:air replace
fill ~-14 ~33 ~-14 ~14 ~64 ~14 minecraft:air replace
fill ~-14 ~65 ~-14 ~14 ~96 ~14 minecraft:air replace
fill ~-14 ~97 ~-14 ~14 ~128 ~14 minecraft:air replace
fill ~-14 ~129 ~-14 ~14 ~160 ~14 minecraft:air replace
fill ~-14 ~161 ~-14 ~14 ~192 ~14 minecraft:air replace
fill ~-14 ~193 ~-14 ~14 ~224 ~14 minecraft:air replace
fill ~-14 ~225 ~-14 ~14 ~255 ~14 minecraft:air replace
fill ~-4 ~-1 ~-4 ~4 ~-1 ~-4 minecraft:barrier replace
fill ~-4 ~-1 ~-4 ~-4 ~-1 ~4 minecraft:barrier replace
fill ~4 ~-1 ~4 ~-4 ~-1 ~4 minecraft:barrier replace
fill ~4 ~-1 ~4 ~4 ~-1 ~-4 minecraft:barrier replace
fill ~-8 ~-1 ~-8 ~8 ~-1 ~-8 minecraft:barrier replace
fill ~-8 ~-1 ~-8 ~-8 ~-1 ~8 minecraft:barrier replace
fill ~8 ~-1 ~8 ~-8 ~-1 ~8 minecraft:barrier replace
fill ~8 ~-1 ~8 ~8 ~-1 ~-8 minecraft:barrier replace
fill ~-12 ~-1 ~-12 ~12 ~-1 ~-12 minecraft:barrier replace
fill ~-12 ~-1 ~-12 ~-12 ~-1 ~12 minecraft:barrier replace
fill ~12 ~-1 ~12 ~-12 ~-1 ~12 minecraft:barrier replace
fill ~12 ~-1 ~12 ~12 ~-1 ~-12 minecraft:barrier replacefill ~3 ~-3 ~-1 ~5 ~-8 ~1 minecraft:barrier hollow
setblock ~4 ~-8 ~2 minecraft:chest[facing=south] replace
data merge block ~4 ~-8 ~2 {Items:[{Slot:0,id:"minecraft:cookie",Count:4},{Slot:1,id:"minecraft:end_rod",Count:2},{Slot:2,id:"minecraft:flint_and_steel",Count:1},{Slot:3,id:"minecraft:writable_book",Count:1}]}
setblock ~ ~-7 ~ minecraft:stone_pressure_plate replace
setblock ~ ~-8 ~ minecraft:command_block[facing=east] replacedata merge block ~ ~-8 ~ {Command:"tp @p ~4 ~1 ~", auto:0}
setblock ~1 ~-8 ~ minecraft:chain_command_block[facing=east] replace
data merge block ~1 ~-8 ~ {Command:"clone ~3 ~ ~2 ~3 ~ ~2 ~3 ~3 ~ replace force", auto:1}
setblock ~2 ~-8 ~ minecraft:chain_command_block[facing=north] replace
data merge block ~2 ~-8 ~ {Command:"fill ~2 ~3 ~ ~2 ~3 ~ minecraft:air destroy", auto:1}
setblock ~2 ~-8 ~-1 minecraft:chain_command_block[facing=west] replace
data merge block ~2 ~-8 ~-1 {Command:"scoreboard players set @a[distance=..16] days 0", auto:1}setblock ~ ~-8 ~-1 minecraft:redstone_wire replace
fill ~ ~-8 ~-2 ~4 ~-8 ~-2 minecraft:redstone_wire replace
setblock ~4 ~-8 ~-1 minecraft:repeater[facing=north,delay=4] replace
setblock ~4 ~-8 ~ minecraft:command_block[facing=up] replace
data merge block ~4 ~-8 ~ {Command:"spreadplayers 0 0 64 1536 false @p", auto:0}

fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 minecraft:bedrock replace
setblock ~ ~-1 ~ minecraft:air replacefill ~-3 ~-7 ~-3 ~-3 ~10 ~-3 minecraft:barrier replace
setblock ~-3 ~-8 ~-3 minecraft:daylight_detector replace
setblock ~-4 ~-8 ~-3 minecraft:comparator[facing=east] replace
setblock ~-3 ~-8 ~-4 minecraft:command_block[facing=up] replace
data merge block ~-3 ~-8 ~-4 {Command:"scoreboard players add @a days 1", auto:0}
setblock ~-3 ~-7 ~-4 minecraft:chain_command_block[facing=up] replace
data merge block ~-3 ~-7 ~-4 {Command:"spawnpoint @a ~ ~7 ~", auto:1}
setblock ~-5 ~-8 ~-3 minecraft:redstone_wire replace
setblock ~-5 ~-8 ~-4 minecraft:redstone_wire replace
setblock ~-5 ~-8 ~-5 minecraft:redstone_wire replace
setblock ~-5 ~-8 ~-6 minecraft:redstone_wire replace
setblock ~-5 ~-8 ~-7 minecraft:redstone_wire replace
setblock ~-4 ~-8 ~-7 minecraft:repeater[facing=west] replace
setblock ~-3 ~-8 ~-7 minecraft:redstone_wire replace
setblock ~-3 ~-8 ~-6 minecraft:redstone_wire replace
setblock ~-3 ~-8 ~-5 minecraft:redstone_wire replace