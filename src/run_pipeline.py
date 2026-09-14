import subprocess
import sys


def run_step(script_name):
    print(f"\n=== RUNNING {script_name} ===")

    result = subprocess.run(
        [sys.executable, f"src/{script_name}"],
        check=True
    )

    return result


def main():
    print("===================================")
    print("   RETAIL SALES ETL PIPELINE")
    print("===================================")

    run_step("transform_data.py")
    run_step("validate_data.py")
    run_step("setup_database.py")
    run_step("load_database.py")

    print("\n===================================")
    print("   PIPELINE COMPLETED SUCCESSFULLY")
    print("===================================")


if __name__ == "__main__":
    main()