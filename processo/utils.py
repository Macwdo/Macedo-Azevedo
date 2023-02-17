import datetime
import re
from time import sleep

import pytz
from rest_framework.exceptions import bad_request
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
                            "dados": {
                                "autor": '/html/body/app-root/app-detalhes-processo/section/div/div/div[2]/div[2]/div[7]/div[3]/label[2]',
                                "reu":'/html/body/app-root/app-detalhes-processo/section/div/div/div[2]/div[2]/div[7]/div[4]/label[2]',
                                "advogados": [
                                    '/html/body/app-root/app-detalhes-processo/section/div/div/div[2]/div[2]/div[7]/div[5]/label[2]',
                                    '/html/body/app-root/app-detalhes-processo/section/div/div/div[2]/div[2]/div[7]/div[5]/label[3]',
                                    '/html/body/app-root/app-detalhes-processo/section/div/div/div[2]/div[2]/div[7]/div[5]/label[4]'
                                ],
                                "movimentacao": "/html/body/app-root/app-detalhes-processo/section/div/div/div[2]/div[2]/div[8]/div[3]/app-movimento/div[2]"
                            }
                        },
                        "antiga": {}
                    }
                }
            }
        }
        self.regex = r"([0-9]{7})[-]([0-9]{2})(.{1})([0-9]{4}).([0-9]{1}).([0-9]{2}).([0-9]{4})"

    def valid_nProcess(self, nProcesso):
        validNP = re.search(self.regex, nProcesso)
        if validNP:
            return True
        return False
    
    def searchWait(self, driver, secs, xpath):
        return WebDriverWait(driver, secs).until(
            EC.presence_of_element_located(
                ("xpath", xpath)
            )
        )

    def search(self, nProcesso: str, request):
        if not self.valid_nProcess(nProcesso):
            bad_request(request)
        nProcesso = nProcesso[:15] + nProcesso[21:]
        driver = self.__driver
        driver.get(self.const["Rj"]["Tj"]["URL"])   


        self.searchWait(driver, 5, self.const["Rj"]["Tj"]["tipoN"]["unica"]["inputNp"]).send_keys(nProcesso)
        
        self.searchWait(driver, 0.5, self.const["Rj"]["Tj"]["tipoN"]["unica"]["button"]).click()

        dados = self.const["Rj"]["Tj"]["tipoN"]["unica"]["dados"]
        dataDict = {
            "autor": self.searchWait(driver, 3, dados["autor"]).text,
            "reu": self.searchWait(driver, 1, dados["reu"]).text,
            "advogados": [
            self.searchWait(driver, 1, dados["advogados"][0]).text,
            self.searchWait(driver, 1, dados["advogados"][1]).text,
            self.searchWait(driver, 1, dados["advogados"][2]).text
            ],
            "movimentacao": self.searchWait(driver, 1, dados["movimentacao"]).text.split("\n")
        }
        driver.close()
        
        
        return dataDict
    


