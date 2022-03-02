from hashlib import md5
from pathlib import Path
from typing import Union
from json import loads, dumps, dump


class CachedFileManager:
    def __init__(self,
                 directory: Union[Path, str],
                 file_name_query: Union[Path, str]
                 ) -> None:
        self.__directory = Path(directory)
        self.__file_name_query = str(file_name_query)
        self.__cached_file_path = self.__build_cached_file_path()

    def __build_cached_file_path(self) -> Path:
        hashcode = md5(self.__file_name_query.encode('utf8')).hexdigest()
        return self.__directory/hashcode

    def is_file_exist(self) -> bool:
        return self.__cached_file_path.exists()

    def load_from_cache(self) -> str:
        return loads(self.__cached_file_path.read_text())

    def save_to_cache(self,
                      data: dict) -> None:
        self.__cached_file_path.parent.mkdir(parents=True, exist_ok=True)
        self.__cached_file_path.write_text(dumps(data))
