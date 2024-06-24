import os
import time

from L20.phonebook.contact import Contact
from L20.phonebook.phonebook import Phonebook

import pytest


@pytest.fixture()
def phonebook(tmp_path):
    contacts_file = tmp_path / "contacts.json"
    print(f"DB: {contacts_file}")
    phonebook = Phonebook(path_to_db=contacts_file, auto_save_period=3)
    yield phonebook
    phonebook.close()


# setup_class, setup_method, teardown_method, teardown_class

class TestSavingToFile:

    def test_save_to_file(self, phonebook):
        contact = Contact('John')
        phonebook.add_contact(contact)
        time.sleep(phonebook.auto_save_period+1)
        assert os.path.exists(phonebook.path_to_db)


class TestXUnit:

    @classmethod
    def setup_class(cls):
        print("In setup_class")
        cls.nominal_contact = Contact('John')

    def setup_method(self):
        print("In setup_method")
        contacts_file = "contacts.json"
        print(f"DB: {contacts_file}")
        self.phonebook = Phonebook(path_to_db=contacts_file, auto_save_period=3)

    def test_save_to_file(self):
        self.phonebook.add_contact(self.nominal_contact)
        time.sleep(self.phonebook.auto_save_period+1)
        assert os.path.exists(self.phonebook.path_to_db)

    def teardown_method(self):
        print("In teardown_method")
        self.phonebook.close()

    @classmethod
    def teardown_class(cls):
        print("In teardown_class")


@pytest.mark.xfail(reason='JIRA-123')
@pytest.mark.parametrize('birth_year', [1900, 2000])
class TestContact:

    @pytest.mark.parametrize('description', ['', 'q'*120])
    def test_description(self, description, birth_year):
        contact = Contact('John', birth_year=birth_year, description=description)
        assert contact.description == description
