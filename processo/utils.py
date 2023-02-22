import datetime
import re
import pytz
from rest_framework.exceptions import bad_request
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

timezone = pytz.timezone('America/Sao_Paulo')


def get_current_time(timezone=timezone):
    return datetime.datetime.now(tz=timezone)


class webScraping:
    def __init__(self, **kwargs) -> None:
        self.__driver = webdriver.Chrome(executable_path="../chromedriver")
        self.const = {
            "Rj": {
                "Tj":{
                    "URL": "https://www3.tjrj.jus.br/consultaprocessual/#/conspublica#porNumero",
                    "tipoN": {
                        "unica": {
                            "inputNp": "/html/body/app-root/app-consultar/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/app-codigo-processo-origem/div/div[2]/div/div/input[1]",
                            "button": "/html/body/app-root/app-consultar/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/button[1]",
                            "errorMessage": "/html/body/app-root/simple-notifications/div/simple-notification/div/div[1]/div",
                            "dados": {
                                "PF": {},
                                "PJ": {}
                            },
                        "antiga": {}
                    }
                }
            }
        }
    }
        self.regex = r"([0-9]{7})[-]([0-9]{2})(.{1})([0-9]{4}).([0-9]{1}).([0-9]{2}).([0-9]{4})"

    def valid_nProcess(self, nProcesso) -> bool:
        validNP = re.search(self.regex, nProcesso)
        if validNP:
            return True
        return False

    def searchAsync(self, driver, secs, xpath) -> WebElement:
        return WebDriverWait(driver, secs).until(
            EC.presence_of_element_located(
                ("xpath", xpath)
            )
        )

    def xpathIdentifier(self, driver) -> str:
        xpath = self.searchAsync(driver, 3, "/html/body/app-root/app-detalhes-processo/section/div/div/div[2]/div[2]/div[7]/div[4]/label[1]").text[2]
        if xpath == "u" or "t":
            return "PF"
        else:
            return "PJ"
    def invalidnProcess(self, driver) -> bool:
        try:
            err_message = self.searchAsync(driver, 2, self.const["Rj"]["Tj"]["tipoN"]["unica"]["errorMessage"])
            if err_message.is_displayed():
                return True
        except:
            return False

    def search(self, nProcesso: str, request) -> dict:
        if not self.valid_nProcess(nProcesso):
            bad_request(request, exception={"detail": "codigo de processo invalido"})
        nProcesso = nProcesso[:15] + nProcesso[21:]
        driver = self.__driver
        driver.get(self.const["Rj"]["Tj"]["URL"])
        self.searchAsync(driver, 5, self.const["Rj"]["Tj"]["tipoN"]["unica"]["inputNp"]).send_keys(nProcesso)
        self.searchAsync(driver, 0.5, self.const["Rj"]["Tj"]["tipoN"]["unica"]["button"]).click()
        if self.invalidnProcess(driver):
            driver.close()
            return {"body": {"detail": "codigo de processo invalido"}, "status": 404}
        tipo = self.xpathIdentifier(driver)

        dataDict = {}

        driver.close()

        
        return dataDict
    


