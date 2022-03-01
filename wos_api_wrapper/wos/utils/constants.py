from pathlib import Path

BASE_PATH = Path.home()/".wos_api_wrapper"/"cache"
DEFAULT_PATHS = {
    'UserQuerySearch': BASE_PATH/'user_query_search',
    'ArticleDetail': BASE_PATH/'article_detail',
}

CONFIG_FILE = Path.home()/".wos_api_wrapper"/"config.ini"

API_URL = 'https://wos-api.clarivate.com/api/wos/'
URLS = {
    'UserQuerySearch': API_URL,
    'ArticleDetail': API_URL,
}

RETRIEVAL_MAX_RECORDS = 100
