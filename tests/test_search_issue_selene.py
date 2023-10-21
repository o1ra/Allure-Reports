import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "Irina_Kirillova")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_search_issue():
    #GIVEN
    browser.open("https://github.com")

    #WHEN
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").send_keys("o1ra/Allure-Reports")
    browser.element("#query-builder-test").submit()

    browser.element(by.link_text("o1ra/Allure-Reports")).click()
    browser.element("#issues-tab").click()

    #THEN
    browser.element(by.partial_text("Welcome to issues!")).should(be.visible)