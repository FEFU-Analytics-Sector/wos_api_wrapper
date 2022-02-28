from typing import Optional

from wos_api_wrapper.wos.superclasses import BaseWrapper
from wos_api_wrapper.wos.utils import URLS


class UserQuerySearch(BaseWrapper):
    def __init__(self,
                 query: str,
                 database_id: str,
                 first_record: int = 1,
                 records_count: int = 100,
                 api_key: Optional[str] = None,
                 **kwargs: str,
                 ) -> None:
        """Interaction with the Web of Science API Expanded. Search by user query.
                :param query: User query for requesting data.
                              The query consists of field tags and boolean operators.
                              Example: "CU=Poland AND PY=2020" (names of field tags and booleans are case insensitive)
                              The best way to make an query is to use the official Search Query Builder:
                              https://www.webofscience.com/wos/woscc/advanced-search.
                :param database_id: Database to search. Must be a valid database ID,
                                    one of the following: BCI/BIOABS/BIOSIS/CCC/DCI/DIIDW/MEDLINE/WOK/WOS/ZOOREC.
                                    WOK represents all databases.
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
        params = {
            "databaseId": database_id,
            "usrQuery": query,
            "count": records_count,
            "firstRecord": first_record,
            **kwargs}
        super(UserQuerySearch, self).__init__(api_url=URLS['UserQuerySearch'], api_key=api_key, params=params)

