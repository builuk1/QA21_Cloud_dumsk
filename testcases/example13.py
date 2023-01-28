# Task: QA25-13 Check duplicated username
# https://dumskaya.net/

def register_user_with_same_nick():
    from time import time
    from factory.new_user import User
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    import os

    my_user = User()

    options = ChromeOptions()
    options.headless = True  # True Запуск теста без включения браузера

    path = f'{os.getcwd()}/drivers/chromedriver'
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://dumskaya.net/'

    driver.maximize_window()
    driver.get(url)

    xpath_enter_button = '//a[@id="pp"]/b'
    xpath_enter_registration_button = '//a[@href="/register/"]'

    xpath_register_email = '//td/input[@name="email"]'
    xpath_register_nick = '//input[@name="nick"]'
    xpath_register_password = '//input[@name="password1"]'
    xpath_register_password2 = '//input[@name="password2"]'
    xpath_register_gender_male = '//input[@name="gender"][@value="m"]'
    xpath_register_gender_female = '//input[@name="gender"][@value="f"]'
    xpath_register_button = '//input[@type="submit"]/following::input[@type="submit"]'
    # XPath Axis         Ось XPath
    xpath_user_finish = '//a[@class="celluname1"]'
    xpath_user_exit = '//a[@class="exitlink"]'
    xpath_error = '//div[@style="color:red;"]'

    enter_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_enter_button)))
    enter_button.click()
    enter_registration_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(('xpath', xpath_enter_registration_button)))
    enter_registration_button.click()

    register_email_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_email)))
    register_email_field.send_keys(my_user.email)

    register_nick = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_nick)))
    register_nick.send_keys(my_user.nick)

    register_password = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_password)))
    register_password.send_keys(my_user.password)

    register_password2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_password2)))
    register_password2.send_keys(my_user.password)

    register_gender_male = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_gender_male)))
    register_gender_male.click()

    register_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_button)))
    register_button.click()

    login_textarea = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_user_finish)))
    login = login_textarea.text

    if my_user.nick == login:
        login_textarea.click()

        login_exit = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_user_exit)))
        login_exit.click()

        enter_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_enter_button)))
        enter_button.click()
        enter_registration_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(('xpath', xpath_enter_registration_button)))
        enter_registration_button.click()

        register_email_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_email)))
        register_email_field.send_keys(str(time()).replace('.', '')[:10] + my_user.email)

        register_nick = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_nick)))
        register_nick.send_keys(my_user.nick)

        register_password = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_password)))
        register_password.send_keys(my_user.password)

        register_password2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_password2)))
        register_password2.send_keys(my_user.password)

        register_gender_male = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(('xpath', xpath_register_gender_male)))
        register_gender_male.click()

        register_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_button)))
        register_button.click()

        error_textarea = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_error)))
        error_same_nick = error_textarea.text
    else:
        error_same_nick = ''

    #   time.sleep(6000)
    driver.close()

    return error_same_nick, 'Пользователь с таким ником уже зарегистрирован. Придумайте другой'


if __name__ == '__main__':
    a = register_user_with_same_nick()
    print(a[0])
    print(a[1])
    print(a[0] == a[1])
