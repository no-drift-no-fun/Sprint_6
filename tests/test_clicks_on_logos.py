import allure
from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import BasePageLocators
from links import *

class TestClicksOnLogos:

    @allure.title("Нажатие на логотип сайта")
    @allure.description("Проверка перехода на основную страницу при клике на логотип сайта")
    @allure.link(ORDER_URL, name='https://qa-scooter.praktikum-services.ru/order')
    def test_click_scooter_logo(self, driver_start):
        page = MainPage(driver_start)
        page.click_scooter_logo()
        assert BASE_URL == page.get_current_url()

    @allure.title("Нажатие на логотип яндекса")
    @allure.description("Проверка перехода на yandex dzen при клике на логотип yandex")
    @allure.link(BASE_URL, name='https://qa-scooter.praktikum-services.ru/')
    def test_click_yandex_logo(self, driver_start):
        page = MainPage(driver_start)
        page.click_yandex_logo()
        page.switch_to_new_tab()
        page.wait_text_contains("Дзен")
        assert "dzen.ru/" in page.get_current_url()