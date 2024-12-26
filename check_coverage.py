import sys

import coverage


def main(short: bool):
    cov = coverage.Coverage()
    cov.load()
    data = cov.get_data()
    files = sorted(data.measured_files())
    res = ""
    for file in files:
        analysis = cov._analyze(file)
        total = len(analysis.statements)
        executed = len(analysis.executed)
        coverage_percent = (executed / total) * 100 if total > 0 else 0
        file = file.split("/")[-1]
        coverage_percent = int(coverage_percent)
        if file.startswith("test_") is False:
            continue

        res_icon = "✅" if coverage_percent == 100 else "❌"

        if short:
            res += res_icon
        else:
            print(f"{res_icon} {file}: {coverage_percent}")

    if short:
        print(res)


if __name__ == "__main__":
    short = "--short" in sys.argv[1:]
    main(short)
