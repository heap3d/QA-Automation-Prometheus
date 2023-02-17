from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class RZTKPage(BasePage):
    URL = 'https://rozetka.com.ua/ua/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(RZTKPage.URL)

    def try_login(self, username, password):
        # user_btn = self.driver.find_element(By.CSS_SELECTOR, 'rz-user > button')
        # user_btn = self.driver.find_element(By.CSS_SELECTOR, 'rz-cart > button')
        user_btn = self.driver.find_element(By.XPATH, '//rz-cart/button')
        user_btn.click()
