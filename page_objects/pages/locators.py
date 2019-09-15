from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL_FORM = (By.CSS_SELECTOR, "input[name='login-username'].form-control")
    LOGIN_PASSWORD_FORM = (By.CSS_SELECTOR, "input[name='login-password'].form-control")
    REGISTER_EMAIL_FORM = (By.CSS_SELECTOR, "input[name='registration-email'].form-control")
    REGISTER_PASSWORD_FORM = (By.CSS_SELECTOR, "input[name='registration-password1'].form-control")
    REGISTER_PASSWORD_CONFIRM_FORM = (By.CSS_SELECTOR, "input[name='registration-password2'].form-control")

