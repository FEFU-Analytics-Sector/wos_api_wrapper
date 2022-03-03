class WosApiWrapperException(Exception):
    """Base class for exceptions in Wos."""


class WosError(WosApiWrapperException):
    """Exception for a serious error in Wos."""


class WosQueryError(WosApiWrapperException):
    """Exception for problems related to Wos queries."""


class WosHtmlError(WosApiWrapperException):
    """Wrapper for exceptions raised by requests."""


class Wos400Error(WosHtmlError):
    """Raised if a query yields a 400 error (Bad Request for url)."""


class Wos401Error(WosHtmlError):
    """Raised if a query yields a 401 error (Unauthorized for url)."""


class Wos403Error(WosHtmlError):
    """Raised if a query yields a 403 error (Forbidden for url)."""


class Wos404Error(WosHtmlError):
    """Raised if a query yields a 404 error (Not Found for url)."""


class Wos413Error(WosHtmlError):
    """Raised if a query yields a 413 error (Request Entity Too
    Large for url).
    """


class Wos414Error(WosHtmlError):
    """Raised if a query yields a 414 error (Request-URI Too Large for url)."""


class Wos429Error(WosHtmlError):
    """Raised if a query yields a 429 error (Throttle error)."""


class Wos500Error(WosHtmlError):
    """Raised if a query yields a 500 error (Internal Server Error for url)."""


class Wos502Error(WosHtmlError):
    """Raised if a query yields a 502 error (Bad gateway for url)."""


class Wos504Error(WosHtmlError):
    """Raised if a query yields a 504 error (Gateway Time-out for url)."""


ERRORS_DICT = {
    400: Wos400Error,
    401: Wos401Error,
    403: Wos403Error,
    404: Wos404Error,
    413: Wos413Error,
    414: Wos414Error,
    429: Wos429Error,
    500: Wos500Error,
    502: Wos502Error,
}
