import json
import csv
import argparse
import os

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert JSON array of records into CSV."
    )
    parser.add_argument("input", help="Path to input JSON file")
    parser.add_argument("output", help="Path to output CSV file")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite output file if it already exists")    
    return parser.parse_args()

def read_json(file: str) -> list | None:
    try:
        with open(file, "r", encoding="utf-8") as f:
            loaded = json.load(f)
        return loaded
    except (OSError, json.JSONDecodeError) as e:
            print(f"Read error: {e}")

def write_csv(data: list, file: str) -> None:
    try:
        with open(file, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["city", "temperature", "humidity", "wind_speed", "timestamp"])
            writer.writeheader()
            writer.writerows(data)
            print("Saved")
    except OSError as e:
            print(f"Saving error: {e}")


def main():
    args = parse_args()
    
    data = read_json(args.input)
    
    if not data:
        return

    if os.path.exists(args.output) and not args.overwrite:
        print(f"Output file already exists: {args.output}")
        print("Use --overwrite to overwrite it.")
        return

    write_csv(data, args.output)

if __name__ == "__main__":
    main()