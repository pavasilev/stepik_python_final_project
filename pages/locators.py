from selenium.webdriver.common.by import By
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR,"#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR,"#register_form")

class ProductPageLocators():
    BUY_BUTTON = (By.CLASS_NAME,"btn-add-to-basket")
    SUCCES_ALERT_BUY = (By.CSS_SELECTOR,"div.alert:nth-child(1)")
    SUCCES_ALERT_COST = (By.CSS_SELECTOR,"div.alert:nth-child(3)")
    NAME_OF_BOOK_IN_ALERT = (By.CSS_SELECTOR, "div.alert:nth-child(1) strong")
    NAME_OF_BOOK_IN_CARD = (By.CSS_SELECTOR,".product_main h1")
    COST_OF_BOOK_IN_ALERT = (By.CSS_SELECTOR,"div.alert:nth-child(3) strong")
    COST_OF_BOOK_IN_CARD = (By.CSS_SELECTOR,".product_main .price_color")