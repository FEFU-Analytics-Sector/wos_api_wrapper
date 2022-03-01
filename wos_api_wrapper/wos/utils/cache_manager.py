from hashlib import md5
from pathlib import Path
from typing import Union
from json import loads, dumps


class CacheManager:
    def __init__(self,
                 directory: Union[Path, str],
                 file_name_query: Union[Path, str]
                 ) -> None:
        self.__directory = Path(directory)
        self.__file_name_query = str(file_name_query)
        self.__cached_file_path = self.__get_cached_file_path()

    def __get_cached_file_path(self) -> Path:
        hashcode = md5(self.__file_name_query.encode('utf8')).hexdigest()
        return self.__directory/hashcode

    def is_file_exist(self) -> bool:
        return self.__cached_file_path.exists()

    def load_from_cache(self) -> str:
        return loads(self.__cached_file_path.read_text())

    def save_to_cache(self,
                      _json: str) -> None:
        self.__cached_file_path.write_text(_json)
