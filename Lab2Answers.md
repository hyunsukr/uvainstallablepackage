## Affirm we're getting the same object
Make two calls to Singleton() stored in variables a and b. Note theassert using python's id function. When you run it, why does the assert not throw an error? (1 pt)

- The declaration of the variable A creates a new singleton instance. However, for B that is not exactly the case. The singleton instance that was already created (by delcaring A) is returned. Therefore, the id of the two instances are the same because under the hood they are the same. We can double check this by seeing the print outputs. When A is declared "initalize once" is outputted but B does not output such message. The id() function returns a unique id for the specified object, therefore since A and B are the same (B updates the counter) the assert does not throw the error. 


## Init behavior
Look at the print("INIT") statement in the __init__ function in the Singleton class.

When you run the script, notice you see two INIT messages, why? (1 pt)
- In the code there are two instances of the Singleton Object. One is assigned to the variable a, while the other one is assigned to the variable b. When singleton A is created, the __init__ function is called, which prints INIT. Similarly when the second singleton variable, b, is created another print statment is kicked off by the __init__ function. 


## Custom initializer
Now focus on the function called init_once and it's print statement.

It's called in the __new__ function with cls.instance.initialize_once()

Only one print statement from this function shows up when you run the script. Why not 2? (1 pt)
- This is because of the if clause of 'if not hasattr(cls, 'instance'):'. Since __init__ works with objects returned by __new__ the if clause is only entered once. Thust he initalize_once() function is only called once. Since the initalize_once() method is only called once, the print function within that function will only be called once. This can also be checked with the id() function of the two variables returning the same value. 

Resource: 
- https://santoshk.dev/posts/2022/__init__-vs-__new__-and-when-to-use-them/#:~:text=__new__%20returns%20a,init__%20to%20initilize%20value.
- https://www.geeksforgeeks.org/id-function-python/



## Counting references to the singleton
Note the count = 0 just below the class declaration

The __init__ function increments the count every time it is called.

Why is the printout of this variable 1, then 2, and not 1, 1 instead? (1 pt)
- The reasoning is similar to the answer shown above. If you take out the if clause in the __new__ function, 'if not hasattr(cls, 'instance'):', then the output will be 1, 1. However, since this if clause is not entered because the object already has the attribute of instance, the count is just updated. Thus, the count variable is 1, then 2. 


## Using a decorator in pytest

All tests were conducted through pytest `pytest tests/ -v`.
The test file can be found at the following

https://github.com/hyunsukr/uvainstallablepackage/blob/main/tests/test_shared.py


### Writing a passing function

```
compressor_data = [
    (' This is      a  test string  ', 'This is a test string')
]
@pytest.mark.parametrize("input,expected", compressor_data)
def test_compressor(input, expected):
    assert sh.space_compress(input) == expected
    assert 1 == 1
```

### Introducing pytest decorators
Decorators are through the test functions

### Adding a Failing test
```
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
```

### Adding a skipped test
```
@pytest.mark.skip(reason="This is intentionally skipped due to incorrectness")
def test_skip():
    assert 1 == 2
```

### Adding a skip on condition test
```
@pytest.mark.skipif(sys.platform == 'darwin', reason="Test set for non mac users")
def test_os_condition():
    print("My platform is", sys.platform)
    ## This test fails.
    ## if the above skipif is set to != 'darwin' I can see the test fail in my CLI. 
    assert sh.space_compress('111111') == 111111
```
