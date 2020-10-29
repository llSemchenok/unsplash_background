import argparse
from controller import Controller

parser = argparse.ArgumentParser(
    description='Utility to update desktop wallpaper.')
# parser.add_argument('--screen', '-s', dest='screen', action="extend", nargs="+", type=int)
parser.add_argument('--filter', '-f', dest='filter', action="extend",
                    nargs="+")

args = parser.parse_args()


if __name__ == "__main__":
    app = Controller()

    if args.filter != None:
        app.setConfigAttr('search_filter', args.filter)

    app.setWallpaperDesktop()
