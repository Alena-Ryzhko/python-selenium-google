from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from features.logger import MyListener


def browser_init(context, name):

    context.driver = webdriver.Chrome()
    # context.driver = webdriver.Safari()
    # context.driver = webdriver.Firefox()
    # =====================================================================================
    # # ##### HEADLESS #####
    #
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(executable_path='drivers/chromedriver', chrome_options=options)
    # =====================================================================================
    # # ##### LOGGER ##### ???
    #
    # context.driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    # =====================================================================================
    # # ##### Browser Stack ######
    #
    # # Comment lines with "context.driver" before start running test in Browser Stack, lines 12-16
    # # Result of tests execution is here: https://automate.browserstack.com/dashboard/v2
    # bs_user = "alenaryzhko1"
    # bs_pw = "UhWjjuzSQ8KsqAafs5Ha"
    #
    # desired_cap = {
    #     'browser': 'Chrome',
    #     'browser_version': '83.0',
    #     'os': 'Windows',
    #     'os_version': '10',
    #     'name': name
    # }
    # url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    # =====================================================================================

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver, 15)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
