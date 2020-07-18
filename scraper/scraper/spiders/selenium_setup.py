import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def setup_driver():

    options = Options()
    # options.headless = True
    options.add_argument(
        'user-agent="Mozilla/5.0 ' '(Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0"'
    )
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(
        executable_path="{}/scraper/spiders/chromedriver".format(os.getcwd()), chrome_options=options
    )
    return driver