from abc import ABC, abstractmethod
from re import search

from rest_framework.exceptions import NotFound, bad_request
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class webScraping(ABC):
    def __init__(self, driver, **kwargs) -> None:
        self.driver = Chrome(driver)
        self.__paths = {}

    @property
    @abstractmethod
    def paths(self):
        return self.__paths
    
    def valid_nProcess(self, nProcess: str) -> bool:
        regex = r"([0-9]{7})[-]([0-9]{2})(.{1})([0-9]{4}).([0-9]{1}).([0-9]{2}).([0-9]{4})"
        validNP = search(regex, nProcess)
        if validNP:
            return True
        raise bad_request()
    
    @abstractmethod
    def run(self, nProcess):
        pass

    @abstractmethod
    def searchNprocess(self, nProcess):
        pass

    @abstractmethod
    def response_data(self):
        pass
       

    def searchWait(self, secs, by, path) -> WebElement:
        return WebDriverWait(self.driver, secs).until(
            EC.presence_of_element_located(
                (by, path)
            )
        )  