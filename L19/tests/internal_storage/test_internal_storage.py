import pytest


def test_adding_contact(nominal_contact, phonebook):
    phonebook.add_contact(nominal_contact)
    assert len(phonebook.get_contacts()) == 1, f"Expected 1 contact but get {len(phonebook.get_contacts())}"


def test_removing_contact(nominal_contact, phonebook):
    phonebook.add_contact(nominal_contact)
    phonebook.remove_contact(1)
    assert len(phonebook.get_contacts()) == 0, 'Contacts not empty'


@pytest.mark.parametrize('numbers', [1, 3, 5])
def test_contact_with_numbers(numbers, contact_with_n_phones):
    contact = contact_with_n_phones(numbers)
    assert len(contact.phones) == numbers

