from projectGUILDSYSTEM06.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.name in self.players:
            return f"Player {player.name} is already in the guild."
        elif not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            player.players.append(player.name)
            self.players.append(player.name)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if player_name not in self.players:
            return f"Player {player_name} is not in the guild."
        Player.guild = "Unaffiliated"
        self.players.remove(player_name)
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for _ in range(len(self.players)):
            result += Player.player_info(player)
        return result


player = Player("Pesho", 90, 90)
guild = Guild("GGXrd")
print(guild.assign_player(player))
print(guild.assign_player(player))

