import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    driver = webdriver.Edge()
    print("--------------launching Edge browser----------------")
    driver.get("https://admin-demo.nopcommerce.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

# def pytest_addoption(parser):
#     parser.addoption('--browser')
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption('--browser')
#
# @pytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome("C:\\Users\\shubham pate\\Downloads")
#         print("Launching Chrome Browser")
#     elif browser == 'edge':
#         print("Launching Edge Browser")
#         driver = webdriver.Edge()
#     else:
#         print("Headless mode")
#         Edge_options = webdriver.EdgeOptions()
#         Edge_options.add_argument("headless")
#         driver = webdriver.Edge(options=Edge_options)
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     return driver

@pytest.fixture(params=[
    ("admin@yourstore.com", "admin", "Pass"),
    ("admin@yourstore.com1", "admin", "Fail"),
    ("admin@yourstore.com", "admin1", "Fail"),
    ("admin@yourstore.com1", "admin1", "Fail")
])
def getDataforlogin(request):
    return request.param

def pytest_metadata(metadata):
    metadata["Environment"] = "Test"
    metadata['Project Name'] = "NonCommerence"
    metadata['Module Name'] = "Login"
    metadata['Tester'] = "Credence"

    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)
