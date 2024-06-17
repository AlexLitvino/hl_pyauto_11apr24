from L18.phonebook.contact import Contact
import pytest

def add(a, b):
    return a + b


def test_add():
    observed = add(3, 5)
    assert observed == 9, f"Expected to get 9, but got {observed}"


def test_contact_name():
    expected_name = 'John'
    contact = Contact(name=expected_name)
    assert contact.name == expected_name


def test_nominal_bmi():
    contact = Contact('John', height=170, weight=80)
    #expected_bmi = round(80 / (1.7 * 1.7), 2)
    expected_bmi = 80 / (1.7 * 1.7)
    observed_bmi = contact.body_mass_index
    assert observed_bmi == expected_bmi, f"Expected to get {expected_bmi}, but got {observed_bmi}"


def test_rounding():
    assert pytest.approx(0.3) == 0.1 + 0.1 + 0.1


def test_rounding2():
    assert 0.3 - 1.e-6 < 0.1 + 0.1 + 0.1 < 0.3 + 1e-6


def test_rounding3():
    """10 [9, 11]"""
    assert pytest.approx(10, abs=1) == 12


def test_rounding4():
    """10 [9, 11]"""
    assert pytest.approx(10, rel=0.1) == 12


def test_rounding5():
    assert pytest.approx([10, 11, 12], abs=1) == [10, 12, 14]


def test_list_comparison():
    assert [10, 11, 12] == [10, 12, 14]

def test_invalid_description():
    description = 'q' * 121
    with pytest.raises(AssertionError, match="Set value doesn't correspond to '.{,120}' regular expression") as exc_info:
        contact = Contact('John', description=description)
    assert str(exc_info.value) == "Set value doesn't correspond to '.{,120}' regular expression"

class TestContacts:
    pass