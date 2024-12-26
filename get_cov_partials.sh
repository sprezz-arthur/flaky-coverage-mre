rm -rf htmlcov
rm -f .coverage
coverage run -m pytest > /dev/null 2>&1
coverage combine > /dev/null 2>&1
python -m check_coverage