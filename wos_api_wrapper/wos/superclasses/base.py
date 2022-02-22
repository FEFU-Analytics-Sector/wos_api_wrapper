"""Basic class object for superclasses."""

from typing import Dict, Optional


class BaseWrapper:
    def __init__(self,
                 wos_api_key: str,
                 ) -> None:
        """Class intended as base class for superclasses.

        :param wos_api_key: Key to access WOS api.
        """
        self.__wos_api_key = wos_api_key
        self.__request_headers = self.prepare_request_headers()

    def prepare_request_headers(self) -> Dict:
        return {
            'X-APIKey': self.__wos_api_key
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
