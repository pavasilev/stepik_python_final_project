from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_product(self):
        buy_button = self.browser.find_element(*ProductPageLocators.BUY_BUTTON)
        buy_button.click()

    def should_be_right_book(self):
        self.should_be_succes_alert()
        self.should_be_cost_alert()
        self.should_be_right_name()
        self.should_be_right_cost()

    def should_be_succes_alert(self):
        assert self.is_element_present(*ProductPageLocators.SUCCES_ALERT_BUY), "There is no succes alert!"

    def should_be_cost_alert(self):
        assert self.is_element_present(*ProductPageLocators.SUCCES_ALERT_COST), "There is no alert with cost!"

    def should_be_right_name(self):
        name_in_alert = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_IN_ALERT)
        name_in_card = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_IN_CARD)
        print(name_in_alert.text)
        print(name_in_card.text)
        assert name_in_alert.text == name_in_card.text, "Books are not same!"

    def should_be_right_cost(self):
        cost_in_alert = self.browser.find_element(*ProductPageLocators.COST_OF_BOOK_IN_ALERT)
        cost_in_card = self.browser.find_element(*ProductPageLocators.COST_OF_BOOK_IN_CARD)
        print(cost_in_alert.text)
        print(cost_in_card.text)
        assert cost_in_alert.text == cost_in_card.text, "Cost are not same!"