rm -rf htmlcov
rm -f .coverage
coverage run -m test_coverage > /dev/null 2>&1
coverage combine > /dev/null 2>&1
coverage report --format=total
