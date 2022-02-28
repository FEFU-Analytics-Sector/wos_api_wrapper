import configparser
from typing import Optional

from wos_api_wrapper.wos.utils.constants import DEFAULT_PATHS, CONFIG_FILE
from wos_api_wrapper.wos.utils.patterns import Singleton


class ConfigManager(metaclass=Singleton):
    def __init__(self):
        """A class intended to interact with a configuration file

        Notes
        -----
        """

        self.api_key = None

    def get_or_create_config(self,
                             api_key: Optional[str] = None,
                             ) -> configparser.ConfigParser:
        """Initiates process to create or read configuration file.
        :param api_key : WOS api key. If the key has not been passed,
                         it will be requested via the command prompt
        """

        config = configparser.ConfigParser()
        config.optionxform = str
        if not self.is_config_exists():
            print(f"Config file does not exist.")
            print(f"Creating config file at {CONFIG_FILE} with default paths...")
            config = self.__create_config(api_key)
        else:
            print(f"Config file exists at '{CONFIG_FILE}', reading...")
            config.read(CONFIG_FILE)

        return config

    @staticmethod
    def is_config_exists() -> bool:
        return CONFIG_FILE.exists()

    def __create_config(self,
                        api_key: Optional[str] = None,
                        ) -> configparser.ConfigParser:
        config = configparser.ConfigParser()
        config.optionxform = str
        config.add_section('Directories')
        for api, path in DEFAULT_PATHS.items():
            config.set('Directories', api, str(path))

        config.add_section('Authentication')
        if api_key is None:
            prompt_key = "Please enter your API Key:\n"
            api_key = input(prompt_key)
        config.set('Authentication', 'APIKey', api_key)

        CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_FILE, "w") as ouf:
            config.write(ouf)
        print(f"Configuration file successfully created at {CONFIG_FILE}\n")
        return config
