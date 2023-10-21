import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "Irina_Kirillova")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    open_main_page("https://github.com")
    search_for_repository("o1ra/Allure-Reports")
    go_to_repository("o1ra/Allure-Reports")
    open_issue_tab()
    should_see_issue_text()


@allure.step("Открываем главную страницу")
def open_main_page(page):
    browser.open(page)


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").send_keys(repo)
    browser.element("#query-builder-test").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие текста 'Welcome to issues!'")
def should_see_issue_text():
    browser.element(by.partial_text("Welcome to issues!")).should(be.visible)