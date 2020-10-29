from __future__ import annotations
from abc import ABC, abstractmethod
from queue import Queue
from time import sleep
from datetime import datetime
import os
from urllib.request import urlretrieve
import asyncio


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class GetPhoto(Command):

    def __init__(self, service: Service) -> None:
        self._service = service
        self._width = self._service._config["width"]
        self._height = self._service._config["height"]
        self._search_filter = self._service._config['search_filter']

    def execute(self) -> None:
        asyncio.run(self.__getPhoto__())

    async def __getPhoto__(self) -> None:
        path_to_save = f'{self._service._config["pathToWallpapers"]}/{str(datetime.now())}.jpeg'
        url = f'https://source.unsplash.com/{self._width}x{self._height}' if not self._search_filter else f'https://source.unsplash.com/{self._width}x{self._height}/?{",".join(self._search_filter)}'
        urlretrieve(url, path_to_save)
        self._service._wallpapersList.append(str(path_to_save))


class SetDesktopWallpaper(Command):
    def __init__(self, service: Service):
        self._service = service
        self._service.call(CheckWallpapersList)

    def execute(self):
        _path_to_photo = f'{self._service._config["pathToWallpapers"]}/wallpaperSet.jpeg'
        os.rename(
            f'{self._service._config["pathToWallpapers"]}/{self._service._wallpapersList.pop()}', _path_to_photo)
        try:
            os.system(
                f"gsettings set org.gnome.desktop.background picture-uri file://{_path_to_photo}")
        except Exception as identifier:
            return identifier


class ConfigInit(Command):
    def __init__(self, service: Service, name: str, value: str):
        self._service = service
        self._name = name
        self._value = value

    def execute(self):
        if self._name in self._service._config:
            self._service._config[self._name] = self._value
        else:
            return "Error name"


class CheckWallpapersList(Command):
    def __init__(self, service: Service):
        self._service = service

    def execute(self):
        self.getWallpapersFromFolder()
        if len(self._service._wallpapersList) < self._service._config['wallpapersListLimit']:
            self.addedList()
        self._service._wallpapersList.sort()

    def getWallpapersFromFolder(self):
        wallpapers = os.listdir(self._service._config['pathToWallpapers'])
        for i in wallpapers:
            if i != "wallpaperSet.jpeg":
                self._service._wallpapersList.append(i)

    def addedList(self):
        count = self._service._config['wallpapersListLimit'] - \
            len(self._service._wallpapersList)
        for i in range(count):
            sleep(3)
            self._service.call(GetPhoto)
