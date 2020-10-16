import os
import configparser


CONFIG_PATH = f'{os.path.abspath(os.path.dirname(__file__))}'

DEFAULT_CONFIG = {
            'PATH_TO_WALLPAPERS': f'{os.getenv("HOME")}/wallpapers',
            'KEY_WORLD': []
        }


class Config():
    def __init__(self, path_to_config_file=CONFIG_PATH, section="DEFAULT", default_config={}, filename='conf'):
        self.__dict__['filename'] = filename
        self.__dict__['__config__'] = configparser.ConfigParser()
        self.__dict__['default_config'] = default_config
        self.__dict__['section'] = section
        self.__dict__['path_to_config_file'] = path_to_config_file
        self.__load__()

    def __load__(self):
        if not os.path.exists(f'{self.path_to_config_file}/{self.filename}'):
            self.__create__()
        else:
            self.__config__.read(self.path_to_config_file)

    def __getattr__(self, name):
        return self.__config__.get(self.section, name) if not name in self.__dict__ else self.__dict__[name]

    def __setattr__(self, name, value):
        self.__config__.set(self.section, name, str(value)) 
        self.__save__()

    def __delattr__(self, name):
        self.__config__.remove_option(self.section, name)
        self.__save__()

    def __create__(self):
        self.__makeDefaultConfig__()
        self.__save__()

    def __save__(self):
        try:
            with open(f'{self.path_to_config_file}/{self.filename}', 'w') as configfile:
                self.__config__.write(configfile)
        except FileNotFoundError as identifier:
            if not os.path.exists(self.path_to_config_file): 
                os.makedirs(self.path_to_config_file)
                self.__save__()

    def __makeDefaultConfig__(self):
        self.__config__[self.section] = self.default_config