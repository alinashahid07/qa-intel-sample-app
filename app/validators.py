import re

from app.bugs import bug_active

EMAIL_PATTERN = re.compile(r"^[\w.+-]+@[\w-]+\.[\w.]+$")
STRICT_PATTERN = re.compile(r"^[a-z]+@[a-z]+\.com$")


def is_valid_email(email: str) -> bool:
    pattern = STRICT_PATTERN if bug_active("email_regex_too_strict") else EMAIL_PATTERN
    return bool(pattern.match(email))