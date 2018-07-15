gamerule commandBlockOutput falseteam leave @aclear @axp set @a 0 levelstp @a 7 202 7
fill -9 200 -9 23 210 23 minecraft:barrier hollow
fill -9 198 -9 23 200 23 minecraft:barrier replace
fill -9 210 -9 23 210 23 minecraft:air replace
fill 4 198 4 10 200 10 minecraft:bedrock replace
fill 6 199 6 8 199 8 minecraft:glowstone replace
fill 7 200 -8 7 200 22 minecraft:bedrock replace
fill -8 200 7 22 200 7 minecraft:bedrock replace
fill 5 200 -8 9 200 -5 minecraft:bedrock replace
fill 5 200 22 9 200 19 minecraft:bedrock replace
fill -8 200 5 -5 200 9 minecraft:bedrock replace
fill 22 200 5 19 200 9 minecraft:bedrock replace
fill 5 199 -4 9 199 -4 minecraft:glowstone replace
fill 5 199 18 9 199 18 minecraft:glowstone replace
fill -4 199 5 -4 199 9 minecraft:glowstone replace
fill 18 199 5 18 199 9 minecraft:glowstone replace
setblock 3 199 3 minecraft:glowstone
setblock 11 199 3 minecraft:glowstone
setblock 3 199 11 minecraft:glowstone
setblock 11 199 11 minecraft:glowstone
setblock 15 199 7 minecraft:glowstone
setblock -1 199 7 minecraft:glowstone
setblock 7 199 15 minecraft:glowstone
setblock 7 199 -1 minecraft:glowstone

setworldspawn 8 201 8
spawnpoint @a 7 201 7

fill 7 64 7 7 199 7 minecraft:air replace
fill 5 64 5 9 67 9 minecraft:barrier replace
fill 7 198 7 7 200 7 minecraft:barrier replace
fill 5 64 5 9 64 9 minecraft:bedrock replace
fill 6 65 6 8 65 8 minecraft:gold_block replace
setblock 7 66 7 minecraft:beacon replace
setblock 16 7 -2 minecraft:wall_torch[facing=west] replace


team add north "Gray Frost"
team modify north color gray 
team modify north nametagVisibility hideForOtherTeams 
team modify north seeFriendlyInvisibles true

team add south "Crimson Skull"
team modify south color dark_red
team modify south nametagVisibility hideForOtherTeams 
team modify south seeFriendlyInvisibles true

team add west "Sapphire Star"
team modify west color blue
team modify west nametagVisibility hideForOtherTeams 
team modify west seeFriendlyInvisibles true

team add east "Golden Sun"
team modify east color yellow
team modify east nametagVisibility hideForOtherTeams 
team modify east seeFriendlyInvisibles true


function cch:z__competition_scoreboard_init
scoreboard objectives setdisplay list deaths 
scoreboard objectives setdisplay belowName health
scoreboard objectives setdisplay sidebar score
fill 5 199 5 8 199 5 minecraft:hopper[facing=east]fill 9 199 5 9 199 8 minecraft:hopper[facing=south]fill 9 199 9 6 199 9 minecraft:hopper[facing=west]
fill 5 199 9 5 199 6 minecraft:hopper[facing=north]
data merge block 5 199 9 {Items:[{Slot:0b, id:"minecraft:brick", Count:1b}]}
data merge block 9 199 5 {Items:[{Slot:0b, id:"minecraft:brick", Count:1b}]}
setblock 7 199 4 minecraft:comparator[facing=south]
setblock 7 199 3 minecraft:command_block[facing=south]{Command:"execute as @a run function cch:z__competition_score_update"} replace
setblock 7 199 10 minecraft:comparator[facing=north]
setblock 7 199 11 minecraft:command_block[facing=north]{Command:"function cch:z__competition_spawn_update"} replace

setblock 7 200 -7 minecraft:repeating_command_block[facing=down,conditional=false]{Command:"team join north @a[x=5,y=199,z=-9,dx=4,dy=4,dz=4]", auto:1}
setblock 7 201 -7 minecraft:stone_pressure_plate replace
setblock 9 201 -5 minecraft:light_gray_banner[rotation=0]{Patterns:[{Pattern:"gra",Color:0}, {Pattern:"flo",Color:3}]} replace
setblock 5 201 -5 minecraft:light_gray_banner[rotation=0]{Patterns:[{Pattern:"gra",Color:0}, {Pattern:"flo",Color:3}]} replace
setblock 7 200 21 minecraft:repeating_command_block[facing=down,conditional=false]{Command:"team join south @a[x=5,y=199,z=19,dx=4,dy=4,dz=4]", auto:1}
setblock 7 201 21 minecraft:stone_pressure_plate replace
setblock 9 201 19 minecraft:red_banner[rotation=8]{Patterns:[{Pattern:"cre",Color:15}]} replace
setblock 5 201 19 minecraft:red_banner[rotation=8]{Patterns:[{Pattern:"cre",Color:15}]} replacesetblock -7 200 7 minecraft:repeating_command_block[facing=down,conditional=false]{Command:"team join west @a[x=-9,y=199,z=5,dx=4,dy=4,dz=4]", auto:1}
setblock -7 201 7 minecraft:stone_pressure_plate replace
setblock -5 201 9 minecraft:blue_banner[rotation=12]{Patterns:[{Pattern:"gra",Color:15}, {Pattern:"mr",Color:0}]} replace
setblock -5 201 5 minecraft:blue_banner[rotation=12]{Patterns:[{Pattern:"gra",Color:15}, {Pattern:"mr",Color:0}]} replace

setblock 21 200 7 minecraft:repeating_command_block[facing=down,conditional=false]{Command:"team join east @a[x=19,y=199,z=5,dx=4,dy=4,dz=4]", auto:1}
setblock 21 201 7 minecraft:stone_pressure_plate replace
setblock 19 201 9 minecraft:yellow_banner[rotation=4]{Patterns:[{Pattern:"flo",Color:1}, {Pattern:"mc",Color:0}]} replace
setblock 19 201 5 minecraft:yellow_banner[rotation=4]{Patterns:[{Pattern:"flo",Color:1}, {Pattern:"mc",Color:0}]} replace

