import traceback


def func_1(a):
    return a


def func_2(a):
    # return 2
    return a


def func_3(a):
    # a()
    return a


def func_4(a):
    return a


for solution in [func_1, func_2, func_3, func_4]:
    print("\n>>> ", solution.__name__, "... ", end="")

    try:
        assert solution(2) == 2, "Test 1"
        assert solution("a") == "a", "Test 2"
        assert solution(True) is True, "Test 3"
        assert solution(None) is None, "Test 4"
        print("√")

    except AssertionError:
        print("χ -- your function failed a test case --", "\n")
        traceback.print_exc()

    except Exception as e:
        print("χ -- your function had an error --", "\n")
        print("An error occurred:", e)
        traceback.print_exc()

print('\n--- all done ---')
