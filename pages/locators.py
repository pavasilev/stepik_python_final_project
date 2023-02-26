from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR,".btn-group .btn:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR,"#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR,"#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR,"#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR,"#id_registration-password1")
    REPEAT_PASSWORD = (By.CSS_SELECTOR,"#id_registration-password2")
    ENTER_BUTTON = (By.CSS_SELECTOR,"[value='Register']")
class ProductPageLocators():
    BUY_BUTTON = (By.CLASS_NAME,"btn-add-to-basket")
    SUCCES_ALERT_BUY = (By.CSS_SELECTOR,"div.alert:nth-child(1)")
    SUCCES_ALERT_COST = (By.CSS_SELECTOR,"div.alert:nth-child(3)")
    NAME_OF_BOOK_IN_ALERT = (By.CSS_SELECTOR, "div.alert:nth-child(1) strong")
    NAME_OF_BOOK_IN_CARD = (By.CSS_SELECTOR,".product_main h1")
    COST_OF_BOOK_IN_ALERT = (By.CSS_SELECTOR,"div.alert:nth-child(3) strong")
    COST_OF_BOOK_IN_CARD = (By.CSS_SELECTOR,".product_main .price_color")
class BasketPageLocators():
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR,".col-sm-6.h3")
    EMPTY_BASKET = (By.CSS_SELECTOR,"#content_inner > p")