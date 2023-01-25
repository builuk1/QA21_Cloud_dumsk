def register_user():
    import time
    from factory.new_user import User
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    import os

    my_user = User()
    # my_user.nick = my_user.nick + my_user.nick + my_user.nick + my_user.nick
    # length = len(my_user.nick)
    options = ChromeOptions()
    foptions = FirefoxOptions()
    options.headless = False#True Запуск теста без включения браузера

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
    #XPath Axis         Ось XPath
    xpath_user_finish = '//a[@class="celluname1"]'

    enter_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_enter_button)))
    enter_button.click()
    enter_registration_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_enter_registration_button)))
    enter_registration_button.click()

    register_gender_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_button)))
    register_gender_button.click()

    login_textarea = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '//td[@class="newscol"]/div')))
    login = login_textarea.text
    f = driver.find_element('xpath', '//td[@class="newscol"]/div')
    f.text
    print(login)
    time.sleep(15)


    driver.close()



    return my_user.nick, login #'Пользователь с таким ником уже зарегистрирован. Придумайте другой'

if __name__ == '__main__':
    print(register_user())