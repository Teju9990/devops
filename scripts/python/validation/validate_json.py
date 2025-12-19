import json
import sys
import os

FILE = "sfdx-project.json"

if not os.path.exists(FILE):
    print("sfdx-project.json not found")
    sys.exit(1)

with open(FILE, "r") as f:
    data = json.load(f)

# Validate API version
api_version = float(data.get("sourceApiVersion", 0))

if api_version < 58.0:
    print("sourceApiVersion must be >= 58.0")
    sys.exit(1)

# Validate packageDirectories
if "packageDirectories" not in data:
    print("packageDirectories missing")
    sys.exit(1)

print(f"JSON validation passed (API version {api_version})")
