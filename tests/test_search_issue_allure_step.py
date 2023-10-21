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
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        browser.element(".header-search-button").click()
        browser.element("#query-builder-test").send_keys("o1ra/Allure-Reports")
        browser.element("#query-builder-test").submit()

    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text("o1ra/Allure-Reports")).click()

    with allure.step("Открываем таб Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие текста 'Welcome to issues!'"):
        browser.element(by.partial_text("Welcome to issues!")).should(be.visible)
