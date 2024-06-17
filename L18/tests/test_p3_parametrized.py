import pytest

from L18.phonebook.contact import Contact



"""
0
1
5
119
120
"""

def test_contact_contains_description():
    expected_description = 'anything'
    print(len(expected_description))
    contact = Contact('John', description=expected_description)
    observed_description = contact.description
    assert observed_description == expected_description


@pytest.mark.parametrize('description', ['', 'q', 'q'*60, 'q'*119, 'q'*120], ids=['min', 'min+1', 'nominal', 'max-1', 'max'])
def test_valid_description(description):
    contact = Contact('John', description=description)
    observed_description = contact.description
    assert observed_description == description

@pytest.mark.parametrize('height,weight,expected_bmi', [(170, 80, 23), (160, 60, 23)])
def test_bmi(height, weight, expected_bmi):
    contact = Contact('John', height=height, weight=weight)
    observed_bmi = contact.body_mass_index
    assert observed_bmi == expected_bmi


@pytest.mark.parametrize('name', ['Anna', 'John'])
@pytest.mark.parametrize('birth_year', [1967, 1987])
def test_valid_user(name, birth_year):
    contact = Contact(name=name, birth_year=birth_year)
    assert len(contact.name) != 0
    assert contact.birth_year > 1900



test_data = [
    pytest.param(170, 80, 23, marks=pytest.mark.xfail(reason='JIRA-123'), id='First scenario'),
    pytest.param(160, 60, 23.44, id='Second scenario')
]

@pytest.mark.parametrize('height,weight,expected_bmi', test_data)
def test_bmi2(height, weight, expected_bmi):
    contact = Contact('John', height=height, weight=weight)
    observed_bmi = contact.body_mass_index
    assert observed_bmi == expected_bmi
