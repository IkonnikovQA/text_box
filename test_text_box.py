from selene import browser

from faker import Faker

fake = Faker()

def test_text_box():
    browser.open('https://demoqa.com/text-box')
    browser.element('#userName').type(fake.name())
    browser.element('#userEmail').type(fake.email())
    browser.element('#currentAddress').type(fake.address())
    browser.element('#permanentAddress').type(fake.address())
    browser.element('#submit').click()
