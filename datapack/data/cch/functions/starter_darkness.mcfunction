setworldspawn ~1 ~ ~
spawnpoint @a ~4 ~ ~-1
gamerule commandBlockOutput false

fill ~-5 ~-1 ~7 ~13 ~8 ~-16 minecraft:air replace
fill ~-5 ~-6 ~7 ~13 ~-1 ~-16 minecraft:bedrock replace
fill ~-4 ~-1 ~6 ~12 ~-1 ~-15 minecraft:lava replace
fill ~-3 ~-1 ~5 ~11 ~-1 ~-14 minecraft:quartz_block replace
fill ~-2 ~ ~3 ~-2 ~3 ~3 minecraft:quartz_pillar[axis=y] replace
fill ~-2 ~ ~ ~-2 ~3 ~ minecraft:quartz_pillar[axis=y] replace
fill ~-2 ~ ~-3 ~-2 ~3 ~-3 minecraft:quartz_pillar[axis=y] replace
fill ~-2 ~ ~-6 ~-2 ~3 ~-6 minecraft:quartz_pillar[axis=y] replace
fill ~-2 ~ ~-9 ~-2 ~3 ~-9 minecraft:quartz_pillar[axis=y] replace
fill ~-2 ~ ~-12 ~-2 ~3 ~-12 minecraft:quartz_pillar[axis=y] replace
fill ~10 ~ ~3 ~10 ~3 ~3 minecraft:quartz_pillar[axis=y] replace
fill ~10 ~ ~ ~10 ~3 ~ minecraft:quartz_pillar[axis=y] replace
fill ~10 ~ ~-3 ~10 ~3 ~-3 minecraft:quartz_pillar[axis=y] replace
fill ~10 ~ ~-6 ~10 ~3 ~-6 minecraft:quartz_pillar[axis=y] replace
fill ~10 ~ ~-9 ~10 ~3 ~-9 minecraft:quartz_pillar[axis=y] replace
fill ~10 ~ ~-12 ~10 ~3 ~-12 minecraft:quartz_pillar[axis=y] replace
setblock ~-1 ~ ~3 minecraft:wall_torch[facing=east] replace
setblock ~-1 ~ ~ minecraft:wall_torch[facing=east] replace
setblock ~-1 ~ ~-3 minecraft:wall_torch[facing=east] replace
setblock ~-1 ~ ~-6 minecraft:wall_torch[facing=east] replace
setblock ~-1 ~ ~-9 minecraft:wall_torch[facing=east] replace
setblock ~-1 ~ ~-12 minecraft:wall_torch[facing=east] replace
setblock ~9 ~ ~3 minecraft:wall_torch[facing=west] replace
setblock ~9 ~ ~ minecraft:wall_torch[facing=west] replace
setblock ~9 ~ ~-3 minecraft:wall_torch[facing=west] replace
setblock ~9 ~ ~-6 minecraft:wall_torch[facing=west] replace
setblock ~9 ~ ~-9 minecraft:wall_torch[facing=west] replace
setblock ~9 ~ ~-12 minecraft:wall_torch[facing=west] replace

fill ~-1 ~ ~2 ~9 ~3 ~5 minecraft:quartz_block replace
setblock ~4 ~2 ~1 minecraft:wall_sign[facing=north]{"Text1":"{\"text\":\"When the shadows\"}", "Text2":"{\"text\":\"unmake the world,\"}", "Text3":"{\"text\":\"champions of light\"}", "Text4":"{\"text\":\"fear not death.\"}"} replace
setblock ~4 ~1 ~1 minecraft:wall_sign[facing=north]{"Text1":"{\"text\":\"Place the blocks\"}", "Text2":"{\"text\":\"upon the shrines\"}", "Text3":"{\"text\":\"to heal the world\"}", "Text4":"{\"text\":\"rent by shadows.\"}"} replace
setblock ~4 ~ ~1 minecraft:wall_sign[facing=north]{"Text1":"{\"text\":\"Banish darkness\"}", "Text2":"{\"text\":\"where you stray\"}", "Text3":"{\"text\":\"evil yet lingers\"}", "Text4":"{\"text\":\"in the shadows.\"}"} replace


gamerule doDaylightCycle false
fill ~ ~ ~2 ~2 ~2 ~4 minecraft:bedrock replace
setblock ~1 ~1 ~2 minecraft:barrier replace
setblock ~1 ~1 ~3 minecraft:diamond_block replace
setblock ~1 ~-1 ~1 minecraft:repeating_command_block[facing=down,conditional=false] replace
data merge block ~1 ~-1 ~1 {Command:"execute unless block ~ ~1 ~ minecraft:diamond_block run time set 20000", auto:1}
setblock ~1 ~-2 ~1 minecraft:repeating_command_block[facing=down,conditional=false] replace
data merge block ~1 ~-2 ~1 {Command:"execute if block ~ ~2 ~ minecraft:diamond_block run gamerule doDaylightCycle true", auto:1}
setblock ~1 ~-3 ~1 minecraft:chain_command_block[facing=down,conditional=true] replace
data merge block ~1 ~-3 ~1 {Command:"time set 21950", auto:1}
setblock ~1 ~-4 ~1 minecraft:chain_command_block[facing=down,conditional=true] replace
data merge block ~1 ~-4 ~1 {Command:"fill ~ ~ ~ ~ ~3 ~ minecraft:bedrock replace", auto:1}


gamerule doWeatherCycle false
weather thunder 1000000
fill ~2 ~ ~2 ~4 ~2 ~4 minecraft:bedrock replace
setblock ~3 ~1 ~2 minecraft:barrier replace
setblock ~3 ~1 ~3 minecraft:magma_block replace
setblock ~3 ~-1 ~1 minecraft:repeating_command_block[facing=down,conditional=false] replace
data merge block ~3 ~-1 ~1 {Command:"execute if block ~ ~1 ~ minecraft:magma_block run weather clear", auto:1}
setblock ~3 ~-2 ~1 minecraft:chain_command_block[facing=down,conditional=true] replace
data merge block ~3 ~-2 ~1 {Command:"gamerule doWeatherCycle true", auto:1}
setblock ~3 ~-3 ~1 minecraft:chain_command_block[facing=down,conditional=true] replace
data merge block ~3 ~-3 ~1 {Command:"fill ~ ~ ~ ~ ~2 ~ minecraft:bedrock replace", auto:1}


difficulty hard
fill ~4 ~ ~2 ~6 ~2 ~4 minecraft:bedrock replace
setblock ~5 ~1 ~2 minecraft:barrier replace
setblock ~5 ~1 ~3 minecraft:wither_skeleton_skull replace
setblock ~5 ~-1 ~1 minecraft:repeating_command_block[facing=down,conditional=false] replace
data merge block ~5 ~-1 ~1 {Command:"execute if block ~ ~1 ~ minecraft:wither_skeleton_skull run difficulty normal", auto:1}
setblock ~5 ~-2 ~1 minecraft:chain_command_block[facing=down,conditional=true] replace
data merge block ~5 ~-2 ~1 {Command:"fill ~ ~ ~ ~ ~1 ~ minecraft:bedrock replace", auto:1}


fill ~6 ~ ~2 ~8 ~2 ~4 minecraft:bedrock replace
setblock ~7 ~1 ~2 minecraft:barrier replace
setblock ~7 ~1 ~3 minecraft:purpur_block replace
setblock ~7 ~-1 ~1 minecraft:repeating_command_block[facing=down,conditional=false] replace
data merge block ~7 ~-1 ~1 {Command:"execute if block ~ ~1 ~ minecraft:purpur_block run fill ~ ~ ~ ~ ~ ~ minecraft:bedrock replace", auto:1}
setblock ~7 ~-2 ~1 minecraft:repeating_command_block[facing=down,conditional=false] replace
data merge block ~7 ~-2 ~1 {Command:"execute if block ~ ~1 ~ minecraft:bedrock run effect give @a minecraft:luck 6000 0 true", auto:1}


spreadplayers ~4 ~-5 1 5 false @a


fill ~-3 ~4 ~5 ~11 ~4 ~-14 minecraft:quartz_block replace
fill ~-2 ~5 ~4 ~10 ~5 ~-13 minecraft:quartz_block replace
fill ~ ~6 ~4 ~8 ~6 ~-13 minecraft:quartz_block replace
setblock ~-1 ~6 ~3 minecraft:torch replace
setblock ~-1 ~6 ~ minecraft:torch replace
setblock ~-1 ~6 ~-3 minecraft:torch replace
setblock ~-1 ~6 ~-6 minecraft:torch replace
setblock ~-1 ~6 ~-9 minecraft:torch replace
setblock ~-1 ~6 ~-12 minecraft:torch replace
setblock ~9 ~6 ~3 minecraft:torch replace
setblock ~9 ~6 ~ minecraft:torch replace
setblock ~9 ~6 ~-3 minecraft:torch replace
setblock ~9 ~6 ~-6 minecraft:torch replace
setblock ~9 ~6 ~-9 minecraft:torch replace
setblock ~9 ~6 ~-12 minecraft:torch replace
setblock ~4 ~7 ~3 minecraft:torch replace
setblock ~4 ~7 ~ minecraft:torch replace
setblock ~4 ~7 ~-3 minecraft:torch replace
setblock ~4 ~7 ~-6 minecraft:torch replace
setblock ~4 ~7 ~-9 minecraft:torch replace
setblock ~4 ~7 ~-12 minecraft:torch replace
fill ~4 ~1 ~-1 ~4 255 ~-1 minecraft:air replace
setblock ~4 ~-1 ~-1 minecraft:grass_block replace
