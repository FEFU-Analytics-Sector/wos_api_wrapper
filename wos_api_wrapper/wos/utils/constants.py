from pathlib import Path

if (Path.home()/".wos_api_wrapper").exists():
    BASE_PATH = Path.home()/".wos_api_wrapper"
else:
    BASE_PATH = Path.home()/".wos_api_wrapper"/"Wos"
DEFAULT_PATHS = {
    'QueryRetrieval': BASE_PATH/'query_retrieval',
    'ReferencesRetrieval': BASE_PATH/'references_retrieval',
}

if (Path.home()/".wos_api_wrapper").exists():
    CONFIG_FILE = Path.home()/".wos_api_wrapper"/"config.ini"
else:
    CONFIG_FILE = Path.home()/".wos_api_wrapper"/"config.ini"

API_URL = 'https://wos-api.clarivate.com/api/wos/'
URLS = {
    'UserQuerySearch': API_URL,
    'ArticleDetail': API_URL,
}

RETRIEVAL_MAX_RECORDS = 100
