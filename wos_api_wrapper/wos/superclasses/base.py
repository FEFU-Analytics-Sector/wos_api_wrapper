import requests
from requests.structures import CaseInsensitiveDict

from wos_api_wrapper.wos.utils.config_manager import ConfigManager
from typing import Dict, Optional


class BaseWrapper:
    def __init__(self,
                 api_url: str,
                 params: dict = {},
                 api_key: Optional[str] = None,
                 ) -> None:
        """Class intended as base class for superclasses.

        :param api_url: Api endpoint.
        :param params: Query params. Must contain
                        fields and values mentioned in the API specification at
                        https://api.clarivate.com/swagger-ui/?url=https%3A%2F%2Fdeveloper.clarivate.com%2Fapis%2Fwos%2Fswagger.
        :param api_key: Key to access WOS api.
        """

        self.__config_manager = ConfigManager()
        self.__config = self.__config_manager.get_or_create_config(api_key)

        self.__api_url = api_url
        self.__request_headers = self.__prepare_request_headers()
        self.__request_params = params

        self.__response = None
        self.__response_headres = None

    def __prepare_request_headers(self) -> Dict:
        return {
            'X-APIKey': self.__config.get('Authentication', 'APIKey')
        }

    def __get_response(self) -> requests.Response:
        if self.__response is None:
            self.__response = requests.get(
                url=self.__api_url,
                headers=self.__request_headers,
                params=self.__request_params
            )
        return self.__response

    def get_row_results(self) -> str:
        """Method for getting json-encoded content of a response.

        Returns
        -------
        result : str
                 The json-encoded content of a response, if any.
        """
        result = self.__get_response().json()
        return result

    def get_request_per_second_remaining_quota(self) -> Optional[str]:
        """Method for getting remaining request quota per second.

        Returns
        -------
        remaining_quota : Optional[str]
                          Remaining requests per current second.
        """
        try:
            remaining_quota = self.get_response_headers()['X-REQ-ReqPerSec-Remaining']
        except AttributeError:
            remaining_quota = None
        return remaining_quota

    def get_response_headers(self) -> CaseInsensitiveDict[str]:
        """Method for getting full response headers.

        Returns
        -------
        response.headers : CaseInsensitiveDict[str]
                           response headers.
        """
        response = self.__get_response()
        return response.headers
