import sys
import time
import os

# print(sys.path)
# sys.path.append('/home/olytvynov/Projects/HL/HL_courses/hl_pyauto_11apr24/L19/phonebook')
# print(sys.path)
from L19.phonebook.contact import Contact
from L19.phonebook.phonebook import Phonebook

import pytest

# def test_adding_contact():
#     phonebook = Phonebook()
#     contact = Contact('John')
#     phonebook.add_contact(contact)
#     assert len(phonebook.get_contacts()) == 1, f"Expected 1 contact but get {len(phonebook.get_contacts())}"
#
#
# def test_removing_contact():
#     phonebook = Phonebook()
#     contact = Contact('John')
#     phonebook.add_contact(contact)
#     phonebook.remove_contact(1)
#     assert len(phonebook.get_contacts()) == 0, 'Contacts not empty'

# ######################################################################################################################


# @pytest.fixture(scope='session')
# def nominal_contact():
#     return Contact('John')
#
#
# @pytest.fixture()
# def phonebook():
#     return Phonebook()
#
#
# def test_adding_contact(nominal_contact, phonebook):
#     print(id(nominal_contact))
#     phonebook.add_contact(nominal_contact)
#     assert len(phonebook.get_contacts()) == 1, f"Expected 1 contact but get {len(phonebook.get_contacts())}"
#
#
# def test_removing_contact(nominal_contact, phonebook):
#     print(id(nominal_contact))
#     phonebook.add_contact(nominal_contact)
#     phonebook.remove_contact(1)
#     assert len(phonebook.get_contacts()) == 0, 'Contacts not empty'


# ######################################################################################################################


# @pytest.fixture(scope='session')
# def nominal_contact():
#     return Contact('John')


# @pytest.fixture()
# def phonebook():
#     return Phonebook()
#
#
# @pytest.fixture()
# def phonebook_with_one_record(nominal_contact):
#     phonebook = Phonebook()
#     phonebook.add_contact(nominal_contact)
#     return phonebook


# def test_adding_contact(nominal_contact, phonebook):
#     phonebook.add_contact(nominal_contact)
#     assert len(phonebook.get_contacts()) == 1, f"Expected 1 contact but get {len(phonebook.get_contacts())}"
#
#
# def test_removing_contact(nominal_contact, phonebook_with_one_record):
#     phonebook_with_one_record.remove_contact(1)
#     assert len(phonebook_with_one_record.get_contacts()) == 0, 'Contacts not empty'

# ######################################################################################################################

# @pytest.fixture()
# def phonebook_with_autosave():
#     phonebook = Phonebook(path_to_db="contacts.json", auto_save_period=3)
#     yield phonebook
#     phonebook.close()
#
#
# def test_file_creation(nominal_contact, phonebook_with_autosave):
#     phonebook_with_autosave.add_contact(nominal_contact)
#     time.sleep(4)
#     assert os.path.exists("contacts.json"), 'File not created'
