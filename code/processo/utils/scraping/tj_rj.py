from rest_framework.exceptions import NotFound
from selenium.webdriver.common.by import By

from .scrapingPattern import webScraping


class TjRjScraping(webScraping):
    paths = {
                "URL": "https://www3.tjrj.jus.br/consultaprocessual/#/conspublica#porNumero",
                "tipoN": {
                    "unica": {
                        "inputNp": "/html/body/app-root/app-consultar/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/app-codigo-processo-origem/div/div[2]/div/div/input[1]",
                        "button": "/html/body/app-root/app-consultar/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/button[1]",
                        "errorMessage": "/html/body/app-root/simple-notifications/div/simple-notification/div/div[1]/div",
                        "dados": {
                           "serventia" :"/html/body/app-root/app-detalhes-processo/section/div/div/div[2]/div[2]/div[6]/div[1]/div",
                           "dados_processo": "/html/body/app-root/app-detalhes-processo/section/div/div/div[2]/div[2]/div[6]/div[2]",
                           "dados_personagem": "/html/body/app-root/app-detalhes-processo/section/div/div/div[2]/div[2]/div[7]",
                           "movimentacao": "/html/body/app-root/app-detalhes-processo/section/div/div/div[2]/div[2]/div[8]"
                        },
                    "antiga": {}
                }
            }
        }

    def searchNprocess(self, nProcess):
        if self.valid_nProcess(nProcess):
            nProcess = nProcess[:15] + nProcess[21:]
            
        self.driver.get(self.paths["URL"])
        self.searchWait(5, By.XPATH, self.paths["tipoN"]["unica"]["inputNp"]).send_keys(nProcess)
        self.searchWait(0.5, By.XPATH, self.paths["tipoN"]["unica"]["button"]).click()
        try:
            if self.searchWait(2, By.XPATH, self.paths["tipoN"]["unica"]["errorMessage"]).is_displayed():
                raise NotFound()
        except:
            pass

    def response_data(self):
        dados_serventia = self.searchWait(5, By.XPATH, self.paths["tipoN"]["unica"]["dados"]["serventia"]).text.split("\n")
        dados_do_processo= self.searchWait(0.5, By.XPATH, self.paths["tipoN"]["unica"]["dados"]["dados_processo"]).text.split("\n")
        dados_personagem = self.searchWait(0.5, By.XPATH, self.paths["tipoN"]["unica"]["dados"]["dados_personagem"]).text.split("\n")
        dados_movimentacao = self.searchWait(0.5, By.XPATH, self.paths["tipoN"]["unica"]["dados"]["movimentacao"]).text.split("\n")
        
        return [dados_serventia, dados_do_processo, dados_personagem, dados_movimentacao]

    def run(self, nProcess):
        self.searchNprocess(nProcess)
        data = self.response_data()
        return {"body":{"detail": data}, "status": 200}


