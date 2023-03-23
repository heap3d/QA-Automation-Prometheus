import time
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class RozetkaPage(BasePage):
    URL_MAIN = 'https://rozetka.com.ua/ua/'

    def __init__(self) -> None:
        super().__init__()


    def check_title(self, expected):
        return self.driver.title == expected

    def go_main(self):
        self.driver.get(RozetkaPage.URL_MAIN)

    def go_computers_notebooks(self):
        self.go_main()
        computers_notebooks_menu = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Ноутбуки та комп’ютери")))
        computers_notebooks_menu.click()
        xpath_loc = "//h1"
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_loc)))

    def go_tablets(self):
        self.go_computers_notebooks()
        computers_notebooks_menu = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Планшети")))
        computers_notebooks_menu.click()

    def filter_rozetka(self):
        xpath_loc = "//a[@data-id='Rozetka']"
        filter_el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_loc)))
        filter_el.click()
        time.sleep(1)
        filter_el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_loc)))
        class_name = filter_el.get_attribute('class')
        return '--checked' in class_name
        
    def click_compare(self, index):
        xpath_loc = f"//rz-grid/ul/li[{index}]//rz-app-compare-button//button"
        time.sleep(1)
        compare_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_loc)))
        compare_button.click()

    def is_compared(self, index):
        self.click_compare(index)
        time.sleep(1)
        xpath_loc = f"//rz-grid/ul/li[{index}]//rz-app-compare-button//button"
        compare_icon = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_loc)))
        class_attr = compare_icon.get_attribute('class')
        return class_attr == "compare-button compare-button_state_active"

    def check_header_compare_num(self, count):
        for i in range(1, count+1):
            self.click_compare(i)
        time.sleep(1)
        xpath_loc = f"//header//rz-comparison//span"
        header_compare = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_loc)))
        compare_num = int(header_compare.text)
        return count == compare_num

    def open_compare_page(self, count):
        for i in range(1, count+1):
            self.click_compare(i)
        self.click_compare(1)
        time.sleep(1)

    def clear_compare_bin(self, count):
        time.sleep(1)
        xpath_loc = f"//header//rz-comparison//span"
        header_compare = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_loc)))
        header_compare.click()
        time.sleep(1)
        xpath_loc = f"//rz-comparison-modal//button"
        del_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_loc)))
        del_button.click()
        time.sleep(1)
        xpath_loc = f"//header//rz-comparison//span"
        is_comparing = WebDriverWait(self.driver, 5).until_not(EC.presence_of_element_located((By.XPATH, xpath_loc)))
        return is_comparing
