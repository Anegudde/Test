# content of ./test_smtpsimple.py
import pytest

@pytest.fixture
def smtp():
    import smtplib
    return smtplib.SMTP("google.com")

def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    print response
    assert response == 100
    assert 1 # for demo purposes
