from config import Config, DEFAULT_CONFIG
from desktopwallpaper import DesktopWallpaper


class Service():

    def __init__ (self):
        self.config = Config(default_config=DEFAULT_CONFIG)

        self.history_wallpapers = Config(section="HISTORY_WALLPAPERS", path_to_config_file=f'{self.config.PATH_TO_WALLPAPERS}')
