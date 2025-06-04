import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from links import *
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators


class TestOrder:
    dict_locator = {"name": OrderPageLocators.name_field,
                    "surname": OrderPageLocators.surname_field,
                    "address": OrderPageLocators.address_field,
                    "metro": OrderPageLocators.metro_field,
                    "phone": OrderPageLocators.phone_field,
                    "date": OrderPageLocators.date_when_to_bring_a_scooter_field,
                    "rent": OrderPageLocators.rental_period_dropdown_menu,
                    "duration": OrderPageLocators.one_day_in_rental_period_menu,
                    "color": OrderPageLocators.checkbox_select_black_color_of_the_scooter,
                    "comment": OrderPageLocators.comment_field,
                    "button_order": OrderPageLocators.order_button_for_complete_the_order,
                    "button_yes": OrderPageLocators.order_button_for_yes_the_order,
                    "modal": OrderPageLocators.modal_of_successful_order}

    @pytest.mark.parametrize("dict_data", [
        (
         {"name":"Иля",
          "surname":"Фамилия",
          "address": "Улица Улица, дом дом",
          "metro":"Выхино",
          "phone":"11111111111",
          "date":"06.06.2025",
          "comment":"Ха"}),
        (
         {"name": "Нейм",
          "surname": "Сурнейм",
          "address": "Улица Стрит, дом хоум",
          "metro": "ВДНХ",
          "phone": "22222222222",
          "date": "06.06.2024",
          "comment": "Нигого нет"}),
    ])
    @allure.title("Оформление заказа")
    @allure.description("Создаем заказ и проверяем, что отображается модальное окно 'Заказ оформлен'")
    @allure.link(BASE_URL, name='https://qa-scooter.praktikum-services.ru/')
    def test_make_an_order(self, driver_start, dict_data):
        main_page = MainPage(driver_start)
        main_page.click_top_order_button()
        order_page = OrderPage(driver_start)
        order_page.add_fields_in_who_is_the_scooter_for(self.dict_locator["name"], dict_data["name"],
                                                  self.dict_locator["surname"], dict_data["surname"],
                                                  self.dict_locator["address"], dict_data["address"],
                                                  self.dict_locator["metro"], dict_data["metro"],
                                                  self.dict_locator["phone"], dict_data["phone"])
        order_page.add_fields_in_about_rent(self.dict_locator["date"], dict_data["date"],
                                      self.dict_locator["rent"],
                                      self.dict_locator["duration"],
                                      self.dict_locator["color"],
                                      self.dict_locator["comment"], dict_data["comment"],
                                      self.dict_locator["button_order"],
                                      self.dict_locator["button_yes"])
        assert "Заказ оформлен" in order_page.get_text_from_element(self.dict_locator["modal"])

    @allure.title("Нажатие на вторую кнопку 'Заказать'")
    @allure.description("Проверка работоспособности второй кнопки 'Заказать'")
    @allure.link(BASE_URL, name='https://qa-scooter.praktikum-services.ru/')
    def test_check_second_order_button(self, driver_start):
        page = MainPage(driver_start)
        page.scroll_to_how_it_works_and_click_order()
        assert "/order" in driver_start.current_url