#edition solds count
java_edition=3000000
bedrock_edition=4000000
pocket_edition=4000000
xbox_360=22000000
minecraft_dungeons=25000000
minecraft_legends=3000000
#calculate the avarege solds
total_edition_solds=java_edition+bedrock_edition+pocket_edition+xbox_360+minecraft_dungeons+minecraft_legends
total_steam_solds=minecraft_dungeons+minecraft_legends
total_copies_sold=java_edition+bedrock_edition+pocket_edition
total_console_solds=xbox_360
print("total edition solds of minecraft:",total_edition_solds)
print("total steam solds of minecraft:",total_steam_solds)
print("total copies solds of minecraft:",total_copies_sold)
print("total console solds of minecraft:",total_console_solds)
print("average solds",total_console_solds/6)
#price and solds
solds_per_players=212000000
player_per_sold=java_edition//bedrock_edition//pocket_edition+xbox_360+minecraft_dungeons+minecraft_legends
print("total sold per person",sold_count)

#floor division introduction
sold_count=total