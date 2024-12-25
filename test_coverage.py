import multiprocessing


def complex_math_verification():
    assert 1 + 1 == 2


def test_foo():
    with multiprocessing.Pool(processes=1) as pool:
        pool.apply(complex_math_verification)
        pool.close()
        pool.terminate()
    pool.join()
