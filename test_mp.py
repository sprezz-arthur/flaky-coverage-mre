from multiprocessing.pool import Pool


def complex_math_verification():
    assert 1 + 1 == 2


def test_mp_pool():
    with Pool(processes=1) as pool:
        pool.apply(complex_math_verification)
