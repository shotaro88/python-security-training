import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)

def authenticate(username: str, password: str, token: str):
    # ❌ Never log secrets or PII in plaintext
    logger.debug(f"Authenticating user={username} password={password} token={token}")
    # pretend to authenticate
    return username == "admin" and password == "password"

if __name__ == "__main__":
    authenticate("admin", "password", "FAKE-TOKEN-123")