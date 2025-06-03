import allure
import pytest
from selenium import webdriver
from page_objects.main_page import MainPage
from locators.main_page_locators import MainPageLocators
import data

class TestQuestion:

    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @pytest.mark.parametrize(
        "question, answer, expect",  [
            (MainPageLocators.QUESTION_1_BUTTON, MainPageLocators.QUESTION_1_ANSWER, data.answer1),
            (MainPageLocators.QUESTION_2_BUTTON, MainPageLocators.QUESTION_2_ANSWER, data.answer2),
            (MainPageLocators.QUESTION_3_BUTTON, MainPageLocators.QUESTION_3_ANSWER, data.answer3),
            (MainPageLocators.QUESTION_4_BUTTON, MainPageLocators.QUESTION_4_ANSWER, data.answer4),
            (MainPageLocators.QUESTION_5_BUTTON, MainPageLocators.QUESTION_5_ANSWER, data.answer5),
            (MainPageLocators.QUESTION_6_BUTTON, MainPageLocators.QUESTION_6_ANSWER, data.answer6),
            (MainPageLocators.QUESTION_7_BUTTON, MainPageLocators.QUESTION_7_ANSWER, data.answer7),
            (MainPageLocators.QUESTION_8_BUTTON, MainPageLocators.QUESTION_8_ANSWER, data.answer8)
        ])
    def test_question(self,question,answer,expect):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page = MainPage(self.driver)
        main_page.scroll_to_question(question)
        main_page.click_question_button(question)
        answer = main_page.get_answer(answer)
        assert answer == expect


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()



