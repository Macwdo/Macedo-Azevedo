from rest_framework.exceptions import NotFound
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from re import search
from rest_framework.exceptions import bad_request
from selenium.webdriver.remote.webelement import WebElement


class TjRjScraping:
    def __init__(self, numero_processo) -> None:
        chrome_user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        self.chrome_options = Options()
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument('--remote-debugging-port=9222')
        self.chrome_options.add_argument(f"--user-agent={chrome_user_agent}")
        self.driver = Chrome(options=self.chrome_options)
        self.n_process = numero_processo

    paths = {
                "URL": "https://www3.tjrj.jus.br/consultaprocessual/#/conspublica#porNumero",
                "tipoN": {
                    "unica": {
                        "inputNp": "/html/body/app-root/app-consultar/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/app-codigo-processo-origem/div/div[2]/div/div/input[1]",
                        "button": "/html/body/app-root/app-consultar/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/button[1]",
                        "errorMessage": "/html/body/app-root/simple-notifications/div/simple-notification/div/div[1]/div",
                        "all_changes_button": "/html/body/app-root/app-detalhes-processo/section/div/div/div[1]/div[2]/button[2]",
                        "dados": {
                            "last_change": "/html/body/app-root/app-detalhes-processo/section/div/div/div[2]/div[2]/div[8]/div[3]",
                           "all_changes": "/html/body/app-root/app-detalhes-processo/section/div/div/div[3]/div[1]"
                        },
                    "antiga": {}
                }
            }
        }

    def valid_nProcess(self, nProcess: str) -> bool:
        regex = r"([0-9]{7})[-]([0-9]{2})(.{1})([0-9]{4}).([0-9]{1}).([0-9]{2}).([0-9]{4})"
        validNP = search(regex, nProcess)
        if validNP:
            return True
        raise bad_request()

    def searchWait(self, secs, by, path) -> WebElement:
        return WebDriverWait(self.driver, secs).until(
            EC.presence_of_element_located(
                (by, path)
            )
        )

    def searchNprocess(self, nProcess):
        self.n_process = nProcess
        if self.valid_nProcess(nProcess):
            nProcess = nProcess[:15] + nProcess[21:]

        self.driver.get(self.paths["URL"])
        self.searchWait(40, By.XPATH, self.paths["tipoN"]["unica"]["inputNp"]).send_keys(nProcess)
        self.searchWait(30, By.XPATH, self.paths["tipoN"]["unica"]["button"]).click()
        try:
            if self.searchWait(2, By.XPATH, self.paths["tipoN"]["unica"]["errorMessage"]).is_displayed():
                raise NotFound()
        except:
            pass

    def history_process(self, last=False):
        changes_button = self.searchWait(40, By.XPATH, self.paths["tipoN"]["unica"]["all_changes_button"])
        changes_button.click()
        if last:
            changes = self.searchWait(10, By.XPATH, self.paths["tipoN"]["unica"]["dados"]["last_change"]).text
            all_changes = changes.split("\n")
        else:
            changes = self.searchWait(10, By.XPATH,  self.paths["tipoN"]["unica"]["dados"]["all_changes"]).text
            all_changes = changes.split("\n")[1:]
        changes_data = []
        final_data = {}
        change_type = ""
        first = True
        change_date = ""
        next_index_is_data = False
        for item in all_changes:
            if "Tipo do Movimento" in item and first:
                change_type = item.split("Tipo do Movimento:")[1].strip()
                first = False
                continue

            elif "Tipo do Movimento" in item and not first:
                final_data[change_type] = {
                    "data": changes_data,
                    "date": change_date
                }
                changes_data = []
                change_type = item.split("Tipo do Movimento:")[1].strip()
                continue

            if next_index_is_data:
                change_date = item
                next_index_is_data = False

            if "Data" in item.capitalize():
                next_index_is_data = True
            changes_data.append(item)

        if last:
            final_data[change_type] = {
                "data": changes_data,
                "date": change_date
            }

        return {self.n_process: final_data}


    def run(self):
        self.searchNprocess(self.n_process)
        data = self.history_process(last=False)
        return data


