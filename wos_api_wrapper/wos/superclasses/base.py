import requests
from typing import Dict, Optional
from collections import OrderedDict
from simplejson import JSONDecodeError

from wos_api_wrapper.wos.utils.cache_manager import CachedFileManager
from wos_api_wrapper.wos.utils.config_manager import ConfigManager
from wos_api_wrapper.wos.utils import URLS, DEFAULT_PATHS
from wos_api_wrapper.wos.utils.exception import ERRORS_DICT


class BaseWrapper:
    def __init__(self,
                 endpoint_name: str,
                 download: bool = True,
                 use_cache: bool = True,
                 params: dict = dict({}),
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

        self.__config = ConfigManager().get_or_create_config(api_key)

        self.__params = params
        self.__download = download
        self.__use_cache = use_cache
        self.__api_url = URLS[endpoint_name]
        if use_cache or download:
            self.__cache_manager = CachedFileManager(
                DEFAULT_PATHS[endpoint_name],
                self.__get_sorted_params_string()
            )

        self.__response_data = {}
        self.__fill_response_data()

        if download:
            self.__save_to_cache_response_data()

    def __get_sorted_params_string(self):
        ordered_params = OrderedDict(sorted(self.__params.items()))
        return str(ordered_params)

    def __fill_response_data(self) -> None:
        if self.__cache_manager.is_file_exist() and self.__use_cache:
            self.__response_data = self.__cache_manager.load_from_cache()
        else:
            response = self.__make_request()
            self.__response_data['headers'] = dict(response.headers)
            self.__response_data['content_json'] = response.json()

    def __make_request(self) -> requests.Response:
        response = requests.get(
            url=self.__api_url,
            headers=self.__prepare_request_headers(),
            params=self.__params
        )
        self.__check_status_code(response)
        return response

    def __check_status_code(self,
                            response: requests.Response):
        if response.status_code != 200:
            try:
                error_exception = ERRORS_DICT[response.status_code]
                try:
                    message = response.json()['message']
                except (JSONDecodeError, KeyError):
                    message = ""
                raise error_exception(message)
            except KeyError:
                response.raise_for_status()

    def __prepare_request_headers(self) -> Dict:
        return {
            'X-APIKey': self.__config.get('Authentication', 'APIKey')
        }

    def __save_to_cache_response_data(self) -> None:
        if not self.__cache_manager.is_file_exist() or not self.__use_cache:
            self.__cache_manager.save_to_cache(data=self.__response_data)

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

    def get_response_headers(self) -> dict:
        """Method for getting full response headers.

        Returns
        -------
        response.headers : CaseInsensitiveDict[str]
                           response headers.
        """
        return self.__response_data['headers']

    def get_raw_content_json(self) -> dict:
        """Method for getting json-decoded content of a response.

        Returns
        -------
        result : dict
                 The json-decoded content of a response.
        """
        result = self.__response_data['content_json']
        return result
