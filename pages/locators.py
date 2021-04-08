from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_USER_NAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "[name='login_submit']")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.XPATH, "//button[contains(@class,'btn-add-to-basket')]")
    NAME_BOOK_FOR_BASKET = (By.CSS_SELECTOR, "[class='active']")
    BOOK_ADDED_IN_BASKET = (By.CSS_SELECTOR, ".alertinner > strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_PRICE_ADDED_IN_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner > p strong")
    BOOKS_MESSAGE_SUCCESS = (By.CSS_SELECTOR, "#messages .alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,"#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_WITH_BOOKS = (By.CSS_SELECTOR, "#content_inner .hidden-xs .row")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")