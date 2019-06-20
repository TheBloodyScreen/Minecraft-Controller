# This file is © TheBloodyscreen
# It was created as part of the Minecraft Controller project in May of 2019
# If you want to use all or part of the code in this file,
# please contact JayDee@TheBloodyScreen.com
from mcrcon import MCRcon
from config import config
from bloodyterminal import btext
from mcstatus import MinecraftServer
from rcon import Rcon

# inits and stuffs
colorCodes = ["§1", "§4", "§c", "§6", "§e", "§2", "§a", "§b", "§3", "§9", "§d", "§5", "§f", "§7", "§8", "§0", "§r",
              "§l", "§o", "§n", "§m", "§k"]    # list of every available stylization for removal later
server = MinecraftServer(config["serverIP"], config["serverPORT"])
status = server.status()
description = status.description["text"]
for color in colorCodes:  # removing stylization from minecraft motd for better readability
    description = description.replace(color, "")
ping = server.ping()
image = status.favicon
version = status.version.name
worldName = server.query().map
playersMax = server.query().players.max
playersOnline = server.query().players.names
playersOnlineAmount = server.query().players.online


if __name__ == '__main__':
    pass
