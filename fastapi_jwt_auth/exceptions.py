class AuthJWTException(Exception):
    """
    Base except which all fastapi_jwt_auth errors extend
    """
    pass

class InvalidHeaderError(AuthJWTException):
    """
    An error getting header information from a request
    """
    def __init__(self,status_code: int, message: str):
        self.status_code = status_code
        self.message = message

class MissingHeaderError(AuthJWTException):
    """
    Error raised when <HeaderName> not found in the header
    """
    def __init__(self,status_code: int, message: str):
        self.status_code = status_code
        self.message = message

class JWTDecodeError(AuthJWTException):
    """
    An error decoding a JWT
    """
    def __init__(self,status_code: int, message: str):
        self.status_code = status_code
        self.message = message

class RevokedTokenError(AuthJWTException):
    """
    Error raised when a revoked token attempt to access a protected endpoint
    """
    def __init__(self,status_code: int, message: str):
        self.status_code = status_code
        self.message = message

class AccessTokenRequired(AuthJWTException):
    """
    Error raised when a valid, non-access JWT attempt to access an endpoint
    protected by jwt_required, jwt_optional, fresh_jwt_required
    """
    def __init__(self,status_code: int, message: str):
        self.status_code = status_code
        self.message = message

class RefreshTokenRequired(AuthJWTException):
    """
    Error raised when a valid, non-access JWT attempt to access an endpoint
    protected by jwt_refresh_token_required
    """
    def __init__(self,status_code: int, message: str):
        self.status_code = status_code
        self.message = message

class FreshTokenRequired(AuthJWTException):
    """
    Error raised when a valid, non-fresh JWT attempt to access an endpoint
    protected by fresh_jwt_required
    """
    def __init__(self,status_code: int, message: str):
        self.status_code = status_code
        self.message = message