from abc import ABC, abstractmethod
from re import search

from rest_framework.exceptions import bad_request
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


class webScraping(ABC):
    def __init__(self, **kwargs) -> None:
        chrome_user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        self.chrome_options = Options()
        self.chrome_options.add_argument(f"--user-agent={chrome_user_agent}")
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.chrome_options.add_argument("--headless")
        self.__paths = {}
        self.driver = Chrome(options=self.chrome_options)

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

    @abstractmethod
    def history_process(self):
        pass


    def searchWait(self, secs, by, path) -> WebElement:
        return WebDriverWait(self.driver, secs).until(
            EC.presence_of_element_located(
                (by, path)
            )
        )
