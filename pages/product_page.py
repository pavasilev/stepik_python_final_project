from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product(self):
        buy_button = self.browser.find_element(*ProductPageLocators.BUY_BUTTON)
        buy_button.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT_BUY), \
            "Success buy message is presented, but should not be"

    def buy_message_should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERT_BUY),  \
            "Success buy alert doesnt disappear"

    def should_be_right_book(self):
        self.should_be_success_alert()
        self.should_be_cost_alert()
        self.should_be_right_name()
        self.should_be_right_cost()

    def should_be_success_alert(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ALERT_BUY), "There is no success alert!"

    def should_be_cost_alert(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ALERT_COST), "There is no alert with cost!"

    def should_be_right_name(self):
        name_in_alert = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_IN_ALERT)
        name_in_card = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_IN_CARD)
        assert name_in_alert.text == name_in_card.text, "Books are not same!"

    def should_be_right_cost(self):
        cost_in_alert = self.browser.find_element(*ProductPageLocators.COST_OF_BOOK_IN_ALERT)
        cost_in_card = self.browser.find_element(*ProductPageLocators.COST_OF_BOOK_IN_CARD)
        assert cost_in_alert.text == cost_in_card.text, "Cost are not same!"