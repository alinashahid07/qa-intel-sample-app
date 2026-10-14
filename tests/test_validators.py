import pytest

from app.validators import is_valid_email


@pytest.mark.parametrize(
    "email",
    ["john@example.com", "john.doe+tag@example.co.uk", "user123@mail-server.org"],
)
def test_valid_emails_pass(email):
    assert is_valid_email(email)


@pytest.mark.parametrize("email", ["plainaddress", "missing@tld", "@nouser.com"])
def test_invalid_emails_fail(email):
    assert not is_valid_email(email)