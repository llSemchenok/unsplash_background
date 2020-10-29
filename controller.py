from service import Service
from command import SetDesktopWallpaper
from photolist import PhotoList


class Controller:

    _service = Service()

    def setConfigAttr(self, name, value):
        self._service._config.update({
            name: value
        })

    def setWallpaperDesktop(self):
        self._service.call(SetDesktopWallpaper)
