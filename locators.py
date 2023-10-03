class AuthLocators:

    login_field = '//input[@id="passp-field-login"]'
    password_field = '//input[@id="passp-field-passwd"]'
    phone_field = '//input[@id="passp-field-phone"]'
    enter_button = '//button[@id="passp:sign-in"]'
    create_id_button = ''
    email_switcher = '//span[text()="Почта"]/..'
    phone_switcher = '//span[text()="Телефон"]/..'
    login_error_text = '//div[@id="field:input-login:hint"]'
    phone_error_text = '//div[@id="field:input-phone:hint"]'
    password_error_text = '//div[@id="field:input-passwd:hint"]'
    lk_home_locator = '//a[@data-testid="home-link"]'
    sms_code_field = '//input[@id="passp-field-phoneCode"]'
    social_google_button = '//button[@aria-label="Google"]'
    social_google_login_field = '//input[@id="identifierId"]'
    social_google_password_field = '//input[@aria-label="Введите пароль"]'
    social_google_password_error = '//span[text()[contains(.,"Неверный пароль")]]'
    social_google_next_button = '//span[text()="Далее"]'