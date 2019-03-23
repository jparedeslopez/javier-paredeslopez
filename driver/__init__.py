from driver.elements import Elements
from driver.utils.logger import Logger
from driver.utils.configure import Configure
from appium import webdriver
from tests.testsdata import TestsData

class Driver(Elements, Logger, Configure, TestsData):

    def __init__(self, config):
        Logger.__init__(self)
        Configure.__init__(self, config)
        self.driver = webdriver.Remote(self.appiumServer, self.desiredCaps)