import command
import os


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


def __info_desktop__(attr):
    import re
    from subprocess import run, PIPE
    output = run(['xrandr'], stdout=PIPE).stdout.decode()
    result = re.search(r'current (\d+) x (\d+)', output)
    width, height = map(int, result.groups()) if result else (1920, 1080)
    if attr == 'width':
        return width
    elif attr == 'height':
        return height
