import subprocess
import sys


def execute_script_n_times(script_path: str, N: int) -> float:
    success_count = 0

    for i in range(1, N + 1):
        try:
            result = subprocess.run(
                ["bash", script_path],
                capture_output=True,
                text=True,
                check=True,
            )

            output = result.stdout.strip()
            if output == "100":
                success_count += 1

        except Exception as e:
            print(f"Run {i}: An unexpected error occurred: {e}")
            pass  # Count as failure

    ratio = success_count / N if N > 0 else 0.0

    print(f"Success: {success_count}/{N} ({ratio:.2%})")

    return ratio


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <script_path> <N>")
        print("  <script_path>: Path to the shell script to execute.")
        print("  <N>: Number of times to execute the script (positive integer).")
        sys.exit(1)

    script_path = sys.argv[1]
    N_arg = sys.argv[2]

    try:
        N = int(N_arg)
        if N <= 0:
            raise ValueError
    except ValueError:
        print("Error: <N> must be a positive integer.")
        sys.exit(1)

    execute_script_n_times(script_path, N)
    sys.exit(0)


if __name__ == "__main__":
    main()
