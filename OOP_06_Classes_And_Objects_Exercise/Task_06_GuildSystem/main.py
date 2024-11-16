from project.player import Player
from project.guild import Guild

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
player1 = Player("Peter", 50, 100)
print(player1.add_skill("ala-bala", 10))
print(player1.add_skill("kakskas", 15))
print(player1.add_skill("skfjje", 11))
guild1 = Guild("A1")
print(guild1.assign_player(player1))
print(guild1.guild_info())
