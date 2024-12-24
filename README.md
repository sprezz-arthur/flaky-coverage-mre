# flaky-coverage-mre
MRE for Coverage when running code under multiprocessing


# HOW TO REPRODUCE
Just run:

```shell
rm -rf htmlcov && rm -f .coverage && coverage run -m pytest && coverage combine && coverage html
```

Sometimes the function `complex_math_verification` will show up as being fully covered. Sometimes it won't.

I still don't know how to make either case consistent.
