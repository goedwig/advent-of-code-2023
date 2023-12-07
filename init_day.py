import argparse
import datetime
import logging
import os
import subprocess
from pathlib import Path

import requests

logger = logging.getLogger(__name__)


def main(day, year, is_test_mode):
    dirname = str(day).zfill(2)
    path = Path(dirname)

    if os.path.exists(path):
        if is_test_mode:
            ts = datetime.datetime.now()
            path = Path(f"{dirname}@{ts}")
        else:
            print("Directory already exists")
            return

    os.mkdir(path)
    subprocess.run(["cp", "solution_base.py", path / "solution.py"])

    # Get input from the AoC server
    input = ""
    if session := os.getenv("SESSION"):
        try:
            response = requests.get(
                url=f"https://adventofcode.com/{year}/day/{day}/input",
                cookies={"session": session}
            )
            if response.ok:
                input = response.text
            else:
                print(
                    "Error getting data from the AoC server: "
                    f"{response.status_code=} {response.text=}",
                )
        except requests.RequestException as e:
            print(f"Error getting data from the AoC server: {e}")

    with open(path / "input.txt", "w") as f:
        if input:
            f.write(input)

    subprocess.run(["git", "add", path])


if __name__ == "__main__":
    today = datetime.date.today()
    day, year = today.day, today.year

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--day",
        metavar="[1-25]",
        type=int,
        choices=range(1, 26),
        default=day if day < 26 else 1,
    )
    parser.add_argument(
        "-y", "--year",
        metavar=f"[2015-{year}]",
        type=int,
        choices=range(2015, year + 1),
        default=year,
    )
    parser.add_argument(
        "--test-mode",
        action="store_true",
    )

    args = parser.parse_args()

    main(args.day, args.year, args.test_mode)
