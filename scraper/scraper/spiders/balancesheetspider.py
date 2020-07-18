import os

import scrapy
from scrapy.selector import Selector
from .selenium_setup import setup_driver
from selenium.webdriver.support.select import Select
from ..items import BalanceSheetItem


class BalanceSheetSpider(scrapy.Spider):
    name = "balancesheetspider"
    allowed_domains = ["finance.yahoo.com"]
    start_urls = ["https://finance.yahoo.com/quote/GOOG/balance-sheet?p=GOOG"]

    def __init__(self, name=None, **kwargs):
        self.driver = setup_driver()
        super().__init__(name, **kwargs)

    def parse(self, response):
        self.driver.get(self.start_urls[0])
        data = Selector(text=self.driver.page_source)
        self.driver.close()
        self.driver.quit()
        for balance in data.css("#Col1-1-Financials-Proxy"):
            item = BalanceSheetItem()
            item["date"] = balance.xpath(
                "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[1]/div/div[2]/span/text()").get()
            item["total_assets"] = balance.xpath(
                "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/span/text()").get()
            item["total_liabilities"] = balance.xpath(
                "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/span/text()").get()
            item["total_equity"] = balance.xpath(
                "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/span/text()").get()
            yield item
            item = BalanceSheetItem()
            item["date"] = balance.xpath(
                "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[1]/div/div[3]/span/text()").get()
            item["total_assets"] = balance.xpath(
                "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/span/text()").get()
            item["total_liabilities"] = balance.xpath(
                "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/span/text()").get()
            item["total_equity"] = balance.xpath(
                "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[3]/div[1]/div[3]/span/text()").get()
            yield item
