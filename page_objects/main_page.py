from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators


class MainPage:

    def __init__(self, driver):
        self.driver = driver


    def click_upper_order_button(self):
        self.driver.find_element(*MainPageLocators.UPPER_ORDER_BUTTON).click

    def click_lower_order_button(self):
        self.driver.find_element(*MainPageLocators.LOWER_ORDER_BUTTON).click

    def scroll_to_question(self,question):
        element = self.driver.find_element(*question)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(question))


    def click_question_button(self,question):
        self.driver.find_element(*question).click()

    def get_answer(self,answer):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(answer))
        return self.driver.find_element(*answer).text






