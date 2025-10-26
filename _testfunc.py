def testfunc(func, args, expected):
    result = func(*args)
    assert result == expected, f"Expected {expected}, but got {result}"

    print(f"✅ Test passed: {func.__name__}{args} == {expected}")