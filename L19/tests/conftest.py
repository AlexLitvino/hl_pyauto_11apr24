from L19.phonebook.contact import Contact

import pytest


@pytest.fixture(scope='session')
def nominal_contact():
    return Contact('John')


@pytest.fixture(scope='session', autouse=True)
def start_db_service():
    print("Starting DB...")
    yield
    print("Stopping DB...")

@pytest.fixture(scope='session')
def create_empty_tables(start_db_service):
    print("Creating tables...")