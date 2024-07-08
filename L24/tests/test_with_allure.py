import allure
import pytest


@pytest.fixture
def user():
    return 'AAAA'


@pytest.fixture
def setup():
    print("Setup")
    yield
    print("Tear down")

@allure.step
def find_element():
    pass


@allure.step('Entering name {0}')
def enter_name(name):
    find_element()



@allure.step('Entering password {password}')
def enter_password(password):
    pass

@allure.step
def click_login():
    pass


@allure.epic('Startup')
@allure.feature('Login')
@allure.story('Succesfull login')
@allure.title("Login successfuly")
@allure.description("This test verifies ...")
def test_login(user, setup):
    enter_name('John')
    enter_password('password')
    click_login()


@allure.severity(severity_level=allure.severity_level.MINOR)
def test_that_pass():
    assert True


def test_that_fail():
    param = 111
    assert False


@pytest.mark.parametrize('a,b,c', [(1, 1, 2), (2, 4, 7), (5, 3, 8)], ids=['First', 'Second', 'Third'])
def test_add_with_ids(a, b, c):
    assert a + b == c


@pytest.mark.my_marker
def test_with_markers():
    pass


def test_attachments():
    allure.attach.file('tests/img.jpg', name='Attachment', attachment_type=allure.attachment_type.JPG)
    allure.attach('Text rtrrrrrrrrrrrrrrrrrrrrr', name='My Test', attachment_type=allure.attachment_type.TEXT)
    allure.attach('<html><body><h1>TITLE</h1> TESTS</body></html>')
