# This file is © TheBloodyscreen
# It was created as part of the Minecraft Controller project in May of 2019
# If you want to use all or part of the code in this file,
# please contact JayDee@TheBloodyScreen.com
from mcrcon import MCRcon
from config.config import config
from bloodyterminal import btext
from mcstatus import MinecraftServer

# inits and stuffs
colorCodes = ["§1", "§4", "§c", "§6", "§e", "§2", "§a", "§b", "§3", "§9", "§d", "§5", "§f", "§7", "§8", "§0", "§r",
              "§l", "§o", "§n", "§m", "§k"]
server = MinecraftServer(config["serverIP"], config["serverPORT"])
status = server.status()
description = status.description["text"]
for color in colorCodes:  # removing stylization from minecraft motd for better readability
    description = description.replace(color, "")
version = status.version.name
ping = server.ping()
image = status.favicon

btext.debug(description)
btext.debug(version)
btext.debug(ping)
btext.debug(image)


def executeCommand(command):
    with MCRcon(config['serverIP'], config['rconPass']) as mcr:
        response = mcr.command("command")
        btext.debug(response)


if __name__ == '__main__':
    pass
