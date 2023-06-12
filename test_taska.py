import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture
def size_window():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

def test_1_positive(size_window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_2_negative(size_window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('bbkfdmkmck').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))