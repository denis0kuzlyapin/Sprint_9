import pytest
from pages.header_auth import HeaderAuth


@pytest.fixture(params=["chrome"])
def driver(request):
    from helpers import BrowserFactory

    driver = BrowserFactory.get_driver(request.param, headless=False)
    driver.delete_all_cookies()
    yield driver
    driver.quit()


@pytest.fixture
def logout_after_test(driver):
    yield
    try:
        header_auth = HeaderAuth(driver)
        header_auth.logout()
    except:
        pass
