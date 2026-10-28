import os
import json
import hashlib

PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))
TEST_FOLDER = os.path.join(PROJECT_FOLDER, "test_files")
BASELINE_FILE = os.path.join(PROJECT_FOLDER, "baseline.json")


def file_hash(path):
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha.update(chunk)
    return sha.hexdigest()


def scan():
    if not os.path.isdir(TEST_FOLDER):
        print("Please create the test_files folder first.")
        return

    current = {}

    for root, _, files in os.walk(TEST_FOLDER):
        for name in files:
            path = os.path.join(root, name)
            relative = os.path.relpath(path, TEST_FOLDER)
            current[relative] = file_hash(path)

    if not os.path.exists(BASELINE_FILE):
        with open(BASELINE_FILE, "w") as f:
            json.dump(current, f, indent=4)
        print("Baseline created.")
        print("Files recorded:", len(current))
        print("Run again after changing a test file.")
        return

    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)

    changed = False

    for name, digest in current.items():
        if name not in baseline:
            print("New file:", name)
            changed = True
        elif baseline[name] != digest:
            print("MODIFIED file:", name)
            changed = True

    for name in baseline:
        if name not in current:
            print("DELETED file:", name)
            changed = True

    if not changed:
        print("No file changes detected.")

    print("Scan completed.")


if __name__ == "__main__":
    scan()