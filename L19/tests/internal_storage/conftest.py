from L19.phonebook.contact import Contact
from L19.phonebook.phonebook import Phonebook


import pytest

@pytest.fixture()
def phonebook():
    return Phonebook()

@pytest.fixture()
def contact_with_n_phones():
    def configure_contact(phones_number):
        phones = ['111-1111-111'] * phones_number
        return Contact('John', phones=phones)
    return configure_contact
