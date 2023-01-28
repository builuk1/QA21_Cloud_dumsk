from xpath.registration_page import registration
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class reg_page():


    def email_field(self,driver,email):
        register_email_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(('xpath', registration.xpath_register_email)))
        register_email_field.send_keys(email)

    def nick_field(self, driver, nick):
        register_nick = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', registration.xpath_register_nick)))
        register_nick.send_keys(nick)

    def password_field(self, driver, password):
        register_password = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', registration.xpath_register_password)))
        register_password.send_keys(password)

    def password2_field(self, driver, password2):
        register_password2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', registration.xpath_register_password2)))
        register_password2.send_keys(password2)
    def male_radio(self,driver):
        register_gender_male = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', registration.xpath_register_gender_male)))
        register_gender_male.click()
    def female_radio(self,driver):
        register_gender_female = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', registration.xpath_register_gender_female)))
        register_gender_female.click()