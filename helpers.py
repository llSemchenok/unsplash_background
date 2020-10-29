import os

def __info_desktop__(attr):
    import re
    from subprocess import run, PIPE

    output = run(['xrandr'], stdout=PIPE).stdout.decode()
    result = re.search(r'current (\d+) x (\d+)', output)
    width, height = map(int, result.groups()) if result else (1920, 1080) 
    if attr == "width":
        return width
    elif attr == 'height':
        return height
    else: 
        return width, height