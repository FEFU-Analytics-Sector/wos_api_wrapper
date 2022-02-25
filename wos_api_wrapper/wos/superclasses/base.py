from wos_api_wrapper.wos.utils.config_manager import ConfigManager
from typing import Dict, Optional


class BaseWrapper:
    def __init__(self,
                 api_key: Optional[str] = None,
                 ) -> None:
        """Class intended as base class for superclasses.

        :param wos_api_key: Key to access WOS api.
        """
        self.__request_headers = self.prepare_request_headers()
        self.__config_manager = ConfigManager()
        self.__config = self.__config_manager.get_or_create_config(api_key)

    def prepare_request_headers(self) -> Dict:
        return {
            'X-APIKey': self.__config.get('Authentication', 'APIKey')
        }

    def get_request_per_second_remaining_quota(self) -> Optional[str]:
        """Return number of remaining requests per second
        for the current key.
        """
        try:
            return self.__response_headres['X-REQ-ReqPerSec-Remaining']
        except AttributeError:
            return None

    def get_response_header(self) -> Dict:
        """Return response headers as dictionary.
        """
        return self.__response_headres
