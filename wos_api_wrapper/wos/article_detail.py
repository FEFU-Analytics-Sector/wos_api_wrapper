from typing import Optional

from wos_api_wrapper.wos.superclasses import BaseWrapper
from wos_api_wrapper.wos.utils import URLS


class ArticleDetail(BaseWrapper):
    def __init__(self,
                 detail_type: str,
                 record_id: str,
                 database_id: str,
                 first_record: int = 1,
                 records_count: int = 100,
                 api_key: Optional[str] = None,
                 **kwargs: str,
                 ) -> None:
        """Interaction with the Web of Science API Expanded. Search by user query.
                :param detail_type: {"related", "references", "citing"}
                                    Type of detail request for article,
                                    see documentation and parameters for each one:
                                    https://api.clarivate.com/swagger-ui/?url=https%3A%2F%2Fdeveloper.clarivate.com%2Fapis%2Fwos%2Fswagger.
                :param record_id: Primary item id to be searched, ex: WOS:000270372400005.
                                  Cannot be null or an empty string.
                :param database_id: Database to search. Must be a valid database ID,
                                    one of the following: BCI/DRCI/WOK/WOS.
                                    WOK represents all databases.
                                    For "citing" available only WOS database
                :param records_count: Number of records to return, must be 0-100.
                :param first_record: Specific record, if any within the result set to return.
                                     Cannot be less than 1 and greater than 100000.
                                     The search can return many records, this number can be more than 100
                                     (the maximum number of entries in the response).
                                     The first_record parameter specifies which record to return the response from.
                :param api_key: Your WOS api key. It is not recommended to pass this parameter,
                                it is better to enter the api key into the command prompt if api wrapper requests it.
                                Anyway, a configuration file will be created or overwritten locally,
                                in which the key will be saved for future use.
                :param kwargs: Keywords passed on as query parameters. Must contain
                               fields and values mentioned in the API specification at
                               https://api.clarivate.com/swagger-ui/?url=https%3A%2F%2Fdeveloper.clarivate.com%2Fapis%2Fwos%2Fswagger.
                Raises
                ------
                WosQueryError

                ValueError
                    If any of the parameters above is not one of the allowed values.
                Notes
                -----
                Official documentation https://developer.clarivate.com/apis/wos
        """
        if detail_type not in {"related", "references", "citing"}:
            raise KeyError
        params = {
            "databaseId": database_id,
            "uniqueId": record_id,
            "count": records_count,
            "firstRecord": first_record,
            **kwargs}
        super(ArticleDetail, self).__init__(api_url=URLS['ArticleDetail']+detail_type, api_key=api_key, params=params)

