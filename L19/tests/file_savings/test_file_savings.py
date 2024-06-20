import time
import os

import pytest


# def test_file_creation(nominal_contact, phonebook):
#     phonebook.add_contact(nominal_contact)
#     time.sleep(4)
#     assert os.path.exists("contacts.json"), 'File not created'

def test_file_creation(nominal_contact, phonebook):
    phonebook.add_contact(nominal_contact)
    expected_file_path = phonebook.path_to_db
    time.sleep(4)
    assert os.path.exists(expected_file_path), 'File not created'



@pytest.mark.parametrize('autosave_period', [1, 3])
def test_file_creation_timing(autosave_period, phonebook_with_autosave, nominal_contact):
    phonebook = phonebook_with_autosave(autosave=autosave_period)
    phonebook.add_contact(nominal_contact)
    time.sleep(autosave_period+1)
    assert os.path.exists("contacts.json"), 'File not created'
