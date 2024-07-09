import pytest
from POM.login import LoginPage


header =("username,password")
data = [("sahana","123"),("manasvi","456")]

@pytest.mark.xfail
@pytest.mark.parametrize(header,data)
def test_login(browser,username,password):
    login_obj=LoginPage(browser,username,password)
    login_obj.login()

