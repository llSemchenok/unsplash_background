import os
import re
from subprocess import run, PIPE
from urllib.request import urlretrieve


__NAME_PHOTO__ = 'photo.jpeg'
__PATH_TO_PHOTO__ = f'{os.path.abspath(__NAME_PHOTO__)}'

class DesktopWallpaper:
    
    def __init__ (self, config):
        self.width,self.height = (kwargs['width'],kwargs['height']) if ('width' in kwargs and 'height' in kwargs) else self.__info_desktop__()
        self.search_filter = kwargs['filter'] if 'filter' in kwargs else []
        if 'auto' in kwargs:
            if kwargs['auto'] == False: 
                self.set_desktop_background(self.width, self.height, *self.search_filter)
        else: 
            self.set_desktop_background(self.width, self.height, *self.search_filter)

    def __get_photo__(self, width, height,*search_filter):
        url = f'https://source.unsplash.com/{self.width}x{self.height}' if not search_filter else f'https://source.unsplash.com/{self.width}x{self.height}/?{",".join(search_filter)}'
        urlretrieve(url, __PATH_TO_PHOTO__)
        print (url)
        return 200

    def __info_desktop__(self):
        output = run(['xrandr'], stdout=PIPE).stdout.decode()
        result = re.search(r'current (\d+) x (\d+)', output)
        width, height = map(int, result.groups()) if result else (1920, 1080) 
        return width, height

    def set_desktop_background(self, width, height, *search_filter):
        if self.__get_photo__(width,height,*search_filter) == 200:
            os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{__PATH_TO_PHOTO__}")
