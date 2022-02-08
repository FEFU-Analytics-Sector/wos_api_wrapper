from os import environ
from pathlib import Path

# Paths for cached files
if (Path.home()/".scopus").exists():
    BASE_PATH = Path.home()/".scopus"
else:
    BASE_PATH = Path.home()/".pybliometrics"/"Scopus"
DEFAULT_PATHS = {
    'QueryRetrieval': BASE_PATH/'query_retrieval',
    'ReferencesRetrieval': BASE_PATH/'references_retrieval',
}


# Configuration file location
if 'PYB_CONFIG_FILE' in environ:
    CONFIG_FILE = Path(environ['PYB_CONFIG_FILE'])
else:
    if (Path.home()/".scopus").exists():
        CONFIG_FILE = Path.home()/".scopus"/"config.ini"
    else:
        CONFIG_FILE = Path.home()/".pybliometrics"/"config.ini"

# URLs for all classes
API_URL = 'https://wos-api.clarivate.com/api/wos/'
URLS = {
    'QueryRetrieval': API_URL,
    'ReferencesRetrieval': API_URL + '/references',
}

# Limits for got data
RETRIEVAL_MAX_RECORDS = 100
