import pytest
from POM import signin
@pytest.mark.sanity
@pytest.mark.parametrize("data",["india"])
def test_signin(drivers,data):
    sign_obj = signin.Signin(drivers)
    sign_obj.click_on_signin(data)
    assert "Create an Account" in drivers.page_source, "Sign in page is not loaded correctly"
    assert "Create an Account" in drivers.page_source,"Account creation page is not loaded"
    assert "Country/Region" in drivers.page_source,"Country selection is not successful"

# @pytest.mark.parametrize("data",["2"])
# def test_dob(drivers,data):
#     sign_obj = signin.Signin(drivers)
#     sign_obj.click_on_signin_date(data)
