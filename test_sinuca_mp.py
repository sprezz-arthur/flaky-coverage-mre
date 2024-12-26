from sinuca.mp_pool import Pool


def complex_math_verification():
    assert 1 + 1 == 2


def test_sinuca_with_mp():
    with Pool(processes=1) as pool:
        pool.apply(complex_math_verification)
