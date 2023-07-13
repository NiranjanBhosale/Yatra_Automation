import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='function', autouse=True)
def setup(request):
    opts = webdriver.ChromeOptions()
    opts.add_argument('--disable-notifications')


    # OPTIONS TO STOP CONSIDERING THE SCRIPT EXECUTION AS BOT CONTROLLED
    opts.add_argument('--disable-blink-features=AutomationControlled')
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option('useAutomationExtension', False)

    # OPTION TO CONTINUE WITH THE SCRIPT EXECUTION ONCE THE PAGE IS INTERACTABLE AND NOT WAIT FOR WHOLE PAGE TO LOAD
    opts.page_load_strategy = 'eager'

    driver = webdriver.Chrome(options=opts)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()


    accept_cookies_button = "//button[text()='Ok,I Agree']"
    accept_cookies_element = driver.find_element(By.XPATH, accept_cookies_button)

    if accept_cookies_element.is_enabled():
        accept_cookies_element.click()

    request.cls.driver = driver
    print("Request Object",request)
    print("Node ID", request.node)


    yield
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    print("Outcome", outcome.get_result().outcome)
    print("Call",call)
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add urlcall to report
        extras.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extras = extras

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#
#     # set a report attribute for each phase of a call, which can
#     # be "setup", "call", "teardown"
#
#     setattr(item, "rep_" + rep.when, rep)
#
# # check if a test has failed
# @pytest.fixture(scope="function", autouse=True)
# def test_failed_check(request):
#     yield
#     # request.node is an "item" because we use the default
#     # "function" scope
#     if request.node.rep_setup.failed:
#         print("setting up a test failed!", request.node.nodeid)
#     elif request.node.rep_setup.passed:
#         if request.node.rep_call.failed:
#             driver = request.node.funcargs['selenium_driver']
#             take_screenshot(driver, request.node.nodeid)
#             print("executing test failed", request.node.nodeid)

# make a screenshot with a name of the test, date and time
# def take_screenshot(driver, nodeid):
#     time.sleep(1)
#     file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/","_").replace("::","__")
#     driver.save_screenshot(file_name)

