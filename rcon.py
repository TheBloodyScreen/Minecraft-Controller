# This file is © TheBloodyscreen
# It was created as part of the Minecraft Controller project in May of 2019
# If you want to use all or part of the code in this file,
# please contact JayDee@TheBloodyScreen.com

import inspect
from config import config
from mcrcon import MCRcon
from bloodyterminal import btext


class Rcon:

    def __init__(self):
        pass

    @staticmethod
    def ban(target, reason):
        try:
            with MCRcon(config['serverIP'], config['rconPASS']) as mcr:
                response = mcr.command("ban " + target + " " + reason)
                btext.info(response)
        except:
            btext.error("Something fucky happened while trying to use {}".format(inspect.stack()[0][3]))

    @staticmethod
    def banip(target, reason):
        try:
            with MCRcon(config['serverIP'], config['rconPASS']) as mcr:
                response = mcr.command("ban-ip " + target + " " + reason)
                btext.info(response)
        except:
            btext.error("Something fucky happened while trying to use {}".format(inspect.stack()[0][3]))

    @staticmethod
    def banlist():
        try:
            with MCRcon(config['serverIP'], config['rconPASS']) as mcr:
                response = mcr.command("banlist")
                btext.info(response)
        except:
            btext.error("Something fucky happened while trying to use {}".format(inspect.stack()[0][3]))

    @staticmethod
    def datapack(*args):
        try:
            with MCRcon(config['serverIP'], config['rconPASS']) as mcr:
                if len(args) == 1:
                    response = mcr.command("datapack " + args[0])
                    btext.debug(args)
                    btext.debug("1")
                    btext.info(response)
                elif len(args) == 2:
                    response = mcr.command("datapack " + args[0] + ' "' + args[1] + '"')
                    btext.debug(args)
                    btext.debug("2")
                    btext.info(response)
                elif len(args) == 3:
                    response = mcr.command("datapack " + args[0] + ' "' + args[1] + '" ' + args[2])
                    btext.debug(args)
                    btext.debug("3")
                    btext.info(response)
                elif len(args) == 4:
                    response = mcr.command("datapack " + args[0] + ' "' + args[1] + '" ' + args[2] + ' "' + args[3] + '"')
                    btext.debug(args)
                    btext.debug("4")
                    btext.info(response)
        except Exception as e:
            btext.debug(e)
            btext.error("Something fucky happened while trying to use {}".format(inspect.stack()[0][3]))

    @staticmethod
    def pardon(target):
        try:
            with MCRcon(config['serverIP'], config['rconPASS']) as mcr:
                response = mcr.command("pardon " + target)
                btext.info(response)
        except:
            btext.error("Something fucky happened while trying to use {}".format(inspect.stack()[0][3]))

    @staticmethod
    def pardonip(target):
        try:
            with MCRcon(config['serverIP'], config['rconPASS']) as mcr:
                response = mcr.command("pardon-ip " + target)
                btext.info(response)
        except:
            btext.error("Something fucky happened while trying to use {}".format(inspect.stack()[0][3]))

    @staticmethod
    def say(message):
        try:
            with MCRcon(config['serverIP'], config['rconPASS']) as mcr:
                response = mcr.command("say " + message)
                btext.success('Successfully sent "' + message + '" to the Server!')
        except:
            btext.error("Something fucky happened while trying to use {}".format(inspect.stack()[0][3]))

    @staticmethod
    def whitelist(operator, username):
        try:
            with MCRcon(config['serverIP'], config['rconPASS']) as mcr:
                response = mcr.command("whitelist " + operator + " " + username)
                btext.debug(response)
        except:
            btext.error("Something fucky happened while trying to use {}".format(inspect.stack()[0][3]))
