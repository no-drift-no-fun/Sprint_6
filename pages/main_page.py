import allure
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step('Клик по кнопке "Заказать" в хедере')
    def click_top_order_button(self):
        self.find_element_with_wait(BasePageLocators.order_button)
        self.click_to_element(BasePageLocators.order_button)

    @allure.step('Клик по кнопке "Заказать" внизу')
    def scroll_to_how_it_works_and_click_order(self):
        self.scroll_to_element(BasePageLocators.second_order_button)
        self.click_to_element(BasePageLocators.second_order_button)

    @allure.step('Скролл до блока FAQ и клик на вопрос')
    def click_question(self, locator):
        self.scroll_to_element(locator)
        self.click_to_element(locator)

    @allure.step('Клик по лого "Самоката"')
    def click_scooter_logo(self):
        self.click_to_element(BasePageLocators.scooter_logo)

    @allure.step('Клик по лого "Яндекс"')
    def click_yandex_logo(self):
        self.click_to_element(BasePageLocators.yandex_logo)
