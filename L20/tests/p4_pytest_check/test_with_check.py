# def test_several_asserts():
#     assert 1 == 1, 'Assert that passes'
#     print("Before failed assert")
#     assert 3 == 5, 'Assert that fails'
#     print("After failed assert")
#     assert 5 == 5, 'Assert that wouldn\'t be performed'


#from pytest_check import check


# def test_several_asserts_check_as_import(check):
#     assert 1 == 1, 'Assert that passes'
#     print("Before failed assert")
#     with check:
#         assert 3 == 5, 'Assert that fails'
#         print("After failed assert in context manager")
#     print("After first failed assert")
#     with check:
#         assert 5 == 6, 'Another failing assert'
#     print("After second failed assert")


from pytest_check import check

def test_several_asserts_check_validation_functions():
    check.equal(3, 6)
    print("After first assert")
    check.is_true(False)
    print("After second assert")
    check.is_in(3, [5, 7, 9])
    print("After third assert")
