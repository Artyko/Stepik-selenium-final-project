from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL_FORM = (By.CSS_SELECTOR, "input[name='login-username'].form-control")
    LOGIN_PASSWORD_FORM = (By.CSS_SELECTOR, "input[name='login-password'].form-control")
    REGISTER_EMAIL_FORM = (By.CSS_SELECTOR, "input[name='registration-email'].form-control")
    REGISTER_PASSWORD_FORM = (By.CSS_SELECTOR, "input[name='registration-password1'].form-control")
    REGISTER_PASSWORD_CONFIRM_FORM = (By.CSS_SELECTOR, "input[name='registration-password2'].form-control")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_COST = (By.CSS_SELECTOR, "div.alert > div > p:nth-child(1) > strong")
    BASKET_COST = (By.CSS_SELECTOR, "div.alertinner > p > strong")



