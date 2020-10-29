import command
import os
from helpers import __info_desktop__

class Service:

    _wallpapersList = []
    _config = {
        'wallpapersListLimit': 10,
        'pathToWallpapers': f'{os.getenv("HOME")}/wallpapers',
        'width': __info_desktop__("width"),
        'height': __info_desktop__("height"),
        'search_filter': []
    }

    def call(self, command: command.Command):
        _command = command(self)
        _command.execute()


