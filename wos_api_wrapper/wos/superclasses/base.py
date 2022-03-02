import requests
from requests.structures import CaseInsensitiveDict
from typing import Dict, Optional
from collections import OrderedDict

from wos_api_wrapper.wos.utils.cache_manager import CacheManager
from wos_api_wrapper.wos.utils.config_manager import ConfigManager
from wos_api_wrapper.wos.utils import URLS, DEFAULT_PATHS


class BaseWrapper:
    def __init__(self,
                 endpoint_name: str,
                 download: bool = True,
                 use_cache: bool = True,
                 params: dict = dict(),
                 api_key: Optional[str] = None,
                 ) -> None:
        """Class intended as base class for superclasses.

        :param endpoint_name: Api endpoint keyword used in constants.
        :param download: If True, then the response will be cached locally for future use.
                                 To get cached responses for previous requests create a new object of this class
                                 with the same parameters and set use_cache=True.
                                 Then instead of sending a request to the api, cache data will be returned
        :param use_cache: If True, then the response will be loaded from the cache
                          if it was previously downloaded.
                          Attention! The old version of the loaded response may not correspond
                          to the current Web of Science data.
        :param params: Query params. Must contain
                        fields and values mentioned in the API specification at
                        https://api.clarivate.com/swagger-ui/?url=https%3A%2F%2Fdeveloper.clarivate.com%2Fapis%2Fwos%2Fswagger.
        :param api_key: Key to access WOS api.
        """

        self.__config_manager = ConfigManager()
        self.__config = self.__config_manager.get_or_create_config(api_key)

        self.__params = params
        self.__download = download
        self.__use_cache = use_cache
        if use_cache or download:
            self.__cache_manager = CacheManager(
                DEFAULT_PATHS[endpoint_name],
                self.__get_sorted_params_string()
            )

        self.__api_url = URLS[endpoint_name]
        self.__request_headers = self.__prepare_request_headers()
        self.__request_params = params

        self.__response = None
        self.__response = self.__get_response()
        self.__response_headers = self.get_response_headers()

    def __prepare_request_headers(self) -> Dict:
        return {
            'X-APIKey': self.__config.get('Authentication', 'APIKey')
        }

    def __get_response(self) -> Optional[requests.Response]:
        if self.__cache_manager.is_file_exist() and self.__use_cache:
            return None
        elif self.__response is None:
            return requests.get(
                url=self.__api_url,
                headers=self.__request_headers,
                params=self.__request_params
            )

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

    def __get_sorted_params_string(self):
        ordered_params = OrderedDict(sorted(self.__params.items()))
        return str(ordered_params)
