import sys
sys.path.append('.')
import shared as sh
import pytest

def test_clean_string():
    test_str = " This is!      a, test string  "

    assert "This is a test string" == sh.clean_string(test_str), "String <{}> not cleaned as expected".format(test_str)

# https://docs.pytest.org/en/7.1.x/example/parametrize.html?highlight=parameter
compressor_data = [
    (' This is      a  test string  ', 'This is a test string')
]
@pytest.mark.parametrize("input,expected", compressor_data)
def test_compressor(input, expected):
    assert sh.space_compress(input) == expected
    assert 1 == 1


## Failing Test for Compressor
compressor_data_with_failure = [
    (' This is      a test string  ', 'This is a test string'),
    pytest.param(' This! is      a ,test string  ', 'Max is almost done with MSDS!', marks=pytest.mark.xfail),
    pytest.param('111111',111111, marks=pytest.mark.xfail(reason="String to Integer"))
]
@pytest.mark.parametrize("input,expected", compressor_data_with_failure)
def test_compressor_with_failure(input, expected):
    assert sh.space_compress(input) == expected
    assert 1 == 1


## Skip test
@pytest.mark.skip(reason="This is intentionally skipped due to incorrectness")
def test_skip():
    assert 1 == 2


## Skip Conditionally depending on OS
@pytest.mark.skipif(sys.platform == 'darwin', reason="Test set for non mac users")
def test_os_condition():
    print("My platform is", sys.platform)
    ## This test fails.
    ## if the above skipif is set to != 'darwin' I can see the test fail in my CLI. 
    assert sh.space_compress('111111') == 111111


def test_dummy_new():
    assert 1 == 2