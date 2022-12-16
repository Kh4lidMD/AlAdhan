class RateLimitedException(Exception):
    """
    Exception raised when the API rate limit is exceeded, according to the
    API:
    
    `For the AlAdhan API in each region, each IP is allowed approximately 14 requests per second.`
    """
    pass

class BadRequestException(Exception):
    """Exception raised when a bad request is made to the API (e.g. invalid date)."""
    pass

class ServerErrorException(Exception):
    """
    This exception is raised when the API returns a 500 error (internal server error), 
    which is commonly happening in the Aladhan API for non-handled errors.
    """
    pass

class InvalidLocationException(Exception):
    """Exception raised when a invalid location is provided"""
    pass