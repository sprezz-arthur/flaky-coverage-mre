# flaky-coverage-mre
MRE for Coverage when running code under multiprocessing


# HOW TO REPRODUCE
Just run:

```shell
rm -rf htmlcov
rm -f .coverage
coverage run -m pytest > /dev/null 2>&1
coverage combine > /dev/null 2>&1
coverage report --format=total
```

# Stats
Given the flaky nature, you should run the problem a couple of times to detect the flakiness.

This script makes it easier:

```shell
python -m cov_stats get_cov_total.sh 100
```

Sometimes the function `complex_math_verification` will show up as being fully covered. Sometimes it won't.

I still don't know how to make either case consistent.
