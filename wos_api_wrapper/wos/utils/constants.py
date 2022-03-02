from pathlib import Path

BASE_PATH = Path.home()/".wos_api_wrapper"/"cache"
DEFAULT_PATHS = {
    "UserQuerySearch": BASE_PATH/"user_query_search",
    "ArticleDetail_citing": BASE_PATH/"article_detail"/"citing",
    "ArticleDetail_related": BASE_PATH/"article_detail"/"related",
    "ArticleDetail_references": BASE_PATH/"article_detail"/"references",
}

CONFIG_FILE = Path.home()/".wos_api_wrapper"/"config.ini"

API_URL = "https://wos-api.clarivate.com/api/wos/"
URLS = {
    "UserQuerySearch": API_URL,
    "ArticleDetail_citing": API_URL + "citing/",
    "ArticleDetail_related": API_URL + "related/",
    "ArticleDetail_references": API_URL + "references/",
}

RETRIEVAL_MAX_RECORDS = 100
