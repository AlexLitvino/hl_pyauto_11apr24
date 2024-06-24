import logging
import os
import time

import pytest


from L20.phonebook.contact import Contact
from L20.phonebook.phonebook import Phonebook

logger = logging.getLogger()


@pytest.fixture(scope='session')
def nominal_contact():
    logger.info("Creating nominal contact object...")

    return Contact('John')


@pytest.fixture()
def phonebook_with_autosave(request):

    def configure_phonebook(autosave):
        logger.info("Creating phonebook object")
        logger.error("ERROR!!!")
        logger.warning("WARNING")
        phonebook = Phonebook(path_to_db="contacts.json", auto_save_period=autosave)
        logger.debug("Created phonebook object with autosave=%s", autosave)

        def closing_phonebook():
            logger.info("Stopping phonebook object")
            phonebook.close()
        request.addfinalizer(closing_phonebook)

        return phonebook

    return configure_phonebook


def test_file_creation(nominal_contact, phonebook_with_autosave):
    phonebook = phonebook_with_autosave(autosave=3)
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